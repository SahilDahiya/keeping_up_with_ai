"""Polite HTTP: per-host rate limiting, retries with backoff, robots.txt."""

from __future__ import annotations

import random
import time
import urllib.robotparser
from urllib.parse import urlsplit

import httpx

USER_AGENT = "kb-scraper/0.1 (personal research knowledge base; +https://github.com/SahilDahiya/keeping_up_with_ai)"

RETRYABLE_STATUS = {429, 500, 502, 503, 504}


class FetchError(Exception):
    pass


class Fetcher:
    def __init__(self, default_interval: float = 2.0, timeout: float = 20.0):
        self.client = httpx.Client(
            http2=True,
            follow_redirects=True,
            timeout=timeout,
            headers={"User-Agent": USER_AGENT},
        )
        self.default_interval = default_interval
        self._last_request: dict[str, float] = {}
        self._robots: dict[str, urllib.robotparser.RobotFileParser | None] = {}

    def _throttle(self, host: str, interval: float) -> None:
        last = self._last_request.get(host)
        if last is not None:
            wait = interval - (time.monotonic() - last)
            if wait > 0:
                time.sleep(wait)
        self._last_request[host] = time.monotonic()

    def _robots_for(self, host: str, scheme: str) -> urllib.robotparser.RobotFileParser | None:
        if host not in self._robots:
            rp = urllib.robotparser.RobotFileParser()
            try:
                resp = self.client.get(f"{scheme}://{host}/robots.txt")
                if resp.status_code == 200:
                    rp.parse(resp.text.splitlines())
                    self._robots[host] = rp
                else:
                    self._robots[host] = None  # no robots -> everything allowed
            except httpx.HTTPError:
                self._robots[host] = None
        return self._robots[host]

    def allowed_by_robots(self, url: str) -> bool:
        parts = urlsplit(url)
        rp = self._robots_for(parts.netloc, parts.scheme)
        if rp is None:
            return True
        return rp.can_fetch(USER_AGENT, url)

    def get(self, url: str, *, interval: float | None = None, retries: int = 3) -> httpx.Response:
        host = urlsplit(url).netloc
        interval = interval if interval is not None else self.default_interval
        last_error: Exception | None = None
        for attempt in range(retries):
            self._throttle(host, interval)
            try:
                resp = self.client.get(url)
            except httpx.HTTPError as e:
                last_error = e
                time.sleep(2**attempt + random.random())
                continue
            if resp.status_code in RETRYABLE_STATUS:
                retry_after = resp.headers.get("retry-after")
                delay = float(retry_after) if retry_after and retry_after.isdigit() else 2**attempt + random.random()
                last_error = FetchError(f"HTTP {resp.status_code} for {url}")
                time.sleep(delay)
                continue
            if resp.status_code >= 400:
                raise FetchError(f"HTTP {resp.status_code} for {url}")
            return resp
        raise FetchError(f"gave up on {url}: {last_error}")

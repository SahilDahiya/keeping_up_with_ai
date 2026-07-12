"""SQLite bookkeeping: which URLs we've seen, fetched, and filed.

Scraper-internal only — the knowledge base never depends on this file.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from .config import STATE_PATH

_SCHEMA = """
CREATE TABLE IF NOT EXISTS articles (
    url            TEXT PRIMARY KEY,   -- normalized canonical URL
    source         TEXT NOT NULL,
    first_seen     TEXT NOT NULL,
    last_fetched   TEXT,
    etag           TEXT,
    last_modified  TEXT,               -- HTTP Last-Modified or sitemap lastmod
    content_sha256 TEXT,
    kb_path        TEXT,               -- repo-relative path once filed
    status         TEXT NOT NULL,      -- inbox | filed | failed | skipped
    skip_reason    TEXT                -- why a URL was intentionally excluded
);
CREATE INDEX IF NOT EXISTS idx_articles_source ON articles(source);
"""


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class State:
    def __init__(self, path: Path = STATE_PATH):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(_SCHEMA)
        self._migrate()

    def _migrate(self) -> None:
        cols = {row["name"] for row in self.conn.execute("PRAGMA table_info(articles)")}
        if "skip_reason" not in cols:
            self.conn.execute("ALTER TABLE articles ADD COLUMN skip_reason TEXT")
            self.conn.commit()

    def get(self, url: str) -> sqlite3.Row | None:
        return self.conn.execute("SELECT * FROM articles WHERE url = ?", (url,)).fetchone()

    def record_fetched(self, url: str, source: str, *, sha256: str, etag: str | None,
                       last_modified: str | None, status: str = "inbox",
                       kb_path: str | None = None) -> None:
        existing = self.get(url)
        first_seen = existing["first_seen"] if existing else _now()
        # A re-fetch of an already-filed article keeps its kb_path/filed status.
        if existing and existing["status"] == "filed" and status == "inbox":
            status = "filed"
            kb_path = existing["kb_path"]
        self.conn.execute(
            """INSERT INTO articles (url, source, first_seen, last_fetched, etag,
                                     last_modified, content_sha256, kb_path, status, skip_reason)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)
               ON CONFLICT(url) DO UPDATE SET
                 last_fetched=excluded.last_fetched, etag=excluded.etag,
                 last_modified=excluded.last_modified,
                 content_sha256=excluded.content_sha256,
                 kb_path=COALESCE(excluded.kb_path, kb_path),
                 status=excluded.status,
                 skip_reason=NULL""",
            (url, source, first_seen, _now(), etag, last_modified, sha256, kb_path, status),
        )
        self.conn.commit()

    def mark(self, url: str, source: str, status: str, kb_path: str | None = None,
             skip_reason: str | None = None) -> None:
        existing = self.get(url)
        reason = skip_reason if status == "skipped" else None
        path_value = None if status == "skipped" else kb_path
        if existing:
            self.conn.execute(
                """UPDATE articles
                      SET status = ?,
                          kb_path = CASE WHEN ? THEN NULL ELSE COALESCE(?, kb_path) END,
                          skip_reason = ?
                    WHERE url = ?""",
                (status, status == "skipped", path_value, reason, url),
            )
        else:
            self.conn.execute(
                """INSERT INTO articles (url, source, first_seen, status, kb_path, skip_reason)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (url, source, _now(), status, path_value, reason),
            )
        self.conn.commit()

    def needs_fetch(self, url: str, lastmod_hint: str | None) -> bool:
        """Unknown URL, or upstream says it changed since we last fetched."""
        row = self.get(url)
        if row is None:
            return True
        if row["status"] == "failed":
            return True  # retry failures on later runs
        if lastmod_hint and row["last_fetched"] and lastmod_hint > row["last_fetched"]:
            return True
        return False

    def counts(self) -> list[sqlite3.Row]:
        return self.conn.execute(
            "SELECT source, status, COUNT(*) AS n FROM articles GROUP BY source, status ORDER BY source"
        ).fetchall()

    def skip_counts(self) -> list[sqlite3.Row]:
        return self.conn.execute(
            """SELECT COALESCE(skip_reason, 'unknown') AS reason, COUNT(*) AS n
                 FROM articles
                WHERE status = 'skipped'
                GROUP BY COALESCE(skip_reason, 'unknown')
                ORDER BY n DESC, reason"""
        ).fetchall()

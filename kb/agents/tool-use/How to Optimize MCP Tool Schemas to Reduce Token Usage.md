---
title: How to Optimize MCP Tool Schemas to Reduce Token Usage
kind: blog
topic: agents
subtopic: tool-use
secondary_topics:
- infra-platform/cost
summary: Shows how MCP tool definitions consume context tokens and how to engineer
  them for efficiency, using a Rust weather MCP server (Open-Meteo, built on the sans-IO
  'mercutio' library) as the worked example for tightening the tool schemas and descriptions
  that Claude and other agents ingest on every request.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/engineering-mcp-tools-for-token-efficiency
author: Marc
published: '2026-04-16'
fetched: '2026-07-16T22:03:48Z'
classifier: claude
taxonomy_rev: 2
words: 2697
content_sha256: a3b17359a59104aab9c90bff072a169b4df1b62846e3ead02f77aec28d8704a3
---

# How to Optimize MCP Tool Schemas to Reduce Token Usage

One of the most fun things to do is writing a new MCP server. There's something magical when it comes together, and you see it working for the first time with an agent. Something about being more than the sum of its parts and all that. The general act of writing one has been [covered by Peter](https://cetra3.github.io/blog/creating-mcp-servers-in-rust/) already, but I found that as I accumulate more of these nifty helpers, I find myself wanting to apply a bit more engineering to how the tool integrates with Claude and friends, so that is what we are going to look at today.

As a refresher, the Model Context Protocol (MCP) specifies a standard way for making tools, i.e. callable external services or programs, available to an agent, by injecting a bit of text describing the tool and its arguments, and offering a standardized pattern for calling these. Put a little more plain, when working properly, it will inject a bit of text like "there is a function to read calendar entries called `read_calendar(day)`, you should use it when you need to know what the user is doing on a particular day" at the start and provide the actual `read_calendar` function that the agent software (e.g. Claude Code) can forward the function call to. If this looks like [remote procedure calls](https://en.wikipedia.org/wiki/Remote_procedure_call) but with extra steps in plain English to you, well, that's sort of what it is.

Libraries exist to make this easier and save you from having to worry about the protocol specifics, the most popular one in Rust being `rmcp` at the moment. Plenty documentation and examples exist on how to use it, which is why I do not feel bad for pulling a bait-and-switch now, as I'll be using my own [ mercutio](https://crates.io/crates/mercutio) library instead. Once written because I am a big believer in 

[sans-IO](https://www.firezone.dev/blog/sans-io), it also has the advantage of lacking a lot of

`rmcp`'s features, too, thus being easier to explain!

The most bog-standard blueprint for an MCP server is one that wraps an existing API. These tend to be quick to write; since given a thorough API spec, any coding agent is able to crank out a serviceable implementation for a client. The weather example might be a little tired by now, but since I am actually stuck in a place where there is no coverage through the Google weather API (unlike the website) that I used for my previous weather MCP implementation, we'll be using the service I should have gone with in the first place, [Open-Meteo](https://open-meteo.com/).

After a short heart-to-heart with your favorite [clanker](https://en.wikipedia.org/wiki/Clanker) you should have a nicely contained API client ready:

```
#[tokio::test]
#[ignore]
async fn forecast_berlin() {
    let client = OpenMeteoClient::new();
    let mut request = ForecastRequest::new(Coords {
        latitude: 52.52,
        longitude: 13.41,
    });
    request.forecast_days(3);
    let forecast = client.forecast(&request).await.expect("forecast failed");
    println!("{forecast:#?}");
    assert!((forecast.latitude - 52.52).abs() < 0.1);
    assert!((forecast.longitude - 13.41).abs() < 0.1);
    assert!(forecast.hourly.is_some());
    assert!(forecast.daily.is_some());
}
```
Mark your API tests as `#[ignore]`, we do not want to abuse the free tier of the Open-Meteo service if we can help it. And if you are using this in production software instead of a personal use experiment, be a good citizen and add some caching!


An interesting part is whether to return structured data to the LLM (often JSON), or natural language prose. Answering this question is a rabbit hole a little outside the scope of this article, but in general, it boils down to returning either JSON data or a string. There is ongoing debate and some indicators that for weather data returning structured data might be better, but the responses from Open-Meteo are column-oriented, i.e. when requesting temperature and humidity for a week, you will not get one row per day, but rather two lists with seven elements each.

Since we need to transform the data anyway, and this service is less about processing it further and more about presenting it to the user, we'll opt for returning presentable markdown straight away.


I found snapshot testing to be something whose value one only really appreciates after it first solves a problem. Once it clicks, you will find more and more applications for it. It can be tempting to do too much, i.e. to opt for a rendering+snapshot approach when a "regular" test would have been a better fit. In our case we are safe, as we want to capture how our returned results are presented to the caller.

A great tool for snapshot testing in Rust is [ cargo insta](https://crates.io/crates/insta), which is a complete toolkit to handle both checking and updating of snapshots. After capturing a response from the API either through a bespoke one-off test or by curling it to a file, we can parse it and compare our rendering of it:

```
#[test]
fn display_forecast() {
    let json = include_str!("open_meteo/forecast_snapshot.json");
    let forecast: Forecast = serde_json::from_str(json).expect("parse failed");
    insta::assert_snapshot!(forecast.to_string(), @r"
    ## Weather Forecast
    **Location:** 52.52°N, 13.42°E (38 m)
    **Timezone:** Europe/Berlin (GMT+2)
    ### Daily Summary
    | Date       | Precip % | High | Low | Conditions    |
    |------------|----------|------|-----|---------------|
    | 2026-04-01 | 3%       | 12°  | 0°  | Light showers |
    | 2026-04-02 | 18%      | 12°  | 3°  | Overcast      |
    | 2026-04-03 | 30%      | 9°   | 2°  | Light rain    |
    ### Hourly Forecast
    | Time  | Precip % | Temp | Conditions    |
    |-------|----------|------|---------------|
    | 00:00 | 3%       | 5°   | Light showers |
    | 01:00 | 0%       | 5°   | Partly cloudy |
    | 02:00 | 0%       | 4°   | Mostly clear  |
    | 03:00 | 0%       | 3°   | Clear         |
    | 04:00 | 0%       | 3°   | Fog           |
...
    ");
}
```
You'll notice the tables look nice. This is thanks to [ comfy-table](https://crates.io/crates/comfy-table), which you should reach for sooner than later, when you're 20 minutes deep into writing your own text formatting functions. It even comes with a nice LLM-friendly 

[preset!](https://docs.rs/comfy-table/latest/comfy_table/presets/constant.ASCII_MARKDOWN.html)

`ASCII_MARKDOWN`A key point here is that snapshot testing fulfills a dual purpose: it tests and pins the output, but more importantly, it also makes it *visible* in the first place! Otherwise we would be stuck inspecting it once or twice during manual test runs!

If you're working in Python rather than Rust, Alex has written about the equivalent workflow using [inline-snapshot](https://pydantic.dev/articles/inline-snapshot).


The response is half of what the LLM sees, it is what is output after a call. For it to be able to make a call in the first place, we have to define the tool, here's how to do it using `mercutio`:

```
tool_registry! {
    Weather2("weather2", "Weather forecast using Open-Meteo. Returns current conditions, \
        hourly forecast with temperature, humidity, precipitation, wind, and UV index, \
        plus daily forecast with highs, lows, and sunrise/sunset times. \
        Free API, no key required.") {
        /// Location to get weather for. Can be a street address
        /// (e.g. "123 Main St, Springfield"), a place name (e.g. "Eiffel Tower, Paris"),
        /// coordinates as {lat, lon}, or a Google Place ID from search results.
        location: Location,
        /// Number of hours to include in the hourly forecast table.
        /// Valid range is 1-384 hours (up to 16 days). Defaults to 24 hours if not
        /// specified. Higher values provide more forecast data but increase response size.
        forecast_hours: Option<u32>,
        /// Number of days to include in the daily forecast table. Valid range is 1-16 days.
        /// Defaults to 3 days if not specified. Each day includes high/low temperatures,
        /// conditions, precipitation chance, and sun times.
        forecast_days: Option<u8>,
    },
}
```
The `tool_registry!` macro handles the boilerplate of deriving the subset of JSON schema that MCP uses. We can use a snapshot test to make it visible:

```
#[test]
fn weather2_tool_schema_is_stable() {
    let def = mercutio::ToolDefinition::from_tool::<Weather2>();
    let json = serde_json::to_value(&def.input_schema).expect("schema serializes");
    insta::assert_snapshot!(serde_json::to_string_pretty(&json).expect("formatting failed"));
}
```
```
{
  "properties": {
    "forecast_days": {
      "description": "Number of days to include in the daily forecast table. Valid range is 1-16 days. Defaults to 3 days if not specified. Each day includes high/low temperatures, conditions, precipitation chance, and sun times.",
      "format": "uint8",
      "minimum": 0.0,
      "type": "integer"
    },
    "forecast_hours": {
      "description": "Number of hours to include in the hourly forecast table. Valid range is 1-384 hours (up to 16 days). Defaults to 24 hours if not specified. Higher values provide more forecast data but increase response size.",
      "format": "uint32",
      "minimum": 0.0,
      "type": "integer"
    },
    "location": {
      "anyOf": [
        {
          "properties": {
            "lat": { "type": "number" },
            "lon": { "type": "number" }
          },
          "required": ["lat", "lon"],
          "type": "object"
        },
        {
          "properties": {
            "place_id": { "type": "string" }
          },
          "required": ["place_id"],
          "type": "object"
        },
        { "type": "string" }
      ],
      "description": "Location to get weather for. Can be a street address (e.g. \"123 Main St, Springfield\"), a place name (e.g. \"Eiffel Tower, Paris\"), coordinates as {lat, lon}, or a Google Place ID from search results."
    }
  },
  "required": ["location"],
  "type": "object"
}
```

Input to any LLM and thus coding agent is preprocessed before it is seen by the model. The text is broken up into chunks that may or may not be words, parts of words or a combination of punctuation, then ultimately mapped into a vector of integers to eventually form the input tensor, a fancy multidimensional matrix. The end result of the generation process maps integers back to chunks, producing output text. For this reason, we measure input and output sizes of coding agents in tokens.

The context window of an LLM agent is its operating memory, similar to the register set of a CPU -- it is all it sees at any given point in time, and additional data must be loaded to be available. In other words, it is the only thing an LLM perceives outside its fixed training data, so it is a precious resource, as every source file you operate on must pass through it.

Claude's Opus 4.5 for example has a context window size of 200k tokens, while Opus 4.6 offers a million. This sounds like a lot, but usually part of it is reserved for compaction, and all tools and system prompts need to be placed into it as well. The jump from 200k to one million is not a panacea, as less "full" context windows tend to produce better results.

If you want to see what's in your context window, you can type `/context` into a Claude Code prompt and find out. Here is an example using Opus 4.5:

```
Estimated usage by category
# System prompt: 2.5k tokens (1.3%)
# System tools: 16.6k tokens (8.3%)
# MCP tools: 3.3k tokens (1.6%)
# Custom agents: 36 tokens (0.0%)
# Memory files: 8.2k tokens (4.1%)
# Skills: 157 tokens (0.1%)
# Messages: 8.1k tokens (4.0%)
. Free space: 116k (58.1%)
- Autocompact buffer: 45.0k tokens (22.5%)
```
This shows moderate agent use, with 8.1k tokens being my inputs and the respective agents outputs under "messages". Still, I barely have half of the 200k tokens left over (116k or 58.1%). As I accumulate more and more tools, the "MCP tools" section is likely to grow and take away even more of that.

Getting more concrete, the input `{"hello": "world"}` might be tokenized as `{"` - `hello` - `":` - `"` - `world` - `"}`, which is 6 tokens. We can actually measure this even though tokenization is model-specific, for example the anthropic API offers a [ count_tokens](https://platform.claude.com/docs/en/build-with-claude/token-counting) endpoint if you have an API key. Alternatively there's a helpful third-party 

[online tool](https://claude-tokenizer.vercel.app/)to do the same available (which I fed the hello world example above into and guessed the tokenization afterwards).


Feeding our tool definition into the token counter, we get a rather mediocre result: 418 tokens. Goethe's dedication in [ Faust](https://en.wikipedia.org/wiki/Goethe%27s_Faust) in the 

[original German](https://www.gutenberg.org/cache/epub/21000/pg21000.txt)clocks in slightly above that, so this seems a little excessive to describe a single function that returns the current weather.

This is where our snapshot testing becomes useful: an alteration to the comments might not seem impactful at first glance, but it can have a huge impact on how effective an MCP server is. For this reason alone it is worth it, but we can now make our comments more succinct and less verbose in an effort to curb the token usage:

```
Weather2("weather2", "Weather forecast using Open-Meteo (free, no API key)") {
    /// Address, place name, or coordinates.
    location: Location,
    /// Number of hours to forecast, 1-384 (default: 24).
    forecast_hours: Option<u32>,
    /// Number of days to forecast, 1-16 (default: 3).
    forecast_days: Option<u8>,
},
```
That gets us down to 377 -- not huge savings, but every bit counts. However there is another low-hanging fruit that might taste quite sweet when plucked: The `Location` type. Type safety inside Rust is great, but for an LLM it does not matter much and it works equally well from an example. Instead of having the complex `anyOf` Location type, let's use a string and parse the input instead:

```
/// A location specified as coordinates, address, or place ID.
///
/// Parses from a string, detecting the format automatically:
/// - `"48.858, 2.294"` for coordinates (comma-separated lat, lon)
/// - `"place_id:ChIJ..."` for explicit place ID
/// - `"ChIJ..."` / `"GhIJ..."` / `"Ei..."` auto-detected as place IDs (single word, valid base64)
/// - Anything else treated as an address to geocode
#[derive(Clone, Debug, Deserialize, Serialize)]
#[serde(from = "String")]
pub enum Location {
    /// Geographic coordinates.
    Coords(Coords),
    /// Google Place ID.
    PlaceId {
        /// Place ID from search results.
        place_id: String,
    },
    /// Address or place name to be geocoded.
    Address(String),
}
impl From<String> for Location {
    fn from(s: String) -> Self {
        let s = s.trim();
        // Explicit place_id: prefix
        if let Some(id) = s.strip_prefix("place_id:") {
            return Location::PlaceId {
                place_id: id.trim().to_string(),
            };
        }
        // Try "lat, lon" format
        if let Some((lat, lon)) = s.split_once(',')
            && let (Ok(lat), Ok(lon)) = (lat.trim().parse(), lon.trim().parse())
        {
            return Location::Coords(Coords {
                latitude: lat,
                longitude: lon,
            });
        }
        // Auto-detect place IDs: single word + known prefix + valid base64
        if !s.contains(char::is_whitespace)
            && (s.starts_with("ChIJ") || s.starts_with("GhIJ") || s.starts_with("Ei"))
            && URL_SAFE_NO_PAD.decode(s).is_ok()
        {
            return Location::PlaceId {
                place_id: s.to_string(),
            };
        }
        Location::Address(s.to_string())
    }
}
// Manual `JsonSchema` implementation to make it look like a `String`:
impl JsonSchema for Location {
    // ...
    fn json_schema(_gen: &mut schemars::r#gen::SchemaGenerator) -> schemars::schema::Schema {
        use schemars::schema::{InstanceType, SchemaObject};
        SchemaObject {
            instance_type: Some(InstanceType::String.into()),
            ..Default::default()
        }
        .into()
    }
}
```
Our anyOf-soup of types can now be replaced by providing examples on our string in our tool definition:

```
/// Address, place name, or coordinates. Examples: "Av. Gustave Eiffel, 75007 Paris, France", "Eiffel Tower" or "48.858093, 2.294694".
location: String,
```
This gives us our final JSON-schema tool definition in our snapshot test:

```
{
  "properties": {
    "forecast_days": {
      "description": "Number of days to forecast, 1-16 (default: 3).",
      "format": "uint8",
      "minimum": 0.0,
      "type": "integer"
    },
    "forecast_hours": {
      "description": "Number of hours to forecast, 1-384 (default: 24).",
      "format": "uint32",
      "minimum": 0.0,
      "type": "integer"
    },
    "location": {
      "description": "Address, place name, or coordinates. Examples: \"Av. Gustave Eiffel, 75007 Paris, France\", \"Eiffel Tower\" or \"48.858093, 2.294694\".",
      "type": "string"
    }
  },
  "required": [
    "location"
  ],
  "type": "object"
}
```
This now clocks in at **233** tokens, a 44% reduction in token usage. We could probably think about combining the forecast length parameter to improve this even further, but leave this as an exercise to the reader.


Snapshot testing is an invaluable tool, especially when the output to another system is "plain english text" in some form and needs manual inspection. By pinning it with a test, we are able to both inspect it and are protected against accidental changes, which is especially useful with output generated from places that otherwise are not perceived as particularly high-impact when changed, such as comments.

This pattern is not restricted to locations, of course. "Stringifying" your API may go against instinct for many, but it can be the right choice, making examples the surrogate type annotations instead, all in the name of LLM friendliness -- after all, no other users should see this particular interface!

All this combined lets us have excellent control over what our LLM "sees" without any guesswork. So, go forth and wrap your favorite API in an MCP server, and maybe drop me a line once you have!

We have just updated the Logfire MCP. Looking for a tool to debug your telemetry data? Try it out [https://logfire.pydantic.dev](https://logfire.pydantic.dev) ([docs](https://pydantic.dev/docs/logfire/integrations/llms/mcp/)) and tell us what you think!

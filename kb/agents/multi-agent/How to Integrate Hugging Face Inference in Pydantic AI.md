---
title: How to Integrate Hugging Face Inference in Pydantic AI
kind: blog
topic: agents
subtopic: multi-agent
secondary_topics:
- inference/serving
summary: Integrates Hugging Face Inference Providers (unified access to open models
  via Groq, Cerebras, Together AI, SambaNova) as a Pydantic AI model provider, then
  builds a multi-agent flight-booking system where one agent delegates to another,
  powered by Kimi K2 on Together AI.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/hugging-face-inference-providers-in-pydantic-ai
author: Célina Hanouti
published: '2025-08-05'
fetched: '2026-07-16T22:05:08Z'
classifier: claude
taxonomy_rev: 2
words: 1246
content_sha256: 7a17f8aec53d9c01c0ac080e74ae85cde4d36353b02c7ffa5fa580522b851e4c
---

# How to Integrate Hugging Face Inference in Pydantic AI

*The following is a guest post from  Hugging Face*


![Hugging Face x Pydantic AI Integration](https://pydantic.dev/assets/blog/hugging-face-post/HFIP_in_PAI_light.png)


We're excited to announce that [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers/index) is now integrated as a model provider in [Pydantic AI](https://pydantic.dev/docs/ai/overview/)! Hugging Face's Inference Providers give developers a single API to access thousands of open‑source LLMs through world‑class partners like Groq, Cerebras, Together AI, SambaNova, and more, with no markup on provider rates.

Pydantic AI is a Python framework for building production‑grade AI agents with the same simplicity FastAPI brought to web development. With Hugging Face Inference Providers now integrated, you can combine Pydantic AI's developer‑friendly agent framework with instant access to thousands of open-source LLMs through a single, unified API.

To show how easy it is to get started, let's build a multi‑agent flight booking system. In this example, we'll create a simple flow where one agent delegates tasks to another to find the best flights for a user. We'll power it with the [Kimi K2](https://huggingface.co/moonshotai/Kimi-K2-Instruct) running with [Together AI](https://www.together.ai/) inference provider.


Install the required packages:

```
pip install "pydantic-ai-slim[huggingface]"
```
Get your Hugging Face token:

- Sign up at [huggingface.co](https://huggingface.co)
- Create an access token in your [settings](https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained).
- Set the environment variable:

```
export HF_TOKEN='your_hf_token'
```
💡 **Pro tip:** The free tier gives you monthly inference credits to start building and experimenting. Upgrade to [Hugging Face PRO](https://huggingface.co/pro) for even more flexibility, $2 in monthly credits plus pay‑as‑you‑go access to all providers!


We start by defining two Pydantic models FlightDetails and SeatPreference. These models describe the structured outputs we expect from the agents, such as flight number, airline, price, and seat selection. Pydantic automatically validates field types, constraints, and required values, ensuring that every agent response matches the expected schema without extra parsing or manual checks.

```
import datetime
from typing import Literal
from pydantic import BaseModel, Field
# Pydantic automatically validates:
# - Field types (str, int, date)
# - Field constraints (airport codes, price ranges)
# - Required vs optional fields
class FlightDetails(BaseModel):
    """
    Structured flight information that AI will return.
    """
    flight_number: str = Field(description="Flight identifier like 'UA123'")
    airline: str = Field(description="Airline name like 'United Airlines'")
    price: int = Field(ge=50, le=5000, description="Price in USD")
    origin: str = Field(description='Three-letter airport code like SFO')
    destination: str = Field(description='Three-letter airport code like JFK')
    departure_time: str = Field(description="Time like '08:00 AM'")
    date: datetime.date = Field(description="Flight date")
# The Literal type restricts seat letters to valid airplane seats. Field constraints ensure realistic row numbers.
class SeatPreference(BaseModel):
    """
    Seat selection with automatic validation.
    """
    row: int = Field(ge=1, le=30, description="Seat row number")
    seat: Literal['A', 'B', 'C', 'D', 'E', 'F'] = Field(description="Seat letter")
class NoFlightFound(BaseModel):
    """
    Returned when no suitable flight is found.
    """
    reason: str = Field(description="Why no flight was found")
```

We will use [Kimi K2](https://huggingface.co/moonshotai/Kimi-K2-Instruct) powered by Together AI via Hugging Face Provider:

```
from pydantic_ai.models.huggingface import HuggingFaceModel
from pydantic_ai.providers.huggingface import HuggingFaceProvider
model = HuggingFaceModel(
    'moonshotai/Kimi-K2-Instruct',
    provider=HuggingFaceProvider(provider_name='together')
)
```

We then define two agents: The flight agent is responsible for extracting flight details and finding the cheapest option based on user input. The seat agent is called by the flight agent to handle seat selection according to user preferences and flight context.

```
from pydantic_ai import Agent
flight_agent = Agent(
    model,
    output_type=FlightDetails | NoFlightFound,  # Can return either flight details or no flight found
    instructions="""
        You are a flight search expert. Extract flight information from text and
        find the cheapest option that matches the user's criteria.
        If you find a suitable flight, return FlightDetails with: flight number, airline, price, origin, destination, time, and date.
        If no suitable flight matches the criteria, return NoFlightFound with the reason.
    """
)
seat_agent = Agent(
    model,
    output_type=SeatPreference,  # This ensures we get a validated SeatPreference object
    instructions="""
        You are a seat selection expert. Understand user preferences and select appropriate seats.
        Seat guide:
        - A and F seats: Window seats (great views)
        - C and D seats: Aisle seats (easy access)
        - B and E seats: Middle seats (usually avoided)
    """
)
```

For this tutorial, we supply mock flight data. In a real‑world application, this would be downloaded from a booking site, potentially using another agent to navigate the site.

```
FLIGHT_DATA = """
🛫 AVAILABLE FLIGHTS - Multiple Routes - January 10, 2025
=== SAN FRANCISCO (SFO) TO ANCHORAGE (ANC) ===
1. Flight SFO-AK123 - Alaska Airlines
   Price: $350 | Departure: 08:00 AM
   Aircraft: Boeing 737-800
2. Flight SFO-AK456 - Alaska Airlines
   Price: $380 | Departure: 02:30 PM
   Aircraft: Airbus A320
=== CROSS-COUNTRY FLIGHTS ===
3. Flight NYC-LA101 - American Airlines
   Price: $280 | Departure: 09:15 AM
   Route: SFO → ANC (via connection)
4. Flight BOS-SEA303 - JetBlue Airways
   Price: $120 | Departure: 06:00 AM
   Route: BOS → ANC (via Seattle)
   Note: Budget option with layover
=== PREMIUM OPTIONS ===
5. Flight SFO-AK789 - United Airlines
   Price: $450 | Departure: 11:00 AM
   Aircraft: Boeing 777 | First Class Available
6. Flight DFW-ANC404 - Delta Airlines
   Price: $320 | Departure: 03:45 PM
   Route: SFO → ANC (direct)
"""
REQ_ORIGIN = 'SFO'
REQ_DESTINATION = 'ANC'
REQ_DATE = datetime.date(2025, 10, 10)
```

Finally, the flight agent finds the cheapest flight matching the criteria, then delegates seat selection to the seat agent by passing relevant context. The seat agent returns an optimal seat, and the final booking summary combines both agents' outputs.

```
from rich.prompt import Prompt
import asyncio
async def main():
    message_history = None
    while True:
        print(f"\n🔍 Searching for flights from {REQ_ORIGIN} to {REQ_DESTINATION} on {REQ_DATE}...")
        result = await flight_agent.run(
            f'Find me a flight from {REQ_ORIGIN} to {REQ_DESTINATION} on {REQ_DATE}.\n\nAvailable flights:\n{FLIGHT_DATA}',
            message_history=message_history,
        )
        if isinstance(result.output, NoFlightFound):
            print(f'❌ No flight found: {result.output.reason}')
            break
        else:
            flight = result.output
            print(f'✅ Flight found: {flight.airline} {flight.flight_number} - ${flight.price}')
            print(f'   Route: {flight.origin} → {flight.destination} at {flight.departure_time}')
            answer = Prompt.ask(
                'Do you want to buy this flight, or keep searching?',
                choices=['buy', 'search'],
                default='buy'
            )
            if answer == 'buy':
                seat = await find_seat()
                print(f'\n💳 Purchasing {flight.airline} {flight.flight_number} seat {seat.row}{seat.seat}...')
                print(f'✨ Booking complete! Total: ${flight.price} 🛫')
                break
            else:
                print("\n🔄 Continuing search for other options...")
                message_history = result.all_messages()
async def find_seat() -> SeatPreference:
    """
    Interactive seat selection with user prompts.
    """
    message_history = None
    while True:
        answer = Prompt.ask('\n🪑 What seat would you like? (e.g., "window seat in row 8", "aisle seat")')
        result = await seat_agent.run(
            answer,
            message_history=message_history,
        )
        if isinstance(result.output, SeatPreference):
            seat = result.output
            print(f'✅ Selected seat: {seat.row}{seat.seat}')
            return seat
        else:
            print('❌ Could not understand seat preference. Please try again.')
            message_history = result.all_messages()
if __name__ == "__main__":
    asyncio.run(main())
```
Below is an example of what the output looks like when you run the script. You can find the full script [here](https://gist.github.com/hanouticelina/b3474f466c2f256935e6e271aa46fb0e).

```
> python flight_booking.py
🛫 Flight Booking: SFO → ANC on 2025-10-10
🔍 Searching flights...
✅ Found: Alaska Airlines SFO-AK123 - $350 08:00 AM
Book this flight? [y/n/search] (y): y
🪑 Seat Selection (A,F=window | C,D=aisle | B,E=middle)
Seat preference: window seat in any row between 1 and 10
✅ Selected: 7A (Window)
🎉 Booked! Alaska Airlines SFO-AK123, Seat 7A - $350
```

Getting started with Pydantic AI and Hugging Face Inference Providers is very easy—the tutorial shows how a few lines of code create a working LLM app. But you can go much further, using Pydantic AI's built‑in tools and integrating with MCP servers to build more advanced, production‑ready agents.

- You can find more details about Hugging Face Inference Providers in the [documentation](https://huggingface.co/docs/inference-providers/index).
- Subscribe to [PRO](https://huggingface.co/pro)to get access to inference credits, pay‑as‑you‑go, and more.
- **Check out the Pydantic AI**to learn how to build production‑ready AI agents with Hugging Face's Inference Providers!- [documentation](https://pydantic.dev/docs/ai/models/huggingface/)

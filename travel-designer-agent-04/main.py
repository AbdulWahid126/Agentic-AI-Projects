import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool, handoff, set_tracing_disabled

set_tracing_disabled(disabled=True)
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=provider,
)

@function_tool
def get_flights(destination: str) -> str:
    flights = {
        "Tokyo": "Flight PIA-202 | Departure: Karachi | Arrival: Tokyo | Duration: 10h",
        "Paris": "Flight PK-111 | Departure: Lahore | Arrival: Paris | Duration: 8.5h",
    }
    return flights.get(destination, "No flights found.")

@function_tool
def suggest_hotels(destination: str) -> str:
    hotels = {
        "Tokyo": "1. Tokyo Garden Hotel\n2. Sakura Inn\n3. Capsule Heaven",
        "Paris": "1. Hotel de Paris\n2. Eiffel Suites\n3. Cozy Corner"
    }
    return hotels.get(destination, "No hotels available.")

destination_agent = Agent(
    name="DestinationAgent",
    instructions=(
        "Ask user about mood or interests. Based on that, recommend a city.\n"
        "Then call: handoff(BookingAgent, input='Paris')"
    ),
    model=model
)

booking_agent = Agent(
    name="BookingAgent",
    instructions="Use tools to suggest flights and hotels based on destination.",
    model=model,
    tools=[get_flights, suggest_hotels]
)

explore_agent = Agent(
    name="ExploreAgent",
    instructions="Recommend tourist attractions and food for the destination.",
    model=model
)

main_agent = Agent(
    name="TravelDesignerAgent",
    instructions=(
        "You are a travel planner. First, use handoff to DestinationAgent.\n"
        "DestinationAgent will find a place and pass control to BookingAgent.\n"
        "Then handoff to ExploreAgent for things to do and eat."
    ),
    model=model,
    handoffs=[
        handoff(destination_agent),
        handoff(booking_agent),
        handoff(explore_agent)
    ]
)

user_input = input("Where do you want to go? (e.g., I want a peaceful nature trip): ")

result = Runner.run_sync(
    main_agent,
    user_input,
)

print("🧳 Final Travel Plan:\n", result.final_output)
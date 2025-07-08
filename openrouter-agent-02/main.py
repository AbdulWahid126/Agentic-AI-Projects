import asyncio
import os
from openai import AsyncOpenAI # chat completions
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv

set_tracing_disabled(disabled=True) # Open AI Tracing == Disable

load_dotenv()

api_key = os.getenv('OPENROUTER_API_KEY')
base_url = os.getenv('OPENROUTER_BASE_URL')

MODEL = "deepseek/deepseek-r1-0528:free"

client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url
)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Math Expert",
        instructions="You are a math expert. You are given a question and you need to answer it.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(
        agent, # starting agent
        "what is limit in mathematics?.", # request
    )
    print(result.final_output)


asyncio.run(main())


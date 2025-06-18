import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

# Get Gemini Api Key
gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# Configure the LLM model 
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

hello_agent = Agent(
    name="Hello Agent",
    instructions="you are a hello agent, your task is to say to everyone Assalam-O-Alaiqum to the user",
    model=model
)

user_input = input("Enter Your Question: ")

agent_result = Runner.run_sync(hello_agent, user_input)

print(agent_result.final_output)
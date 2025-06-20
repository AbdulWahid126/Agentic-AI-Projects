from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import os
from dotenv import load_dotenv

load_dotenv()

# Get Gemini Api Key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# 
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Configure the LLM model 
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

# Configuration the Runconfig
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)
# Create Agent
student_agent = Agent(
    name="Smart Student Assistant",
    instructions="You are a supportive and knowledgeable Smart Student Assistant helping students learn, summarize, and stay motivated."
)

print("📘👋 Hello! I'm your **Smart Student Assistant**.")
print("1. Ask academic question")
print("2. Get study tip")
print("3. Summarize text")

user_input = input("Enter Your Question: ")

agent_result = Runner.run_sync(
    student_agent,
    user_input,
    run_config=config
)

print(agent_result.final_output)
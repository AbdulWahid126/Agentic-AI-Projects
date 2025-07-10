import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool,set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)



gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=provider,
)

# Get Career Roadmap Tool
@function_tool
def get_career_roadmap(field: str) -> str:
    """Provides a skill roadmap for a given career field."""
    if field.lower() == "ai engineer":
        return "1. Python\n2. ML\n3. Deep Learning\n4. MLOps"
    elif field.lower() == "web developer":
        return "1. HTML/CSS\n2. JavaScript\n3. React.js\n4. Next.js"
    else:
        return "No roadmap found for this career."

# 🧠 Skill Agent
skill_agent = Agent(
    name="SkillAgent",
    instructions="Provide a skill roadmap using the tool for a selected career.",
    model=model,
    tools=[get_career_roadmap]
)

# 🧑‍💼 Job Agent
job_agent = Agent(
    name="JobAgent",
    instructions="Share real-world job roles and examples for a chosen career.",
    model=model
)

# 💡 Career Agent
career_agent = Agent(
    name="CareerAgent",
    instructions=(
        "You are a career expert. Ask the student about their interests. "
        "Once the field is identified, use handoff to SkillAgent to show skills needed. "
        "Then handoff to JobAgent to suggest job roles."
    ),
    model=model,
    handoffs=[skill_agent, job_agent]
)

input_value = input("Enter your interest (e.g. AI, Medicine, Finance): ")

result = Runner.run_sync(
    career_agent,
    input_value,
)

print("Final Result:\n", result.final_output)

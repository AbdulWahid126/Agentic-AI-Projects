import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, handoff, function_tool, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=provider,
)

# Get Career Roadmap Tool
@function_tool
def get_career_roadmap(field: str) -> str:
    return {
        "ai engineer": "1. Python\n2. Machine Learning\n3. Deep Learning\n4. MLOps",
        "backend web developer": "1. Python\n2. Django\n3. Flask\n4. RESTful APIs",
        "frontend web developer": "1. HTML/CSS\n2. JavaScript\n3. React.js\n4. Next.js"
    }.get(field.lower(), "No roadmap found for this career.")

# Skill Agent
skill_agent = Agent(
    name="SkillAgent",
    instructions="Provide a skill roadmap using the tool for a selected career.",
    model=model,
    tools=[get_career_roadmap]
)

# Job Agent
job_agent = Agent(
    name="JobAgent",
    instructions="Share real-world job roles and examples for a chosen career.",
    model=model
)

# Career Agent
career_agent = Agent(
    name="CareerAgent",
    instructions=(
        "You are a career expert. Ask the student about their interests. "
        "Once the field is identified, use handoffs to SkillAgent to show skills needed. "
        "Then handoffs to JobAgent to suggest job roles."
    ),
    model=model,
    handoffs=[handoff(skill_agent), handoff(job_agent)]
)

input_value = input("Enter your interest: ")

result = Runner.run_sync(
    career_agent,
    input_value,
)

print("Final Result:\n", result.final_output)


# ----------AbdulWahid-------------

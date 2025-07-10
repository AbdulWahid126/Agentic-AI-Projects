# 💼 Career Mentor Agent

A multi-agent career guidance assistant built using the OpenAI Agent SDK and Gemini LLM (`gemini-2.0-flash`).  
It helps students explore career paths based on interests, skill roadmaps, and real-world job roles.

---

## 🧠 What It Does

The **Career Mentor Agent** guides students step-by-step using three intelligent agents:

- 🎯 **CareerAgent** — Suggests career fields based on student interests.
- 📚 **SkillAgent** — Provides a skill roadmap using the tool `get_career_roadmap()`.
- 🧳 **JobAgent** — Shares real-world job roles and examples for the chosen career.

It automatically hands off the conversation from one agent to another using the **Agent SDK's handoff mechanism**.

---

## ⚙️ Technologies Used

- **LLM**: Gemini 2.0 Flash (via free API key)
- **Framework**: OpenAI Agent SDK
- **Language**: Python 3.10+
- **Tools**: Custom Tool `get_career_roadmap()` for roadmap generation

---

## 🔁 Agent Handoff Flow

1. User expresses interest in a field.
2. `CareerAgent` recommends suitable careers.
3. Automatically **handoffs** to `SkillAgent` to generate skill roadmap.
4. Then **handoffs** to `JobAgent` to list relevant job roles.
5. Final response returned to the user.

---

## 🛠️ Project Structure


---

## 🔐 .env File

Create a `.env` file with the following content:

```env
GEMINI_API_KEY=your_gemini_api_key_here
# Install dependencies
pip install -r requirements.txt

# Run the agent
python main.py

"I'm interested in Artificial Intelligence."

Suggested Career: AI Engineer
Skill Roadmap:
1. Python
2. Machine Learning
3. Deep Learning
4. MLOps
Job Roles:
- ML Engineer at Google
- Data Scientist at Meta



---

Let me know if you'd like me to:
- Generate a GitHub-ready folder structure?
- Add badges or visuals?
- Translate this into Urdu or add comments in your Python files?

I'm here to polish it further!

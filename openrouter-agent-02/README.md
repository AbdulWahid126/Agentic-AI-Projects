# 🤖 OpenRouter Agent — OpenAI Agent SDK Powered

This is an experimental autonomous agent built using the **[OpenAI Agent SDK](https://github.com/openai/agent) + OpenRouter API**.

It connects with OpenRouter's API layer to utilize various LLMs (like GPT-4, Claude, Mistral, Gemini, etc.) via a unified interface, and follows an agentic execution loop powered by the OpenAI Agent SDK.

---

## 🚀 Features

- 🔁 Agent loop via OpenAI Agent SDK
- 🌍 Model access through OpenRouter API
- 🧠 Pluggable tools and memory
- ✅ Async, streaming, and retry support
- 🧪 Clean, modular Python structure with `uv`

---

## 📂 Folder Structure


---

## ⚙️ Setup Instructions

```bash
# Create & activate virtual env (optional but recommended)
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
uv pip install -r requirements.txt

# Set your API key in .env
OPENROUTER_API_KEY=your_api_key_here

# Run the agent
python main.py
llm:
  provider: openrouter
  model: mistral:instruct
  temperature: 0.7

agent:
  name: WebAssistantAgent
  tools:
    - name: web_search
      path: tools/search.py
  memory:
    type: vector
    path: memory/vector_store.py

---

### 📌 To Use:

1. Isko copy karke `openrouter-agent-02/README.md` file me paste karo.
2. `.env`, `main.py`, `tools`, `config.yaml` ye folders/files agar alag structure me hain to bata dena, me update kar dunga.
3. Agar tum `async` ya `agent loop` ka detailed logic dikhana chahte ho to ek section aur daal sakte hain.

Batao agar isme aur koi agent-specific detail add karni hai?

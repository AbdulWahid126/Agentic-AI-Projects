# 🧳 AI Travel Designer Agent

A multi-agent AI travel planner that designs full travel experiences based on user mood or interest, using OpenAI Agent SDK + Gemini LLM.

---

## 🌟 Features

- Suggests travel **destinations** based on user interest (e.g., beaches, food, history)
- Shows **mock flights and hotel options**
- Recommends **food and tourist attractions**
- Uses **agent-to-agent handoffs** to simulate a realistic conversation

---

## 🧠 Agents Overview

| Agent Name           | Responsibility                                      |
|----------------------|------------------------------------------------------|
| `TravelDesignerAgent` | Main coordinator agent                              |
| `DestinationAgent`   | Recommends destination based on mood                |
| `BookingAgent`       | Simulates flights and hotels using mock data        |
| `ExploreAgent`       | Suggests places to visit and food to try            |

---

## 🔧 Tools Used

| Tool Function       | Purpose                       |
|---------------------|-------------------------------|
| `get_flights()`     | Returns a mocked flight for destination |
| `suggest_hotels()`  | Returns a mocked list of hotels        |

All tools are registered using `@function_tool` from OpenAI Agent SDK.

---

## 📦 Mock Data

Sample for **Tokyo**:

- ✈️ **Flight**: Flight PK-220 | Karachi → Tokyo | Duration: 10h  
- 🏨 **Hotels**: Tokyo Garden Hotel, Sakura Inn, Capsule Heaven  
- 🍣 **Food**: Sushi, Ramen, Tempura  
- 🎡 **Attractions**: Tokyo Skytree, Shibuya Crossing, Asakusa Temple  

---

## 🔁 Handoff Flow

```text
TravelDesignerAgent
    └── handoff → DestinationAgent
        └── handoff → BookingAgent
            └── handoff → ExploreAgent

# CrewAI Trip Planner ✈️🤖

This project uses CrewAI multi-agent architecture with LLaMA-based LLM to automatically generate personalized travel plans based on user preferences.  
Multiple AI agents collaborate to select the best city, gather travel information, and create a complete itinerary with budget estimation.

---

## 🚀 Features

- Multi-Agent AI using CrewAI
- LLaMA / Local LLM support
- Automatic trip planning
- City selection based on weather, events, and cost
- Local expert recommendations
- Full travel itinerary generation
- Budget estimation
- Customizable user inputs

---

## 🧠 Agents Used

1. **City Selection Expert**
   - Chooses best city based on season, weather, and price

2. **Local Expert**
   - Finds attractions, food, events, and culture

3. **Travel Concierge**
   - Creates full travel itinerary with budget

---

## 📂 Project Structure

```
trip_planner/
│── trip_agents.py
│── trip_tasks.py
│── main.py
│── tools/
│   │── search_tool.py
│   │── browser_tool.py
│   │── calculator_tool.py
│── .env
│── pyproject.toml
│── README.md
```

---

## ⚙️ Requirements

- Python 3.10+
- CrewAI
- Ollama / LLaMA model
- Poetry
- Serper API Key
- Browserless API Key

---

## 🔑 Setup Instructions

### 1. Clone repository

```
git clone https://github.com/yourusername/crewAI-trip-planner.git
cd crewAI-trip-planner
```

### 2. Create virtual environment

```
conda create -n crewai python=3.10
conda activate crewai
```

### 3. Install requirements.txt

```
pip install requirments.txt

```

### 4. Install Ollama (for LLaMA)

```
ollama run llama3
```

### 5. Create .env file

Create `.env` and add:

```
SERPER_API_KEY=your_key
BROWSERLESS_API_KEY=your_key
MODEL=llama3
```

---

## ▶️ Run the Project

```
poetry run python main.py
```

Example inputs:

```
From: New York
Cities: London, Paris
Date: Feb 2024
Interests: AI, Food, Technology
```

---

## 📊 Output

- Selected city
- Events and attractions
- Weather info
- Budget estimation
- 7-day itinerary

---

## 💡 Example Use Case

This project shows how AI agents powered by LLaMA can collaborate to solve complex tasks such as travel planning using CrewAI.

---

## 🧑‍💻 Author

Alwin Hilton A  
M.Sc Data Science  
St. Joseph's College, Trichy  

---

## ⭐ Future Improvements

- Add UI
- Add more agents
- Add RAG
- Add hotel & flight booking API
- Support more LLM models

---

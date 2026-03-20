from crewai import Agent, LLM
from tools.browser import BrowserTools
from tools.calculator import CalculatorTools
from tools.search_tool import SearchTools


# Explicitly configure Gemini provider
from crewai import LLM
import os

"""llm = LLM(
    provider="gemini",
    model="gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

llm = LLM(
    provider="anthropic",
    model="claude-3-haiku-20240307",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)"""

llm = LLM(
    provider="ollama",
    model="ollama/llama3.1",
    base_url="http://localhost:11434"
)

class TripAgents:

    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            goal="Select the best city based on weather, season, and prices",
            backstory="Expert in analyzing travel data and destinations.",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            llm=llm,
            verbose=True,
        )

    def local_expert(self):
        return Agent(
            role="Local Expert",
            goal="Provide the best insights about the selected city",
            backstory="A knowledgeable local guide with deep city insights.",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            llm=llm,
            verbose=True,
        )

    def travel_concierge(self):
        return Agent(
            role="Travel Concierge",
            goal="Create detailed travel itineraries with budget suggestions",
            backstory="Specialist in travel planning and logistics.",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                CalculatorTools.calculate,
            ],
            llm=llm,
            verbose=True,
        )
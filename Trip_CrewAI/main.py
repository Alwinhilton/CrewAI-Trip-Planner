from dotenv import load_dotenv
from textwrap import dedent

from crewai import Crew
from trip_agents import TripAgents
from trip_tasks import TripTasks

load_dotenv()


class TripCrew:

    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        agents = TripAgents()
        tasks = TripTasks()

        city_selector = agents.city_selection_agent()
        local_expert = agents.local_expert()
        concierge = agents.travel_concierge()

        identify = tasks.identify_task(
            city_selector, self.origin, self.cities, self.interests, self.date_range
        )
        gather = tasks.gather_task(
            local_expert, self.origin, self.interests, self.date_range
        )
        plan = tasks.plan_task(
            concierge, self.origin, self.interests, self.date_range
        )

        crew = Crew(
            agents=[city_selector, local_expert, concierge],
            tasks=[identify, gather, plan],
            verbose=True,
        )

        return crew.kickoff()


if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print("--------------------------------")

    location = input("From where will you be traveling? ")
    cities = input("City options: ")
    date_range = input("Date range: ")
    interests = input("Your interests: ")

    trip = TripCrew(location, cities, date_range, interests)
    result = trip.run()

    print("\n## Your Trip Plan\n")
    print(result)
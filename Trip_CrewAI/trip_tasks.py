from crewai import Task
from textwrap import dedent


class TripTasks:

    def identify_task(self, agent, origin, cities, interests, date_range):
        return Task(
            description=dedent(f"""
                Analyze and select the best city for the trip based on:
                - Weather
                - Seasonal events
                - Travel costs

                Traveling from: {origin}
                City Options: {cities}
                Trip Date: {date_range}
                Traveler Interests: {interests}

                Provide a detailed report including:
                - Flight costs
                - Weather forecast
                - Attractions
            """),
            expected_output="Detailed report including flight costs, weather forecast, and attractions.",
            agent=agent,
        )

    def gather_task(self, agent, origin, interests, date_range):
        return Task(
            description=dedent(f"""
                Create an in-depth local city guide.

                Include:
                - Attractions
                - Hidden gems
                - Cultural insights
                - Weather
                - Approximate costs

                Trip Date: {date_range}
                Traveling from: {origin}
                Interests: {interests}
            """),
            expected_output="Comprehensive city guide with attractions, hidden gems, cultural insights, weather, and costs.",
            agent=agent,
        )

    def plan_task(self, agent, origin, interests, date_range):
        return Task(
            description=dedent(f"""
                Create a complete 7-day travel itinerary including:

                - Daily schedule
                - Hotels
                - Restaurants
                - Weather forecast
                - Budget breakdown
                - Packing suggestions

                Trip Date: {date_range}
                Origin: {origin}
                Interests: {interests}
            """),
            expected_output="Complete 7-day itinerary with daily schedule, hotels, restaurants, weather, packing list, and budget breakdown.",
            agent=agent,
        )
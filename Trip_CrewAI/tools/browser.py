import json
import os
import requests

from crewai import Agent, Task
from crewai.tools import tool
from unstructured.partition.html import partition_html


class BrowserTools:

    @tool("Scrape website content")
    def scrape_and_summarize_website(website: str) -> str:
        """Scrapes and summarizes website content."""
        url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
        payload = json.dumps({"url": website})
        headers = {
            "cache-control": "no-cache",
            "content-type": "application/json",
        }

        response = requests.post(url, headers=headers, data=payload)
        elements = partition_html(text=response.text)

        content = "\n\n".join([str(el) for el in elements])
        chunks = [content[i:i + 8000] for i in range(0, len(content), 8000)]

        summaries = []

        for chunk in chunks:
            agent = Agent(
                role="Principal Researcher",
                goal="Perform research and summarize provided content",
                backstory=(
                    "You're a Principal Researcher at a large company "
                    "responsible for summarizing complex information."
                ),
                allow_delegation=False,
            )

            task = Task(
                agent=agent,
                description=(
                    "Analyze and summarize the content below. "
                    "Return only the summary.\n\n"
                    f"{chunk}"
                ),
            )

            summaries.append(task.execute())

        return "\n\n".join(summaries)
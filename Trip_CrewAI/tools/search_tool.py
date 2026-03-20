import json
import os
import requests

from crewai.tools import tool


class SearchTools:

    @tool("Search the internet")
    def search_internet(query: str) -> str:
        """Search the internet and return top results."""
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ["SERPER_API_KEY"],
            "content-type": "application/json",
        }

        response = requests.post(url, headers=headers, data=payload)
        data = response.json()

        if "organic" not in data:
            return "Error: SERPER API issue or no results found."

        results = data["organic"][:4]
        output = []

        for result in results:
            output.append(
                "\n".join(
                    [
                        f"Title: {result.get('title')}",
                        f"Link: {result.get('link')}",
                        f"Snippet: {result.get('snippet')}",
                        "-------------------------",
                    ]
                )
            )

        return "\n".join(output)
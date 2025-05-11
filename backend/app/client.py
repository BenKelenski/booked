import requests
from requests.models import Response

from .config import settings


def get_search_books(search_query: str):
    base_url: str = "https://www.googleapis.com/books/v1"

    response: Response = requests.get(
        f"{base_url}/volumes",
        params={"q": search_query, "key": settings.GOOGLE_API_KEY},
    )

    if response.status_code == 200:
        print("Success")
        print(response.json())

        return response.json()
    return None

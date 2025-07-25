import os
import random

import requests

from src.backend.app.models import Record

DISCOGS_USER_AGENT = os.environ.get("DISCOGS_USER_AGENT")
DISCOGS_API_BASE = os.environ.get("DISCOGS_API_BASE")
DISCOGS_TOKEN = os.environ.get("DISCOGS_TOKEN")
DISCOGS_URL = os.environ.get("DISCOGS_URL")


def get_random_album(
    query=None, genre=None, style=None, country=None, year=None
):
    params = {
        "query": query,
        "genre": genre,
        "style": style,
        "country": country,
        "year": year,
        "type": "release",
        "per_page": 50,
    }
    headers = {
        "User-Agent": DISCOGS_USER_AGENT,
        "Authorization": f"Discogs token={DISCOGS_TOKEN}",
    }
    response = requests.get(
        f"{DISCOGS_API_BASE}/database/search", params=params, headers=headers
    )

    results = response.json().get("results", [])

    if not results:
        return {"error": "No albums found"}

    raw = random.choice(results)

    record = Record(
        title=raw.get("title"),
        artist=raw.get("artist"),
        year=raw.get("year"),
        genre=genre,
        cover_image=raw.get("cover_image"),
        link=DISCOGS_URL + raw.get("uri"),
    )

    return record

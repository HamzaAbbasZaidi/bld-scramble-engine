import requests
from datetime import datetime

BASE_URL = "https://www.worldcubeassociation.org"

def fetch_competitions_page(page=1, event_id=None):
    url = f"{BASE_URL}/api/v0/competition_index"
    
    params = {
        "include_cancelled": "false",
        "sort": "-end_date,-start_date,name",
        "page": page,
        "end": datetime.today().strftime("%Y-%m-%d")
    }

    if event_id:
        params["event_ids[]"] = event_id

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_recent_competitions(limit=100, event_id=None):
    page = 1
    results = []

    while len(results) < limit:
        data = fetch_competitions_page(page, event_id)

        if not data:
            break

        results.extend(data)
        page += 1

    return results[:limit]
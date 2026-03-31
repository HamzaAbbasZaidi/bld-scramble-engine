import requests

BASE_URL = "https://www.worldcubeassociation.org"


def fetch_scrambles(competition_id, event_id="333bf"):
    url = f"{BASE_URL}/api/v0/competitions/{competition_id}/scrambles/{event_id}"

    response = requests.get(url)

    if response.status_code == 404:
        print(f"No scrambles for {competition_id}")
        return None

    response.raise_for_status()

    data = response.json()

    if not data.get("rounds"):
        print(f"Empty scrambles for {competition_id}")
        return None

    return data


def extract_scramble_strings(scramble_data, include_extra=False):
    if not scramble_data:
        return []

    results = []

    for round_data in scramble_data.get("rounds", []):
        for s in round_data.get("scrambles", []):

            if not include_extra and s.get("is_extra"):
                continue

            scramble_str = s.get("scramble")

            if scramble_str:
                results.append(scramble_str)

    return results


def build_scramble_records(competition, scramble_data, include_extra=False):
    records = []

    if not scramble_data:
        return records

    comp_id = competition["id"]
    comp_name = competition["name"]

    for round_data in scramble_data.get("rounds", []):
        round_id = round_data.get("id")

        for s in round_data.get("scrambles", []):

            if not include_extra and s.get("is_extra"):
                continue

            record = {
                "competition_id": comp_id,
                "competition_name": comp_name,
                "round_id": round_id,
                "round_type": s.get("round_type_id"),
                "group_id": s.get("group_id"),
                "scramble_number": s.get("scramble_num"),
                "scramble": s.get("scramble")
            }

            records.append(record)

    return records
from ingestion.competitions import get_recent_competitions
from ingestion.scrambles import fetch_scrambles, build_scramble_records


def main():
    comps = get_recent_competitions(10, event_id="333bf")

    all_records = []

    for comp in comps:
        print(f"\n=== {comp['name']} ===")

        data = fetch_scrambles(comp["id"])

        records = build_scramble_records(comp, data)

        print(f"Collected {len(records)} scrambles")

        all_records.extend(records)

    print(f"\nTOTAL SCRAMBLES: {len(all_records)}\n")

    for r in all_records[:20]:
        print(r)


if __name__ == "__main__":
    main()
from ingestion.competitions import get_recent_competitions

def main():
    comps = get_recent_competitions(5, event_id="333bf")

    for c in comps:
        print(c["id"], "-", c["name"])

if __name__ == "__main__":
    main()
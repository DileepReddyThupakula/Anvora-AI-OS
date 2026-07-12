import json
from pathlib import Path

NEWS_FILE = Path("output/news.json")
TOPIC_FILE = Path("output/topic.json")
OUTPUT_FILE = Path("output/topic_details.json")


def main():
    news = json.loads(NEWS_FILE.read_text())
    topic = json.loads(TOPIC_FILE.read_text())

    selected = topic["title"].strip().strip('"')

    match = None

    for article in news:
        title = article.get("title", "").strip()

        if title == selected:
            match = article
            break

    if match is None:
        print("❌ Topic not found in news.")
        return

    OUTPUT_FILE.write_text(
        json.dumps(match, indent=4),
        encoding="utf-8"
    )

    print("✅ Saved:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
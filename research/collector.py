import json
from pathlib import Path

import feedparser


CONFIG_FILE = Path("config/rss_sources.json")
OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "news.json"


def load_sources():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)["sources"]


def collect_news():
    articles = []

    for source in load_sources():
        print(f"Collecting from {source['name']}...")

        feed = feedparser.parse(source["url"])

        for entry in feed.entries:
            articles.append(
                {
                    "source": source["name"],
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "published": entry.get("published", ""),
                    "summary": entry.get("summary", ""),
                }
            )

    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(articles, f, indent=2)

    print(f"\nCollected {len(articles)} articles.")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    collect_news()
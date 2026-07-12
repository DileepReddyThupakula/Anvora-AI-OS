import json
import re
from pathlib import Path

NEWS_FILE = Path("output/news.json")
TOPIC_FILE = Path("output/topic.json")
OUTPUT_FILE = Path("output/topic_details.json")


def normalize(text: str) -> str:
    """
    Normalize titles for comparison.
    """
    text = text.lower().strip()

    # Remove quotes
    text = text.replace('"', "").replace("'", "")

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Collapse multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text


def main():
    news = json.loads(NEWS_FILE.read_text(encoding="utf-8"))
    topic = json.loads(TOPIC_FILE.read_text(encoding="utf-8"))

    selected = normalize(topic["title"])

    match = None

    # 1. Exact normalized match
    for article in news:
        title = normalize(article.get("title", ""))

        if title == selected:
            match = article
            break

    # 2. Partial match fallback
    if match is None:
        for article in news:
            title = normalize(article.get("title", ""))

            if selected in title or title in selected:
                match = article
                break

    if match is None:
        print("❌ Topic not found in news.")
        return

    OUTPUT_FILE.write_text(
        json.dumps(match, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"✅ Saved: {OUTPUT_FILE}")
    print(f"📄 Matched article: {match['title']}")


if __name__ == "__main__":
    main()
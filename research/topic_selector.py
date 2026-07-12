import json
from pathlib import Path

from core.llm import ask

INPUT = Path("output/news.json")
OUTPUT = Path("output/topic.json")


def main():
    articles = json.loads(INPUT.read_text())

    titles = []

    for article in articles[:20]:
        title = article.get("title", "").strip()
        if title:
            titles.append(title)

    prompt = """Choose ONE AI news topic that has the highest YouTube potential.

Return ONLY the title.

News:
"""

    for i, title in enumerate(titles, start=1):
        prompt += f"{i}. {title}\n"

    best_title = ask(
        system="You are an experienced YouTube AI content strategist.",
        user=prompt,
        model="fast",
    ).strip()

    topic = {
        "title": best_title
    }

    OUTPUT.write_text(json.dumps(topic, indent=4))

    print("✅ Saved:", OUTPUT)
    print("🎯 Selected Topic:", best_title)


if __name__ == "__main__":
    main()
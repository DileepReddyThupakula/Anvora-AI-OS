import json
from pathlib import Path

from core.llm import ask

INPUT_FILE = Path("output/news.json")
OUTPUT_FILE = Path("output/top5.json")

SYSTEM_PROMPT = """
You are the Editor-in-Chief of an AI YouTube channel.

Given an AI news article, evaluate it and return ONLY valid JSON in this format:

{
  "viral_score": 1,
  "business_score": 1,
  "developer_score": 1,
  "evergreen_score": 1,
  "recommendation": "Long Video",
  "reason": "..."
}

Recommendations must be one of:
- Long Video
- Short
- Ignore
"""

def main():
    articles = json.loads(INPUT_FILE.read_text())

    ranked = []

    for article in articles[:10]:
        prompt = f"""
Title:
{article["title"]}

Summary:
{article["summary"]}
"""

        result = ask(SYSTEM_PROMPT, prompt)

        ranked.append({
            "title": article["title"],
            "source": article["source"],
            "analysis": result
        })

    OUTPUT_FILE.write_text(json.dumps(ranked, indent=2))

    print(f"Saved {len(ranked)} ranked stories to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
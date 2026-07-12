import json
from pathlib import Path

from core.llm import ask

TOPIC_FILE = Path("output/topic_details.json")
OUTPUT_FILE = Path("output/script.md")


def main():
    print("📝 Generating YouTube script...")

    topic = json.loads(TOPIC_FILE.read_text())

    title = topic.get("title", "")
    summary = topic.get("summary", "")
    source = topic.get("source", "")
    published = topic.get("published", "")
    link = topic.get("link", "")

    prompt = f"""
You are an expert AI technology YouTube creator.

Create an engaging YouTube script based ONLY on the information below.

==========================
ARTICLE INFORMATION
==========================

Title:
{title}

Summary:
{summary}

Source:
{source}

Published:
{published}

Reference:
{link}

==========================

Requirements:

- Length: 700-900 words
- Start with a powerful hook within the first 15 seconds.
- Explain the news in simple language.
- Explain why this announcement matters.
- Explain how it affects AI users, developers and businesses.
- Mention future implications.
- End with a strong conclusion.
- Finish with a call to subscribe.

Rules:

- Do NOT invent facts.
- If something is unknown, don't make it up.
- Stay factual while keeping the script engaging.
- Use a natural conversational YouTube style.
"""

    script = ask(
        system="""
You are one of the world's best AI YouTube script writers.

Your scripts should be:
- Professional
- Accurate
- Engaging
- Easy for beginners to understand
- Suitable for narration
""",
        user=prompt,
        model="writer",
    )

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(script, encoding="utf-8")

    print(f"✅ Script saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
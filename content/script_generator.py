import json
from pathlib import Path

from core.llm import ask

TOPIC_FILE = Path("output/topic_details.json")
OUTPUT_FILE = Path("output/script.md")


def main():
    print("📝 Generating narration script...")

    topic = json.loads(TOPIC_FILE.read_text(encoding="utf-8"))

    title = topic.get("title", "")
    summary = topic.get("summary", "")
    source = topic.get("source", "")
    published = topic.get("published", "")
    link = topic.get("link", "")

    prompt = f"""
You are an expert AI technology YouTube script writer.

Create a professional narration script using ONLY the information below.

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

- Length: 500–700 words.
- Start with a powerful hook in the first 15 seconds.
- Explain the news in simple language.
- Explain why this announcement matters.
- Explain how it affects AI users, developers, and businesses.
- Mention future implications.
- End with a memorable conclusion.
- Finish with a natural call to subscribe.

IMPORTANT RULES:

- Output ONLY the narration.
- Do NOT include scene directions.
- Do NOT include camera directions.
- Do NOT include text like:
    [Opening Scene]
    [Cut To]
    Narrator:
    Voiceover:
    Music:
    Fade In:
- Do NOT use markdown formatting.
- Do NOT invent facts.
- If information is missing, simply don't mention it.
- Write naturally as if a professional YouTube presenter is speaking directly to the audience.
"""

    script = ask(
        system="""
You are one of the world's best AI YouTube script writers.

Your narration should be:
- Natural
- Professional
- Engaging
- Factually accurate
- Easy for beginners to understand
- Ready to be converted directly into speech
""",
        user=prompt,
        model="writer",
    )

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(script.strip(), encoding="utf-8")

    print(f"✅ Script saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
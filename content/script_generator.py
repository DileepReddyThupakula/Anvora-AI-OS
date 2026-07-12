from pathlib import Path

from core.llm import ask

OUTPUT = Path("output/script.md")


def main():
    print("📝 Generating script...")

    prompt = """
Write a professional YouTube script (about 600 words) on this topic:

OpenAI releases a powerful new AI model.

Structure:
- Hook
- Introduction
- Main explanation
- Why it matters
- Conclusion
- Call to subscribe
"""

    script = ask(
        "You are an expert YouTube script writer.",
        prompt,
        model="writer"
    )

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(script, encoding="utf-8")

    print("✅ Script saved to output/script.md")


if __name__ == "__main__":
    main()
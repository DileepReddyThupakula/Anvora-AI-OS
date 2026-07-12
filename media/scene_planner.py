import json
from pathlib import Path

from core.llm import ask

SCRIPT_FILE = Path("output/script.md")
OUTPUT_FILE = Path("output/scene_plan.json")


def main():
    print("🎬 Creating scene plan...")

    script = SCRIPT_FILE.read_text(encoding="utf-8")

    prompt = f"""
You are a professional YouTube video director.

Break the following script into scenes.

For each scene provide:

- scene_number
- duration_seconds
- narration
- visual_description

Return ONLY valid JSON in this format:

[
  {{
    "scene_number": 1,
    "duration_seconds": 8,
    "narration": "...",
    "visual_description": "..."
  }}
]

SCRIPT:

{script}
"""

    result = ask(
        system="You are an expert YouTube video planner.",
        user=prompt,
        model="writer",
    )

    print("\n================ LLM OUTPUT ================\n")
    print(result)
    print("\n============================================\n")

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(result, encoding="utf-8")

    print(f"✅ Scene plan saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
import json
import math
from pathlib import Path

from core.llm import ask

SCRIPT_FILE = Path("output/script.md")
OUTPUT_FILE = Path("output/scene_plan.json")


def estimate_duration(text: str) -> int:
    words = len(text.split())
    return max(6, math.ceil(words / 2.5))


def split_into_sections(text: str):
    paragraphs = [
        p.strip()
        for p in text.split("\n\n")
        if p.strip()
    ]

    # If the model returned one giant paragraph,
    # split roughly every 120 words.
    if len(paragraphs) <= 1:
        words = text.split()
        paragraphs = []

        chunk_size = 120

        for i in range(0, len(words), chunk_size):
            paragraphs.append(" ".join(words[i:i + chunk_size]))

    return paragraphs


def main():
    print("🎬 Creating scene plan...")

    script = SCRIPT_FILE.read_text(encoding="utf-8")

    sections = split_into_sections(script)

    scenes = []

    for index, narration in enumerate(sections, start=1):

        print(f"Creating Scene {index}...")

        visual = ask(
            system="""
You are an expert AI image prompt engineer.

Create ONE image-generation prompt.

Rules:

- 25 to 40 words only.
- Ultra realistic.
- Cinematic.
- Professional lighting.
- 16:9 composition.
- Highly detailed.
- Suitable for FLUX, Stable Diffusion and Midjourney.
- No dialogue.
- No camera directions.
- No text overlays.
- Return ONLY the prompt.
""",
            user=narration,
            model="fast",
        ).strip()

        scenes.append(
            {
                "scene_number": index,
                "duration_seconds": estimate_duration(narration),
                "narration": narration,
                "visual_description": visual,
            }
        )

    OUTPUT_FILE.write_text(
        json.dumps(scenes, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"✅ Scene plan saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
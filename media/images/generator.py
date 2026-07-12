import json
from pathlib import Path

from core.llm import ask

INPUT_FILE = Path("output/scene_plan.json")
OUTPUT_FILE = Path("output/image_prompts.json")


def main():
    print("🖼️ Generating image prompts...")

    scenes = json.loads(INPUT_FILE.read_text(encoding="utf-8"))

    prompts = []

    for scene in scenes:
        narration = scene["narration"]

        image_prompt = ask(
            system="""
You are an expert cinematic AI image prompt engineer.

Create ONE highly detailed image generation prompt.

Requirements:
- Cinematic
- Ultra realistic
- Professional lighting
- 16:9
- No text
- High quality

Return ONLY the prompt.
""",
            user=narration,
            model="fast",
        ).strip()

        prompts.append(
            {
                "scene_number": scene["scene_number"],
                "prompt": image_prompt,
            }
        )

    OUTPUT_FILE.write_text(
        json.dumps(prompts, indent=4),
        encoding="utf-8",
    )

    print(f"✅ Saved {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
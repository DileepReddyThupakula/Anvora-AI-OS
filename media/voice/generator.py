from pathlib import Path

from media.voice.kokoro import generate

SCRIPT_FILE = Path("output/script.md")
OUTPUT_FILE = Path("output/narration.wav")


def main():
    print("🎤 Generating narration...")

    text = SCRIPT_FILE.read_text(encoding="utf-8")

    generate(
        text=text,
        output_path=str(OUTPUT_FILE),
    )


if __name__ == "__main__":
    main()
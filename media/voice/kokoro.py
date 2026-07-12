from pathlib import Path

import soundfile as sf
from kokoro import KPipeline


def generate(text: str, output_path: str):
    pipeline = KPipeline(lang_code="a")

    generator = pipeline(
        text,
        voice="am_adam",
    )

    audio = []

    for _, _, samples in generator:
        audio.extend(samples)

    Path(output_path).parent.mkdir(exist_ok=True)

    sf.write(output_path, audio, 24000)

    print(f"✅ Voice saved to {output_path}")
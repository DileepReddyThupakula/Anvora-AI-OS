from ollama import chat

from core.config import FAST_MODEL, WRITER_MODEL

MODELS = {
    "fast": FAST_MODEL,
    "writer": WRITER_MODEL,
}


def ask(system: str, user: str, model: str = "fast") -> str:
    response = chat(
        model=MODELS[model],
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        options={
            "temperature": 0.3,
            "num_predict": 800,
        },
    )

    return response.message.content
from ollama import chat

MODELS = {
    "fast": "llama3.2:3b",
    "writer": "qwen3:8b",
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
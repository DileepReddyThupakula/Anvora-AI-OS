from ollama import chat

DEFAULT_MODEL = "qwen3:4b"

def ask(system: str, user: str, model: str = DEFAULT_MODEL) -> str:
    """
    Send a prompt to the local Ollama model and return the response.
    """

    response = chat(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )

    return response["message"]["content"]

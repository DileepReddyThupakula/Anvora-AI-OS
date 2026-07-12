import json
from pathlib import Path

from core.llm import ask

INPUT = Path("output/news.json")

articles = json.loads(INPUT.read_text())

titles = []

for article in articles[:20]:
    title = article.get("title", "").strip()
    if title:
        titles.append(title)

prompt = "Choose the 5 best AI news topics for a YouTube channel.\n\n"

for i, title in enumerate(titles, start=1):
    prompt += f"{i}. {title}\n"

result = ask(
    "You are an AI YouTube editor. Choose the five topics most likely to attract viewers. Explain briefly why each one is worth covering.",
    prompt,
)

print(result)
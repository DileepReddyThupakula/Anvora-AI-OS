from pathlib import Path
from core.llm import ask

SYSTEM = """
You are the Research Agent for Anvora AI OS.
Your responses should be clear, factual and concise.
"""

USER = "Introduce yourself."

result = ask(SYSTEM, USER)

print(result)

Path("output").mkdir(exist_ok=True)
Path("output/research_test.md").write_text(result)

print("Saved to output/research_test.md")

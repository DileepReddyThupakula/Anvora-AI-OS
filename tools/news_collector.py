import feedparser
from pathlib import Path

FEEDS = {
    "OpenAI": "https://openai.com/news/rss.xml",
    "Hugging Face": "https://huggingface.co/blog/feed.xml",
}

Path("output").mkdir(exist_ok=True)

report = []

for source, url in FEEDS.items():
    print(f"Checking {source}...")

    feed = feedparser.parse(url)

    report.append(f"# {source}\n")

    for entry in feed.entries[:5]:
        report.append(f"- {entry.title}")
        report.append(f"  {entry.link}\n")

output = "\n".join(report)

Path("output/news_report.md").write_text(output)

print("Saved to output/news_report.md")

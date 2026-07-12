from research.collector import main as collect_news
from research.topic_selector import main as select_topics
from content.script_generator import main as generate_script


def main():
    print("=" * 50)
    print("🚀 Starting Anvora AI OS")
    print("=" * 50)

    print("\n📰 Step 1: Collecting AI news...")
    collect_news()

    print("\n🎯 Step 2: Selecting topics...")
    select_topics()

    print("\n📝 Step 3: Generating script...")
    generate_script()

    print("\n✅ Pipeline completed successfully!")


if __name__ == "__main__":
    main()
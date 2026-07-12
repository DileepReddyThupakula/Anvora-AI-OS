from research.collector import main as collect_news
from research.topic_selector import main as select_topic
from research.enricher import main as enrich_topic

from content.script_generator import main as generate_script

from media.scene_planner import main as create_scene_plan
from media.images.generator import main as generate_image_prompts
from media.voice.generator import main as generate_voice


def main():
    print("=" * 60)
    print("🚀 ANVORA AI PLATFORM")
    print("=" * 60)

    print("\n📰 Step 1/7 - Collecting AI news...")
    collect_news()

    print("\n🎯 Step 2/7 - Selecting best topic...")
    select_topic()

    print("\n📄 Step 3/7 - Enriching selected article...")
    enrich_topic()

    print("\n📝 Step 4/7 - Generating narration script...")
    generate_script()

    print("\n🎬 Step 5/7 - Creating scene plan...")
    create_scene_plan()

    print("\n🖼️ Step 6/7 - Generating image prompts...")
    generate_image_prompts()

    print("\n🎤 Step 7/7 - Generating narration...")
    generate_voice()

    print("\n" + "=" * 60)
    print("🎉 ANVORA PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print("\nGenerated files:")
    print("   ✅ output/news.json")
    print("   ✅ output/topic.json")
    print("   ✅ output/topic_details.json")
    print("   ✅ output/script.md")
    print("   ✅ output/scene_plan.json")
    print("   ✅ output/image_prompts.json")
    print("   ✅ output/narration.wav")


if __name__ == "__main__":
    main()
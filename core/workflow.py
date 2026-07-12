from typing import Callable


class Workflow:
    def __init__(self):
        self.steps = []

    def add(self, name: str, func: Callable):
        self.steps.append((name, func))

    def run(self):
        print("=" * 60)
        print("🚀 ANVORA AI PLATFORM")
        print("=" * 60)

        total = len(self.steps)

        for index, (name, func) in enumerate(self.steps, start=1):
            print(f"\n[{index}/{total}] {name}")

            try:
                func()
                print("✅ Completed")

            except Exception as e:
                print(f"❌ Failed: {e}")
                raise

        print("\n🎉 Pipeline finished successfully!")
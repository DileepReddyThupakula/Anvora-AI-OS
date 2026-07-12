from pathlib import Path

# ==========================
# Models
# ==========================

FAST_MODEL = "llama3.2:3b"
WRITER_MODEL = "qwen3:8b"
BACKUP_MODEL = "qwen3:4b"

# ==========================
# Research
# ==========================

NEWS_LIMIT = 20

# ==========================
# Script
# ==========================

SCRIPT_WORDS = 700

# ==========================
# Directories
# ==========================

ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = ROOT / "output"
KNOWLEDGE_DIR = ROOT / "knowledge"
PROMPTS_DIR = ROOT / "prompts"

OUTPUT_DIR.mkdir(exist_ok=True)
KNOWLEDGE_DIR.mkdir(exist_ok=True)
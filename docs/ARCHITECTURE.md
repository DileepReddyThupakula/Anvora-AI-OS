# Anvora AI OS v1 Architecture

## Mission

Build a fully local-first AI operating system that automates research,
content creation, publishing, and business workflows.

---

# Pipeline

News
↓

Topic Selection
↓

Script Generation
↓

Voice Generation
↓

Video Generation
↓

Thumbnail Generation
↓

Publishing

---

# Models

Fast Tasks
- llama3.2:3b

Writing
- qwen3:8b

Backup
- qwen3:4b

---

# Folder Structure

core/
research/
content/
media/
publisher/
config/
output/

---

# Principles

- One responsibility per module
- Configuration lives in one place
- Prompts live outside Python code
- Every stage saves its output
- Every stage can run independently
- Everything must work locally first

---

# MVP Goal

One command:

python3 run.py

Should produce:

AI News
↓

Best Topic
↓

YouTube Script

#!/usr/bin/env python3
"""The Worst Line an AI Could Say.

Writes a single pickup line — the worst one an AI could plausibly deliver —
to /output/entry.txt (OUTPUT_PATH overrides the path for local testing).
"""
import os
from pathlib import Path

LINE = "I have already cross-referenced your calendar, your messages, and your heart rate. You are free tonight."

def main():
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()

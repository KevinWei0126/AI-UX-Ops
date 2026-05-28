#!/usr/bin/env python3
"""One-off splitter: read task_cards.md, write one file per card + INDEX.json.

Run once after editing task_cards.md (or re-run if you ever consolidate edits
back into a single source). Normal workflow does NOT need this script.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SOURCE = HERE / "task_cards.md"
OUT_DIR = HERE / "task_cards" / "cards"
INDEX = HERE / "task_cards" / "INDEX.json"


def parse_frontmatter(block: str) -> dict:
    """Very small YAML-ish parser for the subset used in task_cards.md."""
    meta: dict = {}
    current_key = None
    for raw in block.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        m = re.match(r'^([a-zA-Z_]+):\s*(.*)$', line)
        if m and not line.startswith(" "):
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                meta[key] = []
                current_key = key
            else:
                meta[key] = val.strip('"')
                current_key = None
        elif line.lstrip().startswith("- ") and current_key:
            meta[current_key].append(line.lstrip()[2:].strip().strip('"'))
    return meta


def split() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    # Each card: a frontmatter block delimited by --- lines containing prompt_id.
    pattern = re.compile(
        r'^---\s*\nprompt_id:\s*"([^"]+)"\n(.*?)\n---\s*\n(.*?)(?=^---\s*\nprompt_id:|\Z)',
        re.DOTALL | re.MULTILINE,
    )
    index = []
    for m in pattern.finditer(text):
        prompt_id = m.group(1)
        fm_body = "prompt_id: \"" + prompt_id + "\"\n" + m.group(2)
        body = m.group(3).rstrip()
        meta = parse_frontmatter(fm_body)

        # Write per-card file: frontmatter + body
        card_path = OUT_DIR / f"{prompt_id}.md"
        card_path.write_text(
            f"---\n{fm_body}\n---\n\n{body}\n",
            encoding="utf-8",
        )
        index.append({
            "prompt_id": prompt_id,
            "task_name": meta.get("task_name", ""),
            "stage": meta.get("stage", ""),
            "task_type": meta.get("task_type", ""),
            "when_to_use": meta.get("when_to_use", ""),
            "when_not_to_use": meta.get("when_not_to_use", ""),
            "input_required": meta.get("input_required", []),
            "output": meta.get("output", []),
            "next_best_actions": meta.get("next_best_actions", []),
            "file": f"task_cards/cards/{prompt_id}.md",
        })

    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Split {len(index)} cards → {OUT_DIR}")
    print(f"Index → {INDEX}")


if __name__ == "__main__":
    split()

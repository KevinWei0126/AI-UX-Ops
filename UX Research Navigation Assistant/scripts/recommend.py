#!/usr/bin/env python3
"""Suggest a task-card combination from input materials → desired output.

Heuristic only — this is a *shortlist generator* to save context, not a
decision-maker. The Navigation Assistant is still responsible for the final
X→Y reasoning per references/workflow-reference.md §4.

Examples:
  python3 scripts/recommend.py --have 逐字稿 --want 洞察報告
  python3 scripts/recommend.py --have 研究目標 --want 訪談腳本
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "task_cards" / "INDEX.json"


# Lightweight semantic groups — extend as needed.
INPUT_ALIASES = {
    "逐字稿": ["逐字稿", "Transcript", "對話", "訪談紀錄"],
    "原話": ["User Quote", "原話", "使用者原話"],
    "研究資料": ["Research Data", "研究資料", "訪談資料"],
    "研究目標": ["研究目標", "研究方向", "研究問題"],
    "洞察": ["洞察", "Insight", "Finding", "關鍵發現"],
    "量化": ["完成率", "drop-off", "平均時間", "量化", "成效"],
}

OUTPUT_ALIASES = {
    "洞察報告": ["洞察", "關鍵發現", "報告"],
    "主題分群": ["主題", "Cluster", "Affinity"],
    "訪談腳本": ["訪談腳本", "Interview Guide", "訪談大綱"],
    "商業價值": ["商業價值", "主管", "PM"],
    "Persona": ["Persona", "人物誌"],
    "Journey Map": ["Journey", "旅程"],
}


def expand(term: str, table: dict) -> list[str]:
    for canonical, aliases in table.items():
        if term in aliases or term == canonical:
            return aliases
    return [term]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--have", action="append", default=[], help="Input material (repeatable)")
    p.add_argument("--want", action="append", default=[], help="Desired output (repeatable)")
    p.add_argument("--top", type=int, default=8)
    args = p.parse_args()

    cards = json.loads(INDEX.read_text(encoding="utf-8"))

    have_terms = [t for h in args.have for t in expand(h, INPUT_ALIASES)]
    want_terms = [t for w in args.want for t in expand(w, OUTPUT_ALIASES)]

    scored: list[tuple[int, dict]] = []
    for c in cards:
        score = 0
        input_blob = " ".join(c["input_required"]) + " " + c["when_to_use"]
        output_blob = " ".join(c["output"]) + " " + c["task_name"]
        for t in have_terms:
            if t in input_blob:
                score += 2
        for t in want_terms:
            if t in output_blob:
                score += 3
        if score > 0:
            scored.append((score, c))

    scored.sort(key=lambda x: (-x[0], x[1]["prompt_id"]))

    if not scored:
        print("(no candidate cards — try different --have/--want terms or browse list_cards.py)")
        return

    print(f"Top {min(args.top, len(scored))} candidates (heuristic shortlist; AI must still reason X→Y):\n")
    for score, c in scored[: args.top]:
        print(f"[{score:>2}] {c['prompt_id']:<12} {c['task_name']:<18} | {c['stage']}")
        print(f"     when_to_use: {c['when_to_use']}")
        if c["next_best_actions"]:
            print(f"     next: {' / '.join(c['next_best_actions'])}")
        print()


if __name__ == "__main__":
    main()

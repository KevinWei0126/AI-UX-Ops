#!/usr/bin/env python3
"""List task cards from INDEX.json, optionally filtered.

Examples:
  python3 scripts/list_cards.py                       # all 55 cards (compact)
  python3 scripts/list_cards.py --stage RP            # only stage prefix RP
  python3 scripts/list_cards.py --keyword 訪談         # text match in name/when_to_use
  python3 scripts/list_cards.py --output 洞察報告      # match desired output
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "task_cards" / "INDEX.json"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--stage", help="Stage prefix (RP/DC/AI/DO/IT/PT) or full stage name")
    p.add_argument("--keyword", help="Match against task_name + when_to_use")
    p.add_argument("--output", dest="want_output", help="Match against desired output")
    p.add_argument("--json", action="store_true", help="Emit JSON instead of table")
    args = p.parse_args()

    cards = json.loads(INDEX.read_text(encoding="utf-8"))

    def matches(c: dict) -> bool:
        if args.stage:
            s = args.stage.upper()
            if not (c["prompt_id"].startswith(s) or s in c["stage"].upper()):
                return False
        if args.keyword:
            blob = c["task_name"] + " " + c["when_to_use"]
            if args.keyword not in blob:
                return False
        if args.want_output:
            if not any(args.want_output in o for o in c["output"]):
                return False
        return True

    hits = [c for c in cards if matches(c)]

    if args.json:
        print(json.dumps(hits, ensure_ascii=False, indent=2))
        return

    if not hits:
        print("(no matches)")
        return

    for c in hits:
        print(f"{c['prompt_id']:<12} {c['task_name']:<18} | {c['stage']}")
        print(f"  when_to_use: {c['when_to_use']}")
        if c["input_required"]:
            print(f"  input:  {', '.join(c['input_required'])}")
        if c["output"]:
            print(f"  output: {', '.join(c['output'])}")
        print()


if __name__ == "__main__":
    main()

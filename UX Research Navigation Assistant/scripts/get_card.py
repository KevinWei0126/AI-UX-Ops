#!/usr/bin/env python3
"""Print one task card's full Markdown by prompt_id.

The Prompt 本文 must be vended to the designer 原樣 (unmodified). Use this
script to fetch it instead of view-ing the whole 3000+ line task_cards.md.

Examples:
  python3 scripts/get_card.py AI-A-001
  python3 scripts/get_card.py DO-A-001 --prompt-only   # only the Prompt body block
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CARDS_DIR = Path(__file__).resolve().parent.parent / "task_cards" / "cards"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("prompt_id")
    p.add_argument(
        "--prompt-only",
        action="store_true",
        help="Only print the ``` Prompt 本文 ``` block (for pasting to the designer)",
    )
    args = p.parse_args()

    path = CARDS_DIR / f"{args.prompt_id}.md"
    if not path.exists():
        print(f"Card not found: {args.prompt_id}", file=sys.stderr)
        print(f"List cards via: python3 scripts/list_cards.py", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")

    if args.prompt_only:
        m = re.search(r"## Prompt 本文\s*\n+```\s*\n(.*?)\n```", text, re.DOTALL)
        if not m:
            print("(no Prompt 本文 block found)", file=sys.stderr)
            sys.exit(2)
        print(m.group(1))
    else:
        print(text)


if __name__ == "__main__":
    main()

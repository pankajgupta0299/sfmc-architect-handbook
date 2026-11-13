#!/usr/bin/env python3
"""Synchronize the standalone Use Case Library with the canonical handbook.

Usage:
    python3 scripts/sync_use_cases.py           # update use-cases.html
    python3 scripts/sync_use_cases.py --check   # return nonzero if out of sync

The canonical content remains in index.html so existing question IDs and saved
bookmarks remain stable. This script copies only public, kind=case question
records. It does not access any private Google Drive materials.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDBOOK = ROOT / "index.html"
LIBRARY = ROOT / "use-cases.html"
HANDBOOK_PATTERN = re.compile(r"window\.HANDBOOK_QUESTIONS=(\[[\s\S]*?\]);\s*</script>")
LIBRARY_PATTERN = re.compile(r"const CASES=(\[[\s\S]*?\]);\s*const \$=")


def run(check: bool) -> int:
    master_html = HANDBOOK.read_text(encoding="utf-8")
    library_html = LIBRARY.read_text(encoding="utf-8")
    m = HANDBOOK_PATTERN.search(master_html)
    l = LIBRARY_PATTERN.search(library_html)
    if not m or not l:
        print("FAIL: Could not locate question JSON in one of the pages.")
        return 2
    questions = json.loads(m.group(1))
    cases = [q for q in questions if q.get("kind") == "case"]
    if not cases or len({q["id"] for q in cases}) != len(cases):
        print("FAIL: No cases or duplicate case IDs in handbook.")
        return 2
    current_cases = json.loads(l.group(1))
    if current_cases == cases:
        print(f"PASS: Use Case Library is in sync ({len(cases)} cases).")
        return 0
    if check:
        print(
            f"FAIL: Use Case Library out of sync: "
            f"{len(current_cases)} embedded / {len(cases)} canonical cases."
        )
        return 1
    formatted = json.dumps(cases, ensure_ascii=False, separators=(",", ":"))
    updated = library_html[:l.start(1)] + formatted + library_html[l.end(1):]
    LIBRARY.write_text(updated, encoding="utf-8")
    print(f"Updated use-cases.html with {len(cases)} cases.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check only; don't write")
    args = parser.parse_args()
    sys.exit(run(args.check))

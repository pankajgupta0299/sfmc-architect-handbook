#!/usr/bin/env python3
"""Check that interview practice remains connected to canonical handbook data.

Static checks only. Browser interaction and correctness of answers require separate review.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
PRACTICE = ROOT / "interview-practice.html"
SIBLINGS = ["index.html", "use-cases.html", "learning-path.html"]
CHAPTERS = re.compile(r"window\.HANDBOOK_CHAPTERS=(\[[\s\S]*?\]);\s*window\.HANDBOOK_QUESTIONS=")
QUESTIONS = re.compile(r"window\.HANDBOOK_QUESTIONS=(\[[\s\S]*?\]);\s*</script>")


def main() -> int:
    html = INDEX.read_text(encoding="utf-8")
    practice = PRACTICE.read_text(encoding="utf-8")
    a, b = CHAPTERS.search(html), QUESTIONS.search(html)
    if not a or not b:
        raise AssertionError("Canonical handbook data not found")
    chapters, questions = json.loads(a.group(1)), json.loads(b.group(1))
    assert chapters and questions, "Empty handbook data"
    assert "fetch('index.html'" in practice, "Practice must fetch canonical content, not ship a second copy"
    assert "q.kind!=='case'" in practice, "Practice should use interview Q&A, not the case library"
    assert "index.html#" in practice, "Missing direct links back to learning answers"
    assert "localStorage" in practice, "Local progress support missing"
    assert "self-assessment" in practice.lower(), "Avoid representing self-rating as AI assessment"
    assert "interview-practice.html" in practice, "Practice nav absent"
    for name in SIBLINGS:
        page = (ROOT / name).read_text(encoding="utf-8")
        assert 'href="interview-practice.html"' in page, f"Practice link missing from {name}"
    ids = [q["id"] for q in questions]
    assert len(ids) == len(set(ids)), "Question IDs must stay unique"
    assert set(q["chapter"] for q in questions) <= {c["id"] for c in chapters}
    pool = [q for q in questions if q.get("kind") != "case"]
    assert pool and all(q.get("ref", "").startswith("https://") for q in pool)
    print(f"PASS: interview practice wired to {len(pool)} Q&A across {len(chapters)} chapters; no copied question bank")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

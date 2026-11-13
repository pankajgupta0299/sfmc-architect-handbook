#!/usr/bin/env python3
"""Static checks for the single-file SFMC Architecture Handbook.

Usage: python3 scripts/validate_handbook.py
Checks structure, schema, IDs, chapter membership, exact duplicate questions,
reference syntax, editorial review metadata and common credential patterns.
It DOES NOT verify external URLs or factual truth.
"""
from __future__ import annotations
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "index.html"
TITLE = re.compile(r"[^a-z0-9]+")
CHAPTERS = re.compile(r"window\.HANDBOOK_CHAPTERS=(\[[\s\S]*?\]);\s*window\.HANDBOOK_QUESTIONS=")
QUESTIONS = re.compile(r"window\.HANDBOOK_QUESTIONS=(\[[\s\S]*?\]);\s*</script>")
SECRET_PATTERNS = (
    ("Private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("OAuth client secret", re.compile(r'["\']client_secret["\']\s*:\s*["\'][A-Za-z0-9_\-]{12,}["\']', re.I)),
    ("Hard-coded bearer token", re.compile(r"Bearer\s+[A-Za-z0-9_\-\.]{40,}", re.I)),
)

def main() -> int:
    errors, warnings = [], []
    if not HTML.exists():
        print("FAIL: index.html not found")
        return 1
    html = HTML.read_text(encoding="utf-8")
    m_ch, m_q = CHAPTERS.search(html), QUESTIONS.search(html)
    if not m_ch or not m_q:
        print("FAIL: embedded handbook JSON missing or malformed")
        return 1
    try:
        chapters, qs = json.loads(m_ch.group(1)), json.loads(m_q.group(1))
    except json.JSONDecodeError as exc:
        print(f"FAIL: embedded JSON is invalid: {exc}")
        return 1
    if not isinstance(chapters, list) or not isinstance(qs, list):
        errors.append("Chapters and questions must be arrays")
        return 1
    chapter_ids = [c.get("id") for c in chapters]
    ids = [q.get("id") for q in qs]
    if len(set(chapter_ids)) != len(chapter_ids):
        errors.append("Duplicate chapter ID")
    if len(set(ids)) != len(ids):
        errors.append("Duplicate question ID")
    if set(ids) & set(chapter_ids):
        warnings.append("Some chapter IDs are also question IDs")
    known_chapters = set(chapter_ids)
    titles = collections.defaultdict(list)
    url_counts = collections.Counter()
    for i, q in enumerate(qs):
        for key in ("id", "chapter", "q", "a", "ref", "level"):
            if not isinstance(q.get(key), str) or not q[key].strip():
                errors.append(f"Question {i} missing nonempty {key}")
        if q.get("chapter") not in known_chapters:
            errors.append(f"Question {q.get('id')} references missing chapter {q.get('chapter')}")
        question = q.get("q", "")
        title = TITLE.sub(" ", question.lower()).strip()
        titles[title].append(q.get("id"))
        url = q.get("ref", "")
        if not re.fullmatch(r"https://[^\s<>\"']+", url):
            errors.append(f"Question {q.get('id')} has invalid HTTPS reference format")
        else:
            url_counts[url] += 1
        if len(re.sub(r"<[^>]+>", "", q.get("a", ""))) < 140:
            warnings.append(f"Brief answer (may be intentional): {q.get('id')}")
        if re.search(r"(?:https?://)?(?:localhost|127\.0\.0\.1)(?::\d+)?", url, re.I):
            errors.append(f"Question {q.get('id')} has local-only reference")
    # Editorial metadata is optional, but when present it must be well-formed.
    checked = 0
    for q in qs:
        review = q.get("review")
        if review is None:
            continue
        if not isinstance(review, dict):
            errors.append(f"Question {q.get('id')} review metadata is not an object")
            continue
        status = review.get("status")
        if status not in {"source_checked"}:
            errors.append(f"Question {q.get('id')} has unknown review status: {status!r}")
        if not re.fullmatch(r"20\d{2}-\d{2}-\d{2}", str(review.get("date", ""))):
            errors.append(f"Question {q.get('id')} has an invalid review date")
        if not isinstance(review.get("scope"), str) or not review["scope"].strip():
            errors.append(f"Question {q.get('id')} needs a clear review scope")
        if status == "source_checked":
            checked += 1
    if checked and "Source-checked" not in html:
        warnings.append("Question review statuses exist but are not visible in website UI")
    print(f"Targeted source-checked answers: {checked} / {len(qs)}")

    for title, matches in titles.items():
        if len(matches) > 1:
            errors.append(f"Duplicate question title: {title} ({', '.join(matches)})")
    for label, pattern in SECRET_PATTERNS:
        if pattern.search(html):
            errors.append(f"Potential secret detected: {label} (review before publish)")
    if not any("HANDBOOK_QUESTIONS" in s for s in (html,)):
        errors.append("Question bank not found")
    if len(qs) < 500:
        warnings.append("Unexpectedly low question count; check whether data was removed")
    print(f"Chapters: {len(chapters)}; questions: {len(qs)}; unique reference URLs: {len(url_counts)}")
    print(f"Errors: {len(errors)}; warnings: {len(warnings)}")
    for e in errors:
        print("ERROR:", e)
    for w in warnings:
        print("WARN:", w)
    if errors:
        print("FAIL: structural audit failed")
        return 1
    print("PASS: structural checks only (links and answers NOT fact-verified)")
    return 0

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Build the quiz data (docs/questions.js) from the saved questions/Q*.md files.

Run this again every time a new question file is added or updated:

    python3 build_quiz.py

The quiz page itself is docs/index.html. Publish the docs/ folder with GitHub Pages.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUESTIONS_DIR = ROOT / "questions"
OUT_FILE = ROOT / "docs" / "questions.js"

OPTION_RE = re.compile(r"^\*\*([A-Z])\.\*\*\s*(.*)$")
FIELD_RE = re.compile(r"^\*\*(Topic|My answer|Correct answer|Result):\*\*\s*(.*)$")
TITLE_RE = re.compile(r"^#\s+([QG]\d+)\s*[:\-–]\s*(.*)$")
BREAKDOWN_HEAD_RE = re.compile(r"^(✅|❌)?\s*([A-Z])\b")
NESTED_EMPHASIS_RE = re.compile(r'\*"\*\*(.+?)\*\*"\*')
PLAIN_RE = re.compile(r"^(?:\*\*In plain words:\*\*|In (?:plain|simple) (?:terms|words):)\s*(.*)$", re.I)
WHY_LABEL_RE =re.compile(r"^\*\*Why it'?s (wrong|correct|right)\:?\*\*:?\s*$", re.I)

SECTION_KINDS = [
    ("What the Question", "asking"),
    ("Key Terms", "terms"),
    ("Real-World", "scenario"),
    ("Option-by-Option", "breakdown"),
    ("E-Commerce", "ecommerce"),
    ("Key Takeaway", "takeaways"),
]


def split_by_heading(lines, level):
    """Split lines on markdown headings of the given level, ignoring code fences."""
    prefix = "#" * level + " "
    chunks, title, buf, in_fence = [], None, [], False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith(prefix):
            if title is not None or any(l.strip() for l in buf):
                chunks.append((title, buf))
            title, buf = line[len(prefix):].strip(), []
        else:
            buf.append(line)
    chunks.append((title, buf))
    return chunks


def clean(lines):
    """Trim blank lines and horizontal rules from both ends."""
    lines = list(lines)
    while lines and lines[0].strip() in ("", "---"):
        lines.pop(0)
    while lines and lines[-1].strip() in ("", "---"):
        lines.pop()
    # marked.js misreads *"**bold quote**"*, so rewrite it as an equivalent form it handles.
    return NESTED_EMPHASIS_RE.sub(r'**_"\1"_**', "\n".join(lines))


def parse_question_block(lines):
    stem, options, current = [], [], None
    for raw in lines:
        if not raw.startswith(">"):
            continue
        line = raw[1:].lstrip(" ") if raw != ">" else ""
        m = OPTION_RE.match(line.strip())
        if m:
            current = {"letter": m.group(1), "text": m.group(2).strip()}
            options.append(current)
        elif current is not None:
            if line.strip():
                current["text"] += "\n" + line.strip()
        else:
            stem.append(line)
    return clean(stem), options


def parse_breakdown(lines):
    result = {}
    for title, body in split_by_heading(lines, 3):
        if not title:
            continue
        m = BREAKDOWN_HEAD_RE.match(title)
        if not m:
            continue
        letter = m.group(2)
        # Drop the quoted option (already shown in the quiz) and the "Why it's ..." label.
        body = [l for l in body if not l.startswith(">") and not WHY_LABEL_RE.match(l.strip())]
        result[letter] = clean(body)
    return result


def parse_plain(lines):
    """The plain-words summary: the "In plain words:" paragraph, up to the next blank line."""
    out = None
    for l in lines:
        m = PLAIN_RE.match(l.strip())
        if out is None:
            if m:
                out = [m.group(1)]
            continue
        if not l.strip():
            break
        out.append(l.rstrip())
    return "\n".join(out).strip() if out else ""


def parse_file(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    q = {"file": path.name, "sections": [], "explanations": {}}

    m = TITLE_RE.match(lines[0]) if lines else None
    q["id"] = m.group(1) if m else path.stem.split("-")[0]
    q["title"] = m.group(2).strip() if m else path.stem
    q["num"] = int(re.sub(r"\D", "", q["id"]) or 0)
    # G###: practice questions written from the official exam guide (numbered separately from Q###).
    q["guide"] = q["id"].startswith("G")

    for title, body in split_by_heading(lines, 2):
        if title is None:
            for l in body:
                f = FIELD_RE.match(l.strip())
                if f and f.group(1) == "Topic":
                    q["topic"] = f.group(2).strip()
            continue
        if "Question" in title and title.startswith("❓"):
            q["stem"], q["options"] = parse_question_block(body)
            for l in body:
                f = FIELD_RE.match(l.strip())
                if not f:
                    continue
                key, val = f.group(1), f.group(2).strip()
                if key == "My answer":
                    q["myAnswer"] = re.findall(r"\b[A-Z]\b", val)
                elif key == "Correct answer":
                    # Only read letters before any " — description" so "HTTP(S)" isn't taken as option S.
                    q["correct"] = re.findall(r"\b[A-Z]\b", re.split(r"\s+[—–-]\s+", val)[0])
            continue
        kind = next((k for needle, k in SECTION_KINDS if needle.lower() in title.lower()), "extra")
        if kind == "breakdown":
            q["explanations"] = parse_breakdown(body)
        else:
            if kind == "asking":
                q["plain"] = parse_plain(body)
            q["sections"].append({"kind": kind, "title": title, "md": clean(body)})

    problems = [k for k in ("stem", "options", "correct") if not q.get(k)]
    if problems:
        raise ValueError(f"{path.name}: could not find {', '.join(problems)}")
    q.setdefault("topic", q["title"])
    return q


def main():
    files = sorted(QUESTIONS_DIR.glob("Q[0-9]*.md")) + sorted(QUESTIONS_DIR.glob("G[0-9]*.md"))
    questions = [parse_file(p) for p in files]
    questions.sort(key=lambda q: (q["guide"], q["num"]))
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(questions, ensure_ascii=False, indent=1)
    OUT_FILE.write_text(
        "// Generated by build_quiz.py from questions/*.md. Do not edit by hand.\n"
        f"window.QUIZ_QUESTIONS = {data};\n",
        encoding="utf-8",
    )
    (OUT_FILE.parent / ".nojekyll").touch()
    for q in questions:
        missing = [o["letter"] for o in q["options"] if o["letter"] not in q["explanations"]]
        note = f"  (no explanation for {', '.join(missing)})" if missing else ""
        print(f"{q['id']}: {len(q['options'])} options, answer {'/'.join(q['correct'])}{note}")
    print(f"Wrote {len(questions)} questions to {OUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

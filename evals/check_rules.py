#!/usr/bin/env python3
"""Check problem-lens outputs against the table rules in problem-lens/SKILL.md.

Usage:
    python3 evals/check_rules.py FILE [FILE ...]

Checks structure only (rows, lens tags, families, anchor, ranking line,
decision prompt, summary length). It does not judge whether the solutions
are good. Exits 1 if any file fails a rule.

This script is a maintainer tool. It is not part of the installed Skill.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LENSES = ROOT / "problem-lens" / "references" / "lenses.md"

# Short names that may appear in Lens Tags, mapped to headings in lenses.md.
ALIASES = {
    "CPS": "Creative Problem Solving (CPS)",
    "Creative Problem Solving": "Creative Problem Solving (CPS)",
    "TRIZ": "Theory of Inventive Problem Solving (TRIZ / TIPS)",
    "TRIZ / TIPS": "Theory of Inventive Problem Solving (TRIZ / TIPS)",
    "TRIZ/TIPS": "Theory of Inventive Problem Solving (TRIZ / TIPS)",
    "RCA": "Root Cause Analysis (RCA)",
    "Root Cause Analysis": "Root Cause Analysis (RCA)",
    "Cynefin": "Cynefin Framework",
    "PDCA": "PDCA (Plan–Do–Check–Act)",
    "OODA": "OODA Loop (Observe–Orient–Decide–Act)",
    "OODA Loop": "OODA Loop (Observe–Orient–Decide–Act)",
}
SHORT = {v: k for k, v in ALIASES.items() if k in
         ("CPS", "TRIZ / TIPS", "Root Cause Analysis", "Cynefin", "PDCA", "OODA")}


def load_lenses():
    family, use_when, current, name = {}, {}, None, None
    for line in LENSES.read_text().splitlines():
        m = re.match(r"## (\w+) Lenses", line)
        if m:
            current = m.group(1)
            continue
        m = re.match(r"### (.+)", line)
        if m:
            name = m.group(1).strip()
            continue
        m = re.match(r"Use when: (.+?)\.?$", line)
        if m and name:
            family[name], use_when[name] = current, m.group(1)
    return family, use_when


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()


def sentences(text):
    text = re.sub(r"\*\*[^*]*\*\*:?", "", text)  # drop bold labels like **Summary:**
    text = re.sub(r"^Summary:?", "", text.strip())
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'`])", text.strip())
    return [p for p in parts if p.strip()]


def check(path, family, use_when):
    text = Path(path).read_text()
    lines = text.splitlines()
    fails, info = [], {}

    rows = [l for l in lines if re.match(r"\|\s*(\d|Anchor)\s*\|", l)]
    if len(rows) != 6:
        fails.append(f"expected 6 table rows, found {len(rows)}")

    primaries = []
    for r in rows:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if len(cells) < 6:
            fails.append(f"row '{cells[0]}' has {len(cells)} cells, expected 6")
            continue
        pri, tags_cell, when = cells[0], cells[2], cells[3]
        tags = [ALIASES.get(t.strip(), t.strip()) for t in re.split(r",\s*", tags_cell) if t.strip()]
        bad = [t for t in tags if t not in family]
        if bad:
            fails.append(f"row {pri}: not a lens: {', '.join(bad)}")
        if not tags or tags[0] not in family:
            continue
        p = tags[0]
        if pri == "Anchor":
            if p != "Occam's Razor":
                fails.append("anchor primary lens is not Occam's Razor")
            info["anchor_matches"] = bool(re.search(r"Matches row \d", r))
        else:
            primaries.append((pri, p))
            if p == "Occam's Razor":
                fails.append(f"row {pri}: Occam's Razor used as primary lens")
        if norm(when) != norm(use_when[p]):
            fails.append(f"row {pri}: When To Use '{when}' does not match {SHORT.get(p, p)}")

    fams = [family[p] for _, p in primaries]
    if len(primaries) == 5 and len(set(fams)) != 5:
        fails.append(f"primary families not distinct: {fams}")
    info["primaries"] = [SHORT.get(p, p) for _, p in primaries]

    if not re.search(r"Ranked by: \w", text):
        fails.append("ranking line missing")
    for opt in ("Expand a solution", "Add more solutions", "Re-rank", "Done"):
        if opt not in text:
            fails.append(f"decision prompt missing '{opt}'")

    # Summary = prose just before the table, after any Turn 1 block.
    first_row = next((i for i, l in enumerate(lines) if l.startswith("| Priority")), None)
    if first_row is not None:
        block = []
        for l in reversed(lines[:first_row]):
            if l.startswith("#") or l.strip() == "---" or l.startswith("USER REPLY"):
                break
            block.insert(0, l)
        summary = " ".join(l.strip() for l in block if l.strip())
        n = len(sentences(summary))
        info["summary_sentences"] = n
        if n > 3:
            fails.append(f"summary has {n} sentences, limit is 3")

    info["turn1_questions"] = "TURN 1 QUESTIONS" in text
    return fails, info


def main(paths):
    family, use_when = load_lenses()
    any_fail = False
    for p in paths:
        fails, info = check(p, family, use_when)
        status = "PASS" if not fails else "FAIL"
        any_fail |= bool(fails)
        print(f"{status}  {p}")
        print(f"      primaries: {', '.join(info.get('primaries', []))}")
        print(f"      summary sentences: {info.get('summary_sentences')}  "
              f"anchor 'Matches row': {info.get('anchor_matches')}  "
              f"turn-1 questions: {info.get('turn1_questions')}")
        for f in fails:
            print(f"      - {f}")
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])

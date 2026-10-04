#!/usr/bin/env python3
"""Check problem-lens outputs against the rules in problem-lens/SKILL.md (v1.1).

Usage:
    python3 evals/check_rules.py FILE [FILE ...]

Checks structure only: recommendation lines, table rows, lenses, families,
anchor, ranking line, questions, decision prompt, summary length, and links.
It does not judge whether the solutions are good. Prints a lens-rotation
summary across all files. Exits 1 if any file fails a rule.

This script is a maintainer tool. It is not part of the installed Skill.
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LENSES = ROOT / "problem-lens" / "references" / "lenses.md"

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
SHORT = {
    "Creative Problem Solving (CPS)": "CPS",
    "Theory of Inventive Problem Solving (TRIZ / TIPS)": "TRIZ / TIPS",
    "Root Cause Analysis (RCA)": "Root Cause Analysis",
    "Cynefin Framework": "Cynefin",
    "PDCA (Plan–Do–Check–Act)": "PDCA",
    "OODA Loop (Observe–Orient–Decide–Act)": "OODA",
}
PROMPT_OPTIONS = ("Expand a solution", "Add more solutions", "Re-rank", "Learn more")


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


def strip_md(s):
    return re.sub(r"[*`_]", "", s)


def sentences(text):
    text = re.sub(r"\*\*[^*]*\*\*:?", "", text)
    text = re.sub(r"^\s*Summary[.:]?", "", text.strip())
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'`])", text.strip())
    return [p for p in parts if p.strip()]


def check(path, family, use_when):
    text = Path(path).read_text()
    plain = strip_md(text)
    lines = text.splitlines()
    fails, info = [], {"primaries": [], "anchor": None}

    # Recommendation lines
    do_first = re.search(r"Do this first:\s*(Row\s*(\d)|Anchor)", plain)
    if not do_first:
        fails.append("missing 'Do this first: Row N' line")
    elif do_first.group(2) and not 1 <= int(do_first.group(2)) <= 5:
        fails.append(f"'Do this first' points to row {do_first.group(2)}")
    if not re.search(r"Switch to (Row\s*\d|Anchor|the Anchor)\b.*\bif\b", plain, re.I):
        fails.append("missing 'Switch to Row M if' line")
    info["do_first"] = do_first.group(1) if do_first else None

    # Table
    header = next((l for l in lines if l.startswith("| Priority")), "")
    if "Why This Lens" not in header:
        fails.append("table header missing 'Why This Lens' column")
    rows = [l for l in lines if re.match(r"\|\s*(\d|Anchor)\s*\|", l)]
    if len(rows) != 6:
        fails.append(f"expected 6 table rows, found {len(rows)}")

    for r in rows:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if len(cells) < 6:
            fails.append(f"row '{cells[0]}' has {len(cells)} cells, expected 6")
            continue
        pri, lens_cell, why = cells[0], strip_md(cells[2]), strip_md(cells[3])
        tags = [ALIASES.get(t.strip(), t.strip()) for t in re.split(r",\s*", lens_cell) if t.strip()]
        if len(tags) > 2:
            fails.append(f"row {pri}: more than two lenses")
        bad = [t for t in tags if t not in family]
        if bad:
            fails.append(f"row {pri}: not a lens: {', '.join(bad)}")
        if not tags or tags[0] not in family:
            continue
        p = tags[0]
        if pri == "Anchor":
            info["anchor"] = p
            if p != "Occam's Razor":
                fails.append("anchor primary lens is not Occam's Razor")
            if re.search(r"Matches row", r, re.I):
                fails.append("anchor repeats a row ('Matches row')")
        else:
            info["primaries"].append(p)
            if p == "Occam's Razor":
                fails.append(f"row {pri}: Occam's Razor used as primary lens")
        if not why:
            fails.append(f"row {pri}: 'Why This Lens' is empty")
        elif norm(why) == norm(use_when[p]):
            fails.append(f"row {pri}: 'Why This Lens' copies the generic trigger")

    fams = [family[p] for p in info["primaries"]]
    if len(info["primaries"]) == 5 and len(set(fams)) != 5:
        fails.append(f"primary families not distinct: {fams}")

    # Ranking line and decision prompt
    if not re.search(r"Ranked by: \w", plain):
        fails.append("ranking line missing")
    for opt in PROMPT_OPTIONS:
        if opt not in plain:
            fails.append(f"decision prompt missing '{opt}'")

    # Answer first: nothing should ask before the recommendation
    if "TURN 1 QUESTIONS" in text:
        fails.append("asked questions before answering")
    rec_pos = plain.find("Do this first")
    if rec_pos > 0 and "?" in plain[:rec_pos]:
        fails.append("question asked before the recommendation")

    # Questions that would change the pick: at most three
    q_head = re.search(r"Questions That Would Change the Pick", plain, re.I)
    if q_head:
        tail = plain[q_head.end():]
        stop = min([i for i in (tail.find(o) for o in PROMPT_OPTIONS) if i >= 0] or [len(tail)])
        qs = [l for l in tail[:stop].splitlines() if re.match(r"\s*(\d+\.|[-*])\s", l) and "?" in l]
        info["questions"] = len(qs)
        if len(qs) > 3:
            fails.append(f"{len(qs)} questions, limit is 3")
    else:
        info["questions"] = 0

    # Summary: prose before the recommendation line
    if rec_pos > 0:
        block = [l for l in plain[:rec_pos].splitlines()
                 if l.strip() and not l.startswith("#") and l.strip() != "---"
                 and not re.match(r"\s*(Recommendation|Summary)[.:]?\s*$", l.strip())]
        summary = " ".join(block)
        n = len(sentences(summary))
        info["summary_sentences"] = n
        if n > 3:
            fails.append(f"summary has {n} sentences, limit is 3")

    # No links in a first answer
    if re.search(r"https?://", text):
        fails.append("contains a link (links belong only in Learn more)")

    return fails, info


def main(paths):
    family, use_when = load_lenses()
    used = Counter()
    any_fail = False
    for p in paths:
        fails, info = check(p, family, use_when)
        any_fail |= bool(fails)
        used.update(info["primaries"])
        print(f"{'PASS' if not fails else 'FAIL'}  {p}")
        print(f"      do first: {info.get('do_first')}  primaries: "
              f"{', '.join(SHORT.get(x, x) for x in info['primaries'])}")
        print(f"      summary sentences: {info.get('summary_sentences')}  questions: {info.get('questions')}")
        for f in fails:
            print(f"      - {f}")
    primary_ok = [n for n in family if n != "Occam's Razor"]
    print("\nLENS ROTATION across these files (primary lens, rows 1-5):")
    for n in primary_ok:
        print(f"  {SHORT.get(n, n):<28} {used.get(n, 0)}")
    print(f"  distinct primaries: {sum(1 for n in primary_ok if used.get(n))} of {len(primary_ok)}")
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])

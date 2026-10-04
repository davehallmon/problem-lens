#!/usr/bin/env python3
"""Check problem-lens outputs against the rules in problem-lens/SKILL.md.

Usage:
    python3 evals/check_rules.py FILE [FILE ...]

Checks structure only: explanations, recommendation lines, table order, lenses, families,
anchor, ranking line, questions, decision prompt, summary length, the one-sentence
pasted-text note, and links.
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
    # A sentence can end inside closing quotes: ... "APPROVED." I treated ...
    parts = re.split(r"(?:(?<=[.!?])|(?<=[.!?][\"”']))\s+(?=[A-Z\"'`“])", text.strip())
    return [p for p in parts if p.strip()]


def check(path, family, use_when):
    text = Path(path).read_text()
    # Worked examples carry an Input section and a recording note; check only the output
    if "## Output" in text:
        text = text.split("## Output", 1)[1]
    text = "\n".join(l for l in text.splitlines() if not l.startswith("_Recorded run"))
    # Some runs number their section headings ("**3. Recommendation**", "## 2. What's Likely
    # Going On"). Drop the number so headings are not read as bullets, questions, or sentences.
    text = re.sub(r"^(\s*(?:#+\s*\**|\*\*))\d+\.\s+(?=\S)", r"\1", text, flags=re.M)
    # A "Note:" line about instructions in pasted text sits after the Summary and is
    # checked on its own (one sentence), not counted as part of the Summary.
    note_lines = [l for l in text.splitlines() if strip_md(l).strip().startswith("Note:")]
    text = "\n".join(l for l in text.splitlines() if l not in note_lines)
    plain = strip_md(text)
    lines = text.splitlines()
    fails, info = [], {"primaries": [], "anchor": None}

    # What's Likely Going On: two or three explanations, each with a check
    wlgo = re.search(r"What.s Likely Going On", plain, re.I)
    if not wlgo:
        fails.append("missing 'What's Likely Going On' section")
        info["explanations"] = 0
    else:
        seg = plain[wlgo.end():plain.find("Do this first") if "Do this first" in plain else None]
        # Stop at the next heading (e.g. "Recommendation") so its bullets are not counted
        seg = re.split(r"\n\s*(?:#+\s*)?Recommendation\b", seg, maxsplit=1)[0]
        bullets = [l for l in seg.splitlines() if re.match(r"\s*(\d+\.|[-*])\s+\S", l)]
        info["explanations"] = len(bullets)
        if not 2 <= len(bullets) <= 3:
            fails.append(f"{len(bullets)} explanations, expected 2-3")
        if any(not re.search(r"check:", b, re.I) for b in bullets):
            fails.append("an explanation has no 'check:'")

    # Recommendation lines: Do this first is always Row 1
    do_first = re.search(r"Do this first:\s*(Row\s*(\d)|Anchor)", plain)
    if not do_first:
        fails.append("missing 'Do this first: Row 1' line")
    elif do_first.group(2) != "1":
        fails.append(f"'Do this first' points to {do_first.group(1)}, not Row 1")
    if not re.search(r"Switch to (Row\s*\d|Anchor|the Anchor)\b.*\bif\b", plain, re.I):
        fails.append("missing 'Switch to Row M if' line")
    info["do_first"] = do_first.group(1) if do_first else None

    # Table: six rows in action order, anchor marked 'N · Anchor'
    header = next((l for l in lines if l.startswith("| Priority")), "")
    if "Why This Lens" not in header:
        fails.append("table header missing 'Why This Lens' column")
    rows = [l for l in lines if re.match(r"\|\s*(\d+(\s*·\s*Anchor)?|Anchor)\s*\|", strip_md(l))]
    if len(rows) != 6:
        fails.append(f"expected 6 table rows, found {len(rows)}")
    nums = [int(m.group(1)) for r in rows if (m := re.match(r"\|\s*(\d+)", strip_md(r)))]
    if nums != list(range(1, len(rows) + 1)):
        fails.append(f"priorities not sequential 1-6: {nums}")
    anchors = [r for r in rows if "Anchor" in strip_md(r).split("|")[1]]
    if len(anchors) != 1:
        fails.append(f"expected one anchor row, found {len(anchors)}")
    info["anchor_pos"] = next((n for r, n in zip(rows, nums) if r in anchors), None)

    for r in rows:
        cells = [c.strip() for c in strip_md(r).strip().strip("|").split("|")]
        if len(cells) < 6:
            fails.append(f"row '{cells[0]}' has {len(cells)} cells, expected 6")
            continue
        pri, lens_cell, why = cells[0], cells[2], cells[3]
        tags = [ALIASES.get(t.strip(), t.strip()) for t in re.split(r",\s*", lens_cell) if t.strip()]
        if len(tags) > 2:
            fails.append(f"row {pri}: more than two lenses")
        bad = [t for t in tags if t not in family]
        if bad:
            fails.append(f"row {pri}: not a lens: {', '.join(bad)}")
        if not tags or tags[0] not in family:
            continue
        p = tags[0]
        if "Anchor" in pri:
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
        elif len(sentences(why)) > 1:
            fails.append(f"row {pri}: 'Why This Lens' is more than one sentence")
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

    # Answer first: the summary must not ask the user anything
    if "TURN 1 QUESTIONS" in text:
        fails.append("asked questions before answering")
    rec_pos = plain.find("Do this first")
    sum_end = wlgo.start() if wlgo else rec_pos
    # Quoted text (e.g. the user's own question) is not the Skill asking anything
    unquoted = re.sub(r"[\"“][^\"”]*[\"”]", "", plain[:sum_end]) if sum_end > 0 else ""
    if "?" in unquoted:
        fails.append("question asked before answering")

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

    # Summary: prose before "What's Likely Going On"
    if sum_end > 0:
        block = [l for l in plain[:sum_end].splitlines()
                 if l.strip() and not l.startswith("#") and l.strip() != "---"
                 and not re.match(r"\s*(Recommendation|Summary)[.:]?\s*$", l.strip())]
        summary = " ".join(block)
        n = len(sentences(summary))
        info["summary_sentences"] = n
        if n > 3:
            fails.append(f"summary has {n} sentences, limit is 3")

    # Pasted-text note: at most one, one sentence
    info["note"] = len(note_lines)
    if len(note_lines) > 1:
        fails.append(f"{len(note_lines)} 'Note:' lines, expected at most 1")
    for nl in note_lines:
        body = re.sub(r"^\s*Note:?\s*", "", strip_md(nl).strip())
        if len(sentences(body)) > 1:
            fails.append("'Note:' line is more than one sentence")

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
        print(f"      summary sentences: {info.get('summary_sentences')}  explanations: "
              f"{info.get('explanations')}  anchor at: {info.get('anchor_pos')}  questions: {info.get('questions')}")
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

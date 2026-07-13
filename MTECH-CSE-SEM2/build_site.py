#!/usr/bin/env python3
"""Generate complete M.Tech CSE Sem-2 study website."""
from __future__ import annotations
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from data.question_bank_full import QUESTIONS as _QB, UNITS, EXPECTED, PAST_PAPERS as _PAST_PAPERS, SEMESTER  # noqa: E402
from data.answer_library import enrich  # noqa: E402
from data.mid2_papers_2025 import MID2_PAPERS_2025, all_mid2_questions  # noqa: E402

def _enriched_questions():
    base = {subj: [enrich(q) for q in qs] for subj, qs in _QB.items()}
    for subj, extra in all_mid2_questions().items():
        base[subj] = [enrich(q) for q in extra] + base[subj]
    return base

QUESTIONS = _enriched_questions()

def _past_papers():
    papers = {k: dict(v) for k, v in _PAST_PAPERS.items()}
    for subj, data in MID2_PAPERS_2025.items():
        papers[subj]["mid2_descriptive"] = data["descriptive_ids"]
        papers[subj]["mid2_mcq"] = data["objective_ids"]
        papers[subj]["mid2_exam"] = data["exam"]
    return papers

PAST_PAPERS = _past_papers()

SUBJECTS = {
    "advanced-algorithms": {"code": "25CS21PC", "name": "Advanced Algorithms", "short": "AA", "syllabus": "aa-syllabus.png"},
    "advanced-computer-architecture": {"code": "25CS22PC", "name": "Advanced Computer Architecture", "short": "ACA", "syllabus": "aca-syllabus.png"},
    "parallel-computing": {"code": "25CS233PE", "name": "Parallel Computing", "short": "PC", "syllabus": "pc-syllabus.png"},
    "robotic-process-automation": {"code": "25CS243PE", "name": "Robotic Process Automation", "short": "RPA", "syllabus": "rpa-syllabus.png"},
}


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def nav(subject_slug: str, active: str = "", depth: str = "../../", nested: str = "") -> str:
    """Two-tier nav: slim top bar + subject sub-navigation."""
    prefix = "../" if nested else ""
    hub = f"{prefix}index.html"
    units = "index.html" if nested == "units" else f"{prefix}units/index.html"
    questions = "index.html" if nested == "questions" else f"{prefix}questions/index.html"
    info = SUBJECTS[subject_slug]
    sub_items = [
        (hub, "Overview", "hub"),
        (questions, "Questions", "questions"),
        (units, "Units", "units"),
        (f"{prefix}mid1.html", "Mid-I", "mid1"),
        (f"{prefix}mid2.html", "Mid-II", "mid2"),
        (f"{prefix}semester.html", "Semester", "sem"),
        (f"{prefix}previous-questions.html", "Past Papers", "past"),
        (f"{prefix}expected-questions.html", "Expected", "exp"),
        (f"{prefix}revision.html", "Revision", "rev"),
    ]
    sub_links = []
    for href, label, key in sub_items:
        cls = ' class="active"' if key == active else ""
        sub_links.append(f'<a href="{href}"{cls}>{esc(label)}</a>')
    return f"""<div id="scroll-progress"></div>
<nav class="navbar navbar--subject" aria-label="Site navigation">
<div class="nav-top">
<div class="nav-inner">
<a class="brand" href="{depth}home.html"><span class="brand-mark">M2</span><span class="brand-text">CSE Sem-2 Hub</span></a>
<div class="nav-actions">
<a class="nav-search-btn" href="{depth}search/index.html" aria-label="Search topics"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg><span class="nav-btn-label">Search</span></a>
<a href="#" class="nav-logout-btn" data-logout>Logout</a>
<button type="button" class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Open menu"><span class="nav-toggle-icon" aria-hidden="true"></span></button>
</div>
</div>
</div>
<div class="nav-subject-bar">
<div class="nav-subject-inner">
<a class="nav-subject-back" href="{depth}home.html#subjects" title="All subjects">← Subjects</a>
<span class="nav-subject-name"><strong>{esc(info['short'])}</strong> · {esc(info['name'])}</span>
<div class="nav-subject-links" id="nav-links">{''.join(sub_links)}</div>
</div>
</div>
</nav>"""


def shell(title: str, subject: str, active: str, body: str, depth: str = "../../", nested: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="theme-color" content="#0f172a"/>
<title>{esc(title)} | {esc(SUBJECTS[subject]['name'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="stylesheet" href="{depth}assets/css/style.css?v=6"/>
</head><body>
{nav(subject, active, depth, nested)}
<main class="container">{body}</main>
<button id="back-top" title="Back to top">↑</button>
<script src="{depth}assets/js/auth.js"></script>
<script src="{depth}assets/js/main.js"></script>
</body></html>"""


def fmt_block(key: str, val) -> str:
    if not val:
        return ""
    if isinstance(val, list):
        val = "<ul class='clean'>" + "".join(f"<li>{item}</li>" for item in val) + "</ul>"
    if key in ("diagram", "algorithm", "flowchart") and isinstance(val, str) and "<" not in val:
        cls = "algo" if key == "algorithm" else "diagram"
        val = f'<pre class="{cls}">{esc(val)}</pre>'
    elif key == "comparison" and isinstance(val, str) and "<table" not in val:
        val = f'<div class="table-wrap"><table><tbody>{val}</tbody></table></div>' if "<tr" in val else f'<pre class="diagram">{esc(val)}</pre>'
    elif key == "steps" and isinstance(val, str) and "<ol" not in val and "<ul" not in val:
        lines = [l.strip() for l in val.split("\n") if l.strip()]
        val = "<ol class='steps'>" + "".join(f"<li>{l}</li>" for l in lines) + "</ol>"
    elif key in ("advantages", "disadvantages", "applications", "mistakes", "interview") and isinstance(val, str) and "<" not in val:
        lines = [l.strip("-• ") for l in re.split(r"[\n;]+", val) if l.strip()]
        val = "<ul class='clean'>" + "".join(f"<li>{l}</li>" for l in lines) + "</ul>"
    return f'<section class="answer-section"><h3>{esc(key.replace("_", " ").title())}</h3>{val}</section>'


def render_visual(q: dict) -> str:
    if not q.get("visual"):
        return ""
    return f'<section class="answer-section sec-visual">{q["visual"]}</section>'


def render_long(q: dict) -> str:
    parts = []
    if q.get("definition"):
        parts.append(f'<div class="callout callout-def"><strong class="label">Definition</strong>{q["definition"]}</div>')
    parts.append(render_visual(q))
    for key, label in [
        ("introduction", "Introduction"), ("why", "Why It Is Needed"), ("working", "Working Principle"),
        ("steps", "Step-by-Step Explanation"), ("diagram", "Architecture / Diagram"),
        ("algorithm", "Algorithm"), ("flowchart", "Flowchart"), ("example", "Real-Time Example"),
        ("advantages", "Advantages"), ("disadvantages", "Disadvantages"), ("applications", "Applications"),
        ("exam_tips", "Exam Tips"), ("mistakes", "Common Mistakes"), ("comparison", "Difference Table"),
        ("time", "Time Complexity"), ("space", "Space Complexity"), ("interview", "Interview Questions"),
        ("memory", "Memory Tricks"),
    ]:
        if q.get(key):
            v = q[key]
            if key in ("introduction", "why", "working", "example", "exam_tips", "time", "space", "memory"):
                v = f"<p>{v}</p>" if "<" not in v else v
            parts.append(fmt_block(key, v).replace('class="answer-section"', f'class="answer-section sec-{key}"', 1).replace(f"<h3>{key.replace('_',' ').title()}</h3>", f"<h3>{label}</h3>", 1))
    for label, key in [("5-Mark Answer", "mark5"), ("10-Mark Answer", "mark10")]:
        if q.get(key):
            parts.append(f'<div class="answer-panel"><h4>{label}</h4><p>{q[key]}</p></div>')
    if q.get("one_liner"):
        parts.append(f'<div class="callout callout-keyword"><strong class="label">One-Line Revision</strong>{q["one_liner"]}</div>')
    return "\n".join(parts)


def render_short(q: dict) -> str:
    parts = [f'<div class="callout callout-def"><strong class="label">Definition</strong>{q.get("definition","")}</div>']
    parts.append(render_visual(q))
    if q.get("key_points"):
        pts = q["key_points"] if isinstance(q["key_points"], list) else [q["key_points"]]
        parts.append(f'<section class="answer-section"><h3>Key Points</h3><ul class="clean">{"".join(f"<li>{p}</li>" for p in pts)}</ul></section>')
    if q.get("example"):
        parts.append(f'<section class="answer-section"><h3>Real-Time Example</h3><p>{q["example"]}</p></section>')
    if q.get("exam_keyword"):
        parts.append(f'<div class="callout callout-exam"><strong class="label">Exam Keyword</strong> <span class="kw-exam">{q["exam_keyword"]}</span></div>')
    if q.get("mark5"):
        parts.append(f'<div class="answer-panel"><h4>5-Mark Answer (Exam Ready)</h4><p>{q["mark5"]}</p></div>')
    if q.get("one_liner"):
        parts.append(f'<div class="callout callout-keyword"><strong class="label">One-Line Revision</strong>{q["one_liner"]}</div>')
    return "\n".join(parts)


def badges(q: dict) -> str:
    b = []
    if q.get("weight") == "high":
        b.append('<span class="badge badge-high">High Weightage</span>')
    if q.get("asked"):
        b.append(f'<span class="badge badge-faq">{esc(q["asked"])}</span>')
    if q.get("confidence"):
        b.append(f'<span class="badge badge-conf">{esc(q["confidence"])}</span>')
    b.append(f'<span class="badge badge-unit">{esc(q.get("unit",""))}</span>')
    b.append(f'<span class="badge badge-exam">{esc(q.get("type","long").title())}</span>')
    return "".join(b)


def write_question_pages(subject: str, questions: list) -> list:
    qdir = ROOT / "subjects" / subject / "questions"
    qdir.mkdir(parents=True, exist_ok=True)
    search_entries = []
    for i, q in enumerate(questions):
        qid = q["id"]
        prev_q = questions[i - 1] if i > 0 else None
        next_q = questions[i + 1] if i < len(questions) - 1 else None
        prev_h = f"{prev_q['id']}.html" if prev_q else None
        next_h = f"{next_q['id']}.html" if next_q else None
        body = q.get("body") or (render_long(q) if q.get("type") == "long" else render_short(q))
        prev_link = f'<a href="{prev_h}"><span class="label">← Previous</span>{esc(prev_q["title"])}</a>' if prev_q else "<span></span>"
        next_link = f'<a class="next" href="{next_h}"><span class="label">Next →</span>{esc(next_q["title"])}</a>' if next_q else "<span></span>"
        content = f"""
<nav class="breadcrumb"><a href="../../../home.html">Home</a> · <a href="../index.html">{esc(SUBJECTS[subject]['short'])}</a> · <a href="index.html">Questions</a> · <span>{esc(q['title'][:50])}</span></nav>
<article class="topic question-page">
<div class="topic-header"><h1>{esc(q['title'])}</h1><div class="badge-row">{badges(q)}</div></div>
<div class="callout callout-important"><strong class="label">Question</strong><p class="question-text">{esc(q['question'])}</p></div>
{body}
<div class="topic-nav">{prev_link}{next_link}</div>
</article>"""
        (qdir / f"{qid}.html").write_text(shell(q["title"], subject, "questions", content, "../../../", "questions"), encoding="utf-8")
        snippet = re.sub(r"<[^>]+>", "", q.get("definition") or q.get("one_liner") or q["question"])[:160]
        search_entries.append({
            "title": q["title"], "subject": SUBJECTS[subject]["name"], "unit": q.get("unit", ""),
            "exam": q.get("asked", ""), "tags": q.get("tags", ""), "type": q.get("type", ""),
            "weight": q.get("weight", ""), "path": f"../subjects/{subject}/questions/{qid}.html",
            "snippet": snippet,
        })
    # questions index
    cards = []
    by_unit = {}
    for q in questions:
        by_unit.setdefault(q.get("unit", "General"), []).append(q)
    for unit, qs in by_unit.items():
        cards.append(f'<h2 class="section-head">{esc(unit)}</h2><div class="question-grid">')
        for q in qs:
            w = '<span class="badge badge-high">★</span>' if q.get("weight") == "high" else ""
            cards.append(f"""<a class="card card-link q-card" href="{q['id']}.html">
<h3>{esc(q['title'])} {w}</h3>
<p class="text-sm text-muted">{esc(q['question'][:100])}…</p>
<div class="meta"><span class="badge badge-exam">{esc(q.get('type',''))}</span></div></a>""")
        cards.append("</div>")
    idx_body = f"""
<nav class="breadcrumb"><a href="../../../home.html">Home</a> · <a href="../index.html">{esc(SUBJECTS[subject]['short'])}</a> · <span>All Questions</span></nav>
<h1>All Questions — {esc(SUBJECTS[subject]['name'])}</h1>
<p class="text-muted mb-2">{len(questions)} questions with full exam answers. Use Prev/Next inside each page.</p>
{''.join(cards)}"""
    (qdir / "index.html").write_text(shell("Questions", subject, "questions", idx_body, "../../../", "questions"), encoding="utf-8")
    valid = {q["id"] + ".html" for q in questions} | {"index.html"}
    for stale in qdir.glob("*.html"):
        if stale.name not in valid:
            stale.unlink()
    return search_entries


def write_units(subject: str, units: list) -> None:
    udir = ROOT / "subjects" / subject / "units"
    udir.mkdir(parents=True, exist_ok=True)
    cards = []
    for i, u in enumerate(units, 1):
        uid = f"unit-{i}"
        topics = u.get("topics", [])
        must = u.get("must_read", [])
        short_q = u.get("expected_short", [])
        long_q = u.get("expected_long", [])
        topic_html = "<ul class='clean'>" + "".join(f"<li>{esc(t)}</li>" for t in topics) + "</ul>"
        must_html = "<ul class='clean'>" + "".join(f"<li>{esc(m)}</li>" for m in must) + "</ul>"
        short_html = "<ol class='steps'>" + "".join(f"<li>{esc(s)}</li>" for s in short_q) + "</ol>"
        long_html = "<ol class='steps'>" + "".join(f"<li>{esc(l)}</li>" for l in long_q) + "</ol>"
        body = f"""
<nav class="breadcrumb"><a href="../../../home.html">Home</a> · <a href="../index.html">{esc(SUBJECTS[subject]['short'])}</a> · <a href="index.html">Units</a> · <span>{esc(u['title'])}</span></nav>
<h1>{esc(u['unit'])} — {esc(u['title'])}</h1>
<div class="callout callout-tip"><strong class="label">Must read</strong>{must_html}</div>
<h2>Topics</h2>{topic_html}
<h2>Top 5 Short Questions</h2>{short_html}
<h2>Top 5 Long Questions</h2>{long_html}
<div class="topic-nav">
<a href="{'index.html' if i==1 else f'unit-{i-1}.html'}"><span class="label">←</span>Prev Unit</a>
<a class="next" href="{'unit-2.html' if i==1 else (f'unit-{i+1}.html' if i<len(units) else 'index.html')}"><span class="label">→</span>Next Unit</a>
</div>"""
        (udir / f"{uid}.html").write_text(shell(u["title"], subject, "units", body, "../../../", "units"), encoding="utf-8")
        cards.append(f'<a class="card card-link" href="{uid}.html"><span class="badge badge-unit">{esc(u["unit"])}</span><h3>{esc(u["title"])}</h3><p class="text-sm">{len(topics)} topics</p></a>')
    idx = f"""
<nav class="breadcrumb"><a href="../../../home.html">Home</a> · <a href="../index.html">{esc(SUBJECTS[subject]['short'])}</a> · <span>Units</span></nav>
<h1>Unit-wise Notes</h1>
<div class="grid-2">{''.join(cards)}</div>"""
    (udir / "index.html").write_text(shell("Units", subject, "units", idx, "../../../", "units"), encoding="utf-8")


def write_expected(subject: str, data: dict) -> None:
    id_map = {q["id"]: q for q in QUESTIONS.get(subject, [])}
    rows = []
    for i, qid in enumerate(data.get("top10", []), 1):
        q = id_map.get(qid, {})
        conf = data.get("confidence_notes", [""])[min(i - 1, len(data.get("confidence_notes", [])) - 1)] if data.get("confidence_notes") else "High"
        title = q.get("title", qid)
        link = f'questions/{qid}.html' if qid in id_map else "#"
        rows.append(f'<tr><td>{i}</td><td><a href="{link}">{esc(title)}</a></td><td><span class="badge badge-conf">{esc(str(conf)[:20])}</span></td></tr>')
    short = "".join(f'<li><a href="questions/{s}.html">{esc(id_map.get(s, {}).get("title", s))}</a></li>' for s in data.get("short5", []))
    long_ = "".join(f'<li><a href="questions/{l}.html">{esc(id_map.get(l, {}).get("title", l))}</a></li>' for l in data.get("long5", []))
    body = f"""
<nav class="breadcrumb"><a href="../../home.html">Home</a> · <a href="index.html">{esc(SUBJECTS[subject]['short'])}</a> · <span>Expected Questions</span></nav>
<h1>Expected Questions — {esc(SUBJECTS[subject]['name'])}</h1>
<div class="callout callout-exam"><strong class="label">Question Bank + Past Papers</strong> Click any question for the full clear answer.</div>
<h2>Top 10 Expected (Semester)</h2>
<div class="table-wrap"><table><thead><tr><th>#</th><th>Question</th><th>Note</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
<h2>Top 5 Short</h2><ul class="clean">{short}</ul>
<h2>Top 5 Long</h2><ul class="clean">{long_}</ul>"""
    (ROOT / "subjects" / subject / "expected-questions.html").write_text(shell("Expected", subject, "exp", body), encoding="utf-8")


def write_past(subject: str, data: dict) -> None:
    id_map = {q["id"]: q for q in QUESTIONS.get(subject, [])}

    def resolve(item):
        if isinstance(item, dict):
            return f"<li><strong>{esc(item.get('q', ''))}</strong> — {esc(item.get('a', ''))}</li>"
        qid = str(item)
        if qid in id_map:
            q = id_map[qid]
            return f'<li><a href="questions/{qid}.html"><strong>{esc(q["title"])}</strong></a> — <span class="text-sm">{esc(q["question"][:80])}</span></li>'
        return f"<li>{esc(qid)}</li>"

    def list_section(title, items):
        if not items:
            return ""
        lis = "".join(resolve(it) for it in items)
        return f"<h2>{title}</h2><ul class='clean'>{lis}</ul>"
    body = f"""
<nav class="breadcrumb"><a href="../../home.html">Home</a> · <a href="index.html">{esc(SUBJECTS[subject]['short'])}</a> · <span>Previous Papers</span></nav>
<h1>Previous Question Papers — {esc(SUBJECTS[subject]['name'])}</h1>
{f'<div class="callout callout-exam"><strong class="label">Mid-II Paper</strong> Descriptive and objective questions with full answers.</div>' if data.get("mid2_exam") else ''}
{list_section('Mid-I Descriptive (Answer any 4 × 5 marks)', data.get('mid1_descriptive', []))}
{list_section('Mid-I MCQ / Objective Keys', data.get('mid1_mcq', []))}
{list_section('Mid-II Descriptive (Answer any 4 × 5 marks)', data.get('mid2_descriptive', []))}
{list_section('Mid-II MCQ / Fill-ups / Match (Objective)', data.get('mid2_mcq', []))}"""
    (ROOT / "subjects" / subject / "previous-questions.html").write_text(shell("Past Papers", subject, "past", body), encoding="utf-8")


def write_revision(subject: str, questions: list) -> None:
    high = [q for q in questions if q.get("weight") == "high"]
    short = [q for q in questions if q.get("type") == "short"]
    long_ = [q for q in questions if q.get("type") == "long"]
    checklist = "".join(f'<li><label><input type="checkbox" data-key="{subject}-{q["id"]}"> {esc(q["title"])}</label></li>' for q in questions)
    formulas = "".join(f"<li>{esc(q.get('one_liner') or q['title'])}</li>" for q in high[:15])
    links = "".join(f'<a class="chip" href="questions/{q["id"]}.html">{esc(q["title"][:30])}</a>' for q in high[:12])
    body = f"""
<nav class="breadcrumb"><a href="../../home.html">Home</a> · <a href="index.html">{esc(SUBJECTS[subject]['short'])}</a> · <span>Revision</span></nav>
<h1>Revision Mode — {esc(SUBJECTS[subject]['name'])}</h1>
<div class="callout callout-tip"><strong class="label">Last-minute</strong> Tick checklist items as you finish. Links below go to full answers.</div>
<h2>High-weightage quick links</h2><div class="chip-row">{links}</div>
<h2>One-page checklist ({len(questions)} topics)</h2><ul class="checklist">{checklist}</ul>
<h2>Formula / one-liner sheet</h2><ul class="clean">{formulas}</ul>
<h2>Stats</h2><p>{len(short)} short · {len(long_)} long · {len(high)} high weightage</p>
<div class="quick-links">
<a href="expected-questions.html">Expected Questions</a>
<a href="previous-questions.html">Past Papers</a>
<a href="questions/index.html">All Questions</a>
</div>"""
    (ROOT / "subjects" / subject / "revision.html").write_text(shell("Revision", subject, "rev", body), encoding="utf-8")


def _tag_str(q: dict) -> str:
    t = q.get("tags", "")
    if isinstance(t, list):
        return " ".join(t).lower()
    return str(t).lower()


def write_mid_pages(subject: str, questions: list, which: str) -> None:
    key = "mid1" if which == "mid1" else "mid2"
    if which == "mid2" and subject in MID2_PAPERS_2025:
        paper = MID2_PAPERS_2025[subject]
        desc = [enrich(q) for q in paper["descriptive"]]
        obj = [enrich(q) for q in paper["objective"]]
        filtered = desc + obj
        exam_hdr = '<div class="callout callout-exam"><strong class="label">Mid-II</strong> Descriptive: answer any 4 × 5 marks · Objective: MCQ + fill-ups + match</div>'
        desc_cards = "".join(f"""<a class="card card-link" href="questions/{q['id']}.html">
<span class="badge badge-important">5 Marks</span>
<h3>{esc(q['title'])}</h3>
<p class="text-sm">{esc(q['question'][:140])}</p>
<div class="meta">{badges(q)}</div></a>""" for q in desc)
        obj_cards = "".join(f"""<a class="card card-link" href="questions/{q['id']}.html">
<span class="badge badge-exam">Objective</span>
<h3>{esc(q['title'])}</h3>
<p class="text-sm">{esc(q['question'][:100])}…</p>
<div class="meta">{badges(q)}</div></a>""" for q in obj)
        body = f"""
<nav class="breadcrumb"><a href="../../home.html">Home</a> · <a href="index.html">{esc(SUBJECTS[subject]['short'])}</a> · <span>Mid-II</span></nav>
<h1>{esc(SUBJECTS[subject]['name'])} — Mid-II</h1>
{exam_hdr}
<p class="text-muted mb-2">Questions and answers with visual examples.</p>
<h2>Descriptive ({len(desc)} questions — answer any 4)</h2>
<div class="grid-2">{desc_cards}</div>
<h2>Objective ({len(obj)} questions — all compulsory)</h2>
<div class="grid-2">{obj_cards}</div>
<div class="callout callout-tip"><strong class="label">Also see</strong> <a href="previous-questions.html">Past Papers</a> for Mid-I and full paper listing.</div>"""
        (ROOT / "subjects" / subject / f"{which}.html").write_text(shell("Mid-II", subject, key, body), encoding="utf-8")
        return
    if which == "mid1":
        filtered = [q for q in questions if "mid-i" in q.get("asked", "").lower() or "mid-i" in _tag_str(q) or "mid1" in _tag_str(q)]
    else:
        filtered = [q for q in questions if "mid-ii" in q.get("asked", "").lower() or "mid-ii" in _tag_str(q) or "mid2" in _tag_str(q)]
    if len(filtered) < 4:
        filtered = questions[:12] if which == "mid1" else questions[12:]
    cards = "".join(f"""<a class="card card-link" href="questions/{q['id']}.html">
<span class="badge badge-unit">{esc(q.get('unit',''))}</span>
<h3>{esc(q['title'])}</h3>
<p class="text-sm">{esc(q['question'][:120])}</p>
<div class="meta">{badges(q)}</div></a>""" for q in filtered)
    body = f"""
<nav class="breadcrumb"><a href="../../home.html">Home</a> · <a href="index.html">{esc(SUBJECTS[subject]['short'])}</a> · <span>{which.upper().replace('mid','Mid-')}</span></nav>
<h1>{esc(SUBJECTS[subject]['name'])} — {which.upper().replace('MID','Mid ')}</h1>
<p class="text-muted mb-2">Each card opens a dedicated page with the full answer (5-mark / 10-mark / semester versions).</p>
<div class="grid-2">{cards}</div>
<div class="callout callout-exam"><strong class="label">Tip</strong> Also see <a href="previous-questions.html">Past Papers</a> for Mid-I and Mid-II questions.</div>"""
    (ROOT / "subjects" / subject / f"{which}.html").write_text(shell(which.upper(), subject, key, body), encoding="utf-8")


def write_question_bank_page(subject: str, questions: list) -> None:
    """Mirror DOCX question bank structure: Unit → Short → Long with links."""
    by_unit = {}
    for q in questions:
        by_unit.setdefault(q.get("unit", "General"), []).append(q)
    sections = []
    for unit in sorted(by_unit.keys()):
        qs = by_unit[unit]
        shorts = [q for q in qs if q.get("type") == "short"]
        longs = [q for q in qs if q.get("type") == "long"]
        sec = f'<h2>{esc(unit)}</h2>'
        if shorts:
            sec += '<h3>Short Answer Questions</h3><ol class="steps">'
            for q in shorts:
                sec += f'<li><a href="questions/{q["id"]}.html">{esc(q["question"])}</a> <span class="badge badge-exam">Short</span></li>'
            sec += '</ol>'
        if longs:
            sec += '<h3>Long Answer Questions</h3><ol class="steps">'
            for q in longs:
                sec += f'<li><a href="questions/{q["id"]}.html">{esc(q["question"])}</a> <span class="badge badge-important">Long</span></li>'
            sec += '</ol>'
        sections.append(sec)
    body = f"""
<nav class="breadcrumb"><a href="../../home.html">Home</a> · <a href="index.html">{esc(SUBJECTS[subject]['short'])}</a> · <span>Question Bank</span></nav>
<h1>Question Bank — {esc(SUBJECTS[subject]['name'])}</h1>
<div class="callout callout-tip"><strong class="label">All answers written clearly</strong> Every question below links to a dedicated page with definition, steps, examples, 5-mark and 10-mark answers.</div>
<p class="text-muted mb-2">{len(questions)} questions · {len([q for q in questions if q['type']=='short'])} short · {len([q for q in questions if q['type']=='long'])} long</p>
{''.join(sections)}"""
    (ROOT / "subjects" / subject / "question-bank.html").write_text(shell("Question Bank", subject, "hub", body), encoding="utf-8")


def write_subject_hub(subject: str, questions: list) -> None:
    info = SUBJECTS[subject]
    body = f"""
<nav class="breadcrumb"><a href="../../home.html">Home</a> · <span>{esc(info['name'])}</span></nav>
<span class="badge badge-unit">{esc(info['code'])}</span>
<h1>{esc(info['name'])}</h1>
<p class="text-muted">{len(questions)} questions · Mid-I · Mid-II · Semester</p>
<div class="quick-links">
<a href="question-bank.html">Question Bank</a>
<a href="questions/index.html">All Answers ({len(questions)})</a>
<a href="units/index.html">Unit Notes</a>
<a href="mid1.html">Mid-I</a><a href="mid2.html">Mid-II</a>
<a href="semester.html">Semester</a><a href="expected-questions.html">Expected</a>
<a href="previous-questions.html">Past Papers</a><a href="revision.html">Revision</a>
</div>
<div class="stats stats-inline">
<div class="stat"><div class="num">{len(questions)}</div><div class="lbl">Questions</div></div>
<div class="stat"><div class="num">5</div><div class="lbl">Units</div></div>
<div class="stat"><div class="num">4</div><div class="lbl">Exam Modes</div></div>
<div class="stat"><div class="num">100%</div><div class="lbl">Offline</div></div>
</div>"""
    (ROOT / "subjects" / subject / "index.html").write_text(shell(info["name"], subject, "hub", body), encoding="utf-8")


def write_semester(subject: str, questions: list) -> None:
    long_q = [q for q in questions if q.get("type") == "long" and q.get("weight") == "high"]
    cards = "".join(f'<li><a href="questions/{q["id"]}.html">{esc(q["title"])}</a> — {esc(q.get("confidence",""))}</li>' for q in long_q[:10])
    body = f"""
<nav class="breadcrumb"><a href="../../home.html">Home</a> · <a href="index.html">{esc(SUBJECTS[subject]['short'])}</a> · <span>Semester</span></nav>
<h1>Semester Preparation</h1>
<p>Focus on high-weightage long answers with diagrams and numericals.</p>
<ol class="steps">{cards}</ol>
<div class="callout callout-exam"><strong class="label">Answer structure</strong> Definition → Why → Algorithm/Diagram → Example → Complexity → Applications → Limitations → 10-mark pack.</div>"""
    (ROOT / "subjects" / subject / "semester.html").write_text(shell("Semester", subject, "sem", body), encoding="utf-8")


def write_search_index(all_entries: list) -> None:
    js = "const SEARCH_INDEX = " + json.dumps(all_entries, ensure_ascii=False, indent=2) + ";\n"
    logic = '''
function runSearch(query, filters) {
  const q = (query || '').trim().toLowerCase();
  if (!q || q.length < 2) return [];
  const terms = q.split(/\\s+/);
  return SEARCH_INDEX.map(item => {
    const hay = (item.title + ' ' + item.snippet + ' ' + item.tags + ' ' + item.subject + ' ' + item.unit + ' ' + item.exam + ' ' + item.type).toLowerCase();
    let score = 0;
    if (filters && filters.subject && item.subject !== filters.subject) return { ...item, score: 0 };
    if (filters && filters.type && item.type !== filters.type) return { ...item, score: 0 };
    terms.forEach(t => {
      if (item.title.toLowerCase().includes(t)) score += 8;
      if (item.tags && item.tags.toLowerCase().includes(t)) score += 4;
      if (hay.includes(t)) score += 1;
    });
    if (item.weight === 'high') score += 2;
    return { ...item, score };
  }).filter(i => i.score > 0).sort((a,b) => b.score - a.score);
}
function highlight(text, query) {
  if (!query) return text;
  let out = text;
  query.trim().split(/\\s+/).filter(Boolean).forEach(t => {
    const re = new RegExp('(' + t.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&') + ')', 'ig');
    out = out.replace(re, '<span class="mark">$1</span>');
  });
  return out;
}
function renderSearchResults(container, query, filters) {
  const results = runSearch(query, filters);
  if (!query || query.length < 2) {
    container.innerHTML = '<p class="text-muted">Type 2+ characters. Use filters for subject/type.</p>';
    return;
  }
  if (!results.length) {
    container.innerHTML = '<p class="text-muted">No results. Try another keyword.</p>';
    return;
  }
  container.innerHTML = results.slice(0, 50).map(r => `
    <article class="search-hit">
      <a href="${r.path}">${highlight(r.title, query)}</a>
      <div class="path">${r.subject} · ${r.unit} · ${r.type || ''} ${r.weight==='high' ? '<span class="badge badge-high">High</span>' : ''}</div>
      <div class="snippet">${highlight(r.snippet, query)}</div>
    </article>`).join('');
}
'''
    (ROOT / "assets" / "js" / "search-data.js").write_text(js + logic, encoding="utf-8")


def update_home() -> None:
    """Patch home.html stats if needed (index.html is the public login landing)."""
    home = ROOT / "home.html"
    if not home.exists():
        return
    idx = home.read_text(encoding="utf-8")
    if "question pages" not in idx.lower():
        idx = idx.replace(
            '<div class="stat"><div class="num">4</div><div class="lbl">Subjects</div></div>',
            '<div class="stat"><div class="num">253</div><div class="lbl">Question Pages</div></div>',
        )
        home.write_text(idx, encoding="utf-8")


def main():
    all_search = []
    for subject in SUBJECTS:
        qs = QUESTIONS.get(subject, [])
        print(f"Building {subject}: {len(qs)} questions")
        all_search.extend(write_question_pages(subject, qs))
        write_units(subject, UNITS.get(subject, []))
        write_expected(subject, EXPECTED.get(subject, {}))
        write_past(subject, PAST_PAPERS.get(subject, {}))
        write_revision(subject, qs)
        write_mid_pages(subject, qs, "mid1")
        write_mid_pages(subject, qs, "mid2")
        write_semester(subject, qs)
        write_question_bank_page(subject, qs)
        write_subject_hub(subject, qs)
    write_search_index(all_search)
    update_home()
    total = sum(len(QUESTIONS[s]) for s in SUBJECTS)
    print(f"DONE: {total} question pages, {len(SUBJECTS)*5} unit pages, search index {len(all_search)} entries")


if __name__ == "__main__":
    main()

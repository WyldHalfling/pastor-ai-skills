#!/usr/bin/env python3
"""Board / Elder Report PDF Generator.

Desk document. Internal governance, distributed to the board only.
"""

import json
import sys
import os

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, "..", "..", "shared"))

from pdf_utils import (
    SLATE,
    build_styles, section_header, add_section, add_title_banner, add_table,
    add_bullet_list, add_shaded_box, make_page_footer, create_doc,
    write_markdown, merge, load_profile,
)
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle


def build_report_styles(base):
    s = dict(base)
    s["cut_note"] = ParagraphStyle(
        "CutNote", fontName="Helvetica", fontSize=9, leading=13,
        textColor=SLATE, spaceAfter=4,
    )
    return s


def add_metrics(story, metrics, styles):
    section_header(story, "THE NUMBERS", styles)
    rows = [[
        m.get("label", ""),
        m.get("current", ""),
        m.get("prior", ""),
        m.get("interpretation", ""),
    ] for m in metrics]
    add_table(story, ["Metric", "Now", "Prior", "What it means"],
              rows, [1.7, 0.7, 0.7, 3.4], styles)


def add_decisions(story, decisions, styles):
    section_header(story, "DECISIONS NEEDED", styles)
    for i, d in enumerate(decisions, 1):
        story.append(Paragraph(f"{i}. {d.get('question', '')}", styles["body_bold"]))
        if d.get("background"):
            story.append(Paragraph(d["background"], styles["body_content"]))

        for opt in d.get("options", []):
            story.append(Paragraph(
                f"<b>{opt.get('option', '')}</b>: {opt.get('tradeoff', '')}",
                styles["bullet"], bulletText="•"))

        elements = []
        if d.get("recommendation"):
            elements.append(Paragraph("Recommendation", styles["body_label"]))
            elements.append(Paragraph(d["recommendation"], styles["body_content"]))
        if d.get("rationale"):
            elements.append(Paragraph(d["rationale"], styles["prompt"]))
        if d.get("if_deferred"):
            elements.append(Paragraph(
                f"<b>If deferred:</b> {d['if_deferred']}", styles["prompt"]))
        if elements:
            add_shaded_box(story, elements, styles)
        story.append(Spacer(1, 14))


def add_risks(story, risks, styles):
    section_header(story, "RISK AND WATCH ITEMS", styles)
    rows = [[r.get("item", ""), r.get("detail", ""), r.get("watching", "")] for r in risks]
    add_table(story, ["Item", "Detail", "What we are doing"], rows, [1.7, 2.7, 2.1], styles)


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    profile = load_profile()
    data = merge(data, profile)

    if not output_path:
        period = data.get("period", "report").replace("/", "-").replace(" ", "-")
        output_path = f"Board-Report-{period}.pdf"

    doc = create_doc(
        output_path,
        title=f"Board Report: {data.get('period', '')}",
        author=data.get("pastor_name", ""),
    )
    styles = build_report_styles(build_styles())
    story = []

    meta = [p for p in [
        f"Meeting: {data['meeting_date']}" if data.get("meeting_date") else None,
        data.get("pastor_name"),
    ] if p]
    add_title_banner(
        story,
        "BOARD REPORT",
        data.get("period", ""),
        meta,
        styles,
    )

    # Decisions first, deliberately. Buried decision items get five minutes at 9:15pm.
    if data.get("decisions"):
        add_decisions(story, data["decisions"], styles)

    if data.get("metrics"):
        add_metrics(story, data["metrics"], styles)

    if data.get("narrative"):
        add_section(story, "WHAT IS ACTUALLY HAPPENING", data["narrative"], styles)

    if data.get("risks"):
        add_risks(story, data["risks"], styles)

    if data.get("prayer"):
        section_header(story, "PRAYER", styles)
        add_bullet_list(story, data["prayer"], styles)

    if data.get("action_items"):
        section_header(story, "ACTION ITEMS", styles)
        rows = [[a.get("action", ""), a.get("owner", ""), a.get("deadline", "")]
                for a in data["action_items"]]
        add_table(story, ["Action", "Owner", "By"], rows, [3.5, 1.7, 1.3], styles)

    if data.get("operational_cut"):
        section_header(story, "HELD BACK AS OPERATIONAL", styles)
        story.append(Paragraph(
            "Reported to staff, not to the board. Listed so nothing looks hidden.",
            styles["cut_note"]))
        add_bullet_list(story, data["operational_cut"], styles)

    page_footer = make_page_footer("church", profile)
    doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)
    write_markdown(doc.filename, data.get("markdown"))
    return os.path.abspath(doc.filename)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate-pdf.py <input.json> [output.pdf]")
        sys.exit(1)
    result = generate_pdf(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print(f"PDF generated: {result}")

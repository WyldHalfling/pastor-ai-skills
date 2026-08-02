#!/usr/bin/env python3
"""Wedding Ceremony Plan PDF Generator.

Desk document. Holds premarital notes and family dynamics, so it carries no
letterhead and is not the printed guest program.
"""

import json
import sys
import os

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, "..", "..", "shared"))

from pdf_utils import (
    SLATE, GOLD,
    build_styles, section_header, add_section, add_title_banner, add_table,
    add_bullet_list, add_shaded_box, make_page_footer, create_doc,
    write_markdown, merge, load_profile,
)
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle


def build_wedding_styles(base):
    s = dict(base)
    s["confidential"] = ParagraphStyle(
        "Confidential", fontName="Helvetica-Bold", fontSize=9, leading=13,
        textColor=SLATE, spaceAfter=4,
    )
    s["register"] = ParagraphStyle(
        "Register", fontName="Helvetica-Bold", fontSize=9, leading=13,
        textColor=GOLD, spaceAfter=2,
    )
    return s


def add_premarital(story, sessions, styles):
    section_header(story, "PREMARITAL SESSIONS", styles)
    for s in sessions:
        story.append(Paragraph(
            f"Session {s.get('session', '')}: {s.get('topic', '')}", styles["body_bold"]))
        for q in s.get("questions", []):
            story.append(Paragraph(q, styles["bullet"], bulletText="•"))
        if s.get("listening_for"):
            story.append(Paragraph(
                f"<b>Listening for:</b> {s['listening_for']}", styles["prompt"]))
        for w in s.get("warning_signs", []):
            story.append(Paragraph(f"<b>Warning sign:</b> {w}", styles["prompt"]))
        story.append(Spacer(1, 10))


def add_ceremony_order(story, order, styles):
    section_header(story, "CEREMONY ORDER", styles)
    rows = []
    for item in order:
        element = item.get("element", "")
        if item.get("pastor_speaks"):
            element += "  [YOUR WORDS]"
        rows.append([
            element,
            str(item.get("minutes", "")),
            item.get("who", ""),
            "Core" if item.get("essential") else "Cuttable",
        ])
    add_table(story, ["Element", "Min", "Who", "If short"], rows, [3.1, 0.6, 1.5, 1.0], styles)
    story.append(Paragraph(
        "Slots marked [YOUR WORDS] are deliberately empty. The charge is yours.",
        styles["prompt"]))
    story.append(Spacer(1, 8))


def add_liturgy(story, options, styles):
    section_header(story, "LITURGY AND VOW OPTIONS", styles)
    current = None
    for opt in options:
        element = opt.get("element", "")
        if element != current:
            current = element
            story.append(Paragraph(element, styles["body_bold"]))
        if opt.get("register"):
            story.append(Paragraph(opt["register"], styles["register"]))
        add_shaded_box(story, [Paragraph(opt.get("text", ""), styles["body_content"])], styles)
        story.append(Spacer(1, 10))


def add_scripture_options(story, options, styles):
    section_header(story, "SCRIPTURE OPTIONS", styles)
    for opt in options:
        ref = opt.get("reference", "")
        if opt.get("translation"):
            ref += f" ({opt['translation']})"
        story.append(Paragraph(ref, styles["body_bold"]))
        if opt.get("does"):
            story.append(Paragraph(opt["does"], styles["body_content"]))
        if opt.get("note"):
            story.append(Paragraph(opt["note"], styles["prompt"]))
        story.append(Spacer(1, 6))


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    profile = load_profile()
    data = merge(data, profile)

    if not output_path:
        initials = data.get("couple_initials", "couple").replace(".", "").replace(" ", "")
        date = data.get("date", "").replace("/", "-").replace(" ", "-").replace(",", "")
        output_path = f"Wedding-Plan-{initials}-{date}.pdf"

    doc = create_doc(
        output_path,
        title="Wedding Ceremony Plan",
        author=data.get("pastor_name", ""),
    )
    styles = build_wedding_styles(build_styles())
    story = []

    meta = [p for p in [data.get("setting"), data.get("pastor_name")] if p]
    add_title_banner(
        story,
        "WEDDING CEREMONY",
        f"{data.get('couple_initials', '')}  |  {data.get('date', '')}".strip(" |"),
        meta,
        styles,
    )

    story.append(Paragraph(
        "PASTOR'S PLANNING DOCUMENT. Not the printed guest program.",
        styles["confidential"]))
    story.append(Spacer(1, 10))

    if data.get("situation_read"):
        add_section(story, "READING THE SITUATION", data["situation_read"], styles)

    if data.get("premarital_sessions"):
        add_premarital(story, data["premarital_sessions"], styles)

    if data.get("ceremony_order"):
        add_ceremony_order(story, data["ceremony_order"], styles)

    if data.get("liturgy_options"):
        add_liturgy(story, data["liturgy_options"], styles)

    if data.get("scripture_options"):
        add_scripture_options(story, data["scripture_options"], styles)

    if data.get("logistics"):
        section_header(story, "LOGISTICS", styles)
        add_bullet_list(story, data["logistics"], styles)

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

#!/usr/bin/env python3
"""Funeral / Memorial Service Plan PDF Generator.

Desk document. This holds family landmines and message framing, so it carries no
letterhead and must never be mistaken for a handout.
"""

import json
import sys
import os

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, "..", "..", "shared"))

from pdf_utils import (
    NAVY, GOLD, SLATE,
    build_styles, section_header, add_section, add_title_banner, add_table,
    add_bullet_list, add_shaded_box, make_page_footer, create_doc,
    write_markdown, merge, load_profile,
)
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle


def build_funeral_styles(base):
    s = dict(base)
    s["confidential"] = ParagraphStyle(
        "Confidential", fontName="Helvetica-Bold", fontSize=9, leading=13,
        textColor=SLATE, spaceAfter=4,
    )
    s["slot"] = ParagraphStyle(
        "Slot", fontName="Helvetica-Bold", fontSize=10.5, leading=15,
        textColor=GOLD, spaceAfter=2,
    )
    return s


def add_family_questions(story, questions, styles):
    section_header(story, "QUESTIONS FOR THE FAMILY", styles)
    current_group = None
    for q in questions:
        group = q.get("group", "")
        if group and group != current_group:
            current_group = group
            story.append(Paragraph(group, styles["body_label"]))
        story.append(Paragraph(q.get("question", ""), styles["bullet"], bulletText="•"))
        if q.get("note"):
            story.append(Paragraph(f"<i>{q['note']}</i>", styles["prompt"]))
    story.append(Spacer(1, 8))


def add_order_of_service(story, order, styles):
    section_header(story, "ORDER OF SERVICE", styles)
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
        "Slots marked [YOUR WORDS] are deliberately empty. Those are yours.",
        styles["prompt"]))
    story.append(Spacer(1, 8))


def add_scripture_options(story, options, styles):
    section_header(story, "SCRIPTURE OPTIONS", styles)
    for opt in options:
        ref = opt.get("reference", "")
        if opt.get("translation"):
            ref += f" ({opt['translation']})"
        story.append(Paragraph(ref, styles["body_bold"]))
        if opt.get("does"):
            story.append(Paragraph(opt["does"], styles["body_content"]))
        if opt.get("avoid_when"):
            story.append(Paragraph(
                f"<b>Wrong choice when:</b> {opt['avoid_when']}", styles["prompt"]))
        story.append(Spacer(1, 6))


def add_message_framing(story, framing, styles):
    section_header(story, "MESSAGE FRAMING", styles)
    elements = []
    if framing.get("one_thing"):
        elements.append(Paragraph("What this service needs to say", styles["body_label"]))
        elements.append(Paragraph(framing["one_thing"], styles["body_content"]))
    if framing.get("anchors"):
        elements.append(Paragraph("Theological anchors", styles["body_label"]))
        for a in framing["anchors"]:
            elements.append(Paragraph(a, styles["bullet"], bulletText="•"))
    if framing.get("avoid"):
        elements.append(Paragraph("Do not say", styles["body_label"]))
        for a in framing["avoid"]:
            elements.append(Paragraph(a, styles["bullet"], bulletText="•"))
    if framing.get("length"):
        elements.append(Paragraph(f"<b>Length:</b> {framing['length']}", styles["prompt"]))
    add_shaded_box(story, elements, styles)
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "This is framing, not a message. The words are yours and the Spirit's.",
        styles["prompt"]))


def add_followup(story, followups, styles):
    section_header(story, "FOLLOW-UP", styles)
    rows = [[f.get("when", ""), f.get("date", ""), f.get("note", "")] for f in followups]
    add_table(story, ["When", "Date", "Note"], rows, [1.4, 1.6, 3.2], styles)
    story.append(Paragraph(
        "This section matters more than the service. Put these on the calendar now.",
        styles["prompt"]))


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    profile = load_profile()
    data = merge(data, profile)

    if not output_path:
        initials = data.get("deceased_initials", "service").replace(".", "").replace(" ", "")
        date = data.get("date", "").replace("/", "-").replace(" ", "-").replace(",", "")
        output_path = f"Funeral-Plan-{initials}-{date}.pdf"

    doc = create_doc(
        output_path,
        title=f"{data.get('service_type', 'Service')} Plan",
        author=data.get("pastor_name", ""),
    )
    styles = build_funeral_styles(build_styles())
    story = []

    meta = [p for p in [data.get("date"), data.get("pastor_name")] if p]
    add_title_banner(
        story,
        data.get("service_type", "MEMORIAL SERVICE").upper(),
        f"For {data.get('deceased_initials', '')}".strip(),
        meta,
        styles,
    )

    story.append(Paragraph(
        "PASTOR'S PLANNING DOCUMENT. Not for distribution to the family or attendees.",
        styles["confidential"]))
    story.append(Spacer(1, 10))

    if data.get("situation_read"):
        add_section(story, "READING THE SITUATION", data["situation_read"], styles)

    if data.get("family_questions"):
        add_family_questions(story, data["family_questions"], styles)

    if data.get("order_of_service"):
        add_order_of_service(story, data["order_of_service"], styles)

    if data.get("scripture_options"):
        add_scripture_options(story, data["scripture_options"], styles)

    if data.get("message_framing"):
        add_message_framing(story, data["message_framing"], styles)

    if data.get("logistics"):
        section_header(story, "LOGISTICS", styles)
        add_bullet_list(story, data["logistics"], styles)

    if data.get("followup_dates"):
        add_followup(story, data["followup_dates"], styles)

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

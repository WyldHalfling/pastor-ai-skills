# Skill Standards

> **AUTHORITATIVE** for how a skill is written, how it sounds, and how it outputs.
> For what a skill is *allowed* to do, see `project-guidelines.md`.

---

## Anatomy of a Skill

```
<category>/<skill-name>/
├── SKILL.md            # required: frontmatter + workflow
├── generate-pdf.py     # optional: only if the output is a document
└── references/         # optional: lookup tables the skill reads on demand
```

Categories: `foundation/`, `sermon-prep/`, `pastoral-care/`, `teaching/`,
`leadership/`, `personal/`, `written-communication/`, `sermon-repurposing/`,
`social-media/`, `pastoral-rhythm/`.

### Frontmatter

```yaml
---
name: skill-name          # kebab-case, matches the directory
description: What it does, what you give it, what you get back. Written so Claude can
  decide whether this skill applies. State the tier if it is 1 or 2.
---
```

### Required sections

1. **Title + one-line promise.** What the pastor walks away with.
2. **`> Requires: pastor-foundation skill`**
3. **What You Need to Provide.** Split required vs. optional. Always state the
   minimum viable input, and honor it. Never interrogate a pastor through five
   questions before doing any work.
4. **Numbered workflow steps.** What happens, in order.
5. **Output Format.** For document skills: the JSON schema and the generation command.
6. **Quality bar.** What "done" looks like, and the failure modes to avoid.

---

## Voice

Every skill sounds like the same person: a competent colleague who respects the
pastor's time and knows the work.

- **Warm and plain, not corporate.** A pastor, not a middle manager.
- **Assume smart but time-starved.** Do not over-explain. Do not pad.
- **No Christianese unless it is genuinely the clearest term.** "Follow-up," not
  "assimilation pathway." "Connect," not "do life together." "Serving," not
  "plugging in."
- **No em dashes.** Ever. Periods, commas, or colons.
- **Concise by default.** If a weekly email lands in 150 words, do not write 400. A
  pastor should not have to trim your output.
- **Say the hard thing.** If an agenda has too many items, if a series premise is
  thin, if a letter is going to land badly, say so before drafting.

### Banned phrases

Never use: "In an era of...", "In today's fast-paced...", "Navigate the complexities
of...", "Leverage your...", "Unlock the power of...", "Here's the thing...", "Let me
break this down...", "It's worth noting that...", "At the end of the day...",
"Passionate about...", "Thrilled to...", "Honored to...", "Game-changer", "Deep dive",
"Unpack" (as in "unpack this passage"), "Lean in/into", "Dive in/into", "Space" (as in
"holding space"), "Impactful", "Transformative".

### Banned structures

- Paragraphs longer than 3 sentences.
- Opening a sentence with "So," / "Well," / "Look," as filler.
- Closing with "Thoughts?" or "What do you think?" as fake engagement.
- Bullet lists over 7 items without subheadings.
- Three or more stacked adjectives ("powerful, dynamic, Spirit-led worship experience").
- A rhetorical question followed by "You're not alone."

---

## Output Standards

### Ready to use, not ready to rewrite
If more than 20% needs rewriting, the skill failed. Names, dates, church details, and
tone should be right on the first pass, pulled from `church-profile.md`.

### Every output ends with "Why this works"
One sentence on the thinking behind the approach. Not filler. Over time it teaches
the principle so the pastor needs the skill less.

> **Why this works:** Opening with the number (175 kids) makes the ask concrete and
> harder to scroll past than a generic "we need volunteers."

### Tier 1 and 2 outputs end with a handoff line
Research and care documents close by returning the work to the pastor. Vary the
wording; do not make it boilerplate. Something in the register of:

> This is raw material. Pray it through before it becomes a word for your people.

### Format for scanning
Pastors read on phones between meetings. Short paragraphs, clear headers, bold on key
phrases. No walls of text.

---

## Document Output

Skills that produce a document write **both a PDF and its markdown source** into
`output/` (gitignored).

### Wiring a generator

```python
from pdf_utils import (
    build_styles, create_doc, make_page_footer,
    add_church_footer, write_markdown, merge, load_profile,
)

profile = load_profile()          # reads church-profile.md
data = merge(data, profile)       # fills church_name, pastor_name, translation, etc.
                                  # explicit values in `data` always win
doc = create_doc(output_path, ...)          # bare filename -> output/
...
add_church_footer(story, styles, profile)   # congregation-facing only
page_footer = make_page_footer("church", profile)
doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)
write_markdown(doc.filename, data.get("markdown"))
return os.path.abspath(doc.filename)
```

Always include a `markdown` key in the JSON payload holding the same content as prose.
The PDF is for handing out; the markdown is for pasting into email, slides, or next
week's file.

### Branding modes

| Mode | Contact banner | Page footer | Used by |
|---|---|---|---|
| **Congregation-facing** | Yes, full letterhead | Church name + page | `church-letter`, `midweek-devotional`, `small-group-questions` |
| **Desk document** | No | Church name + page | `sermon-research`, `sermon-brainstorm`, `sermon-series`, `meeting-agenda`, `announcement-script`, `funeral-service`, `wedding-service`, `board-report` |

Choose the mode by **who holds the paper**, not by how nice it looks. If a document
contains anything the subject should not read (family landmines, warning signs,
what-not-to-say, governance candor), it is a desk document and must not carry
letterhead that makes it look distributable.

The banner reads from `church-profile.md` and **skips itself entirely** if the
letterhead fields are unfilled. A half-empty contact block looks worse than none.

There is no agency branding in this repo. Documents carry the church's identity or
nothing.

### Visual system

Defined once in `shared/pdf_utils.py`. Do not redefine colors in a generator.

- Navy `#1B2A4A` (headers, banners), Gold `#B8860B` (accents, rules)
- Body `#2D3436` Times-Roman 11/16, headers Helvetica-Bold
- Letter, 1" side margins, 0.85" top/bottom
- Skill-specific styles extend the base: `s = dict(base_styles); s["custom"] = ...`

---

## Dependencies

`reportlab` is the only one, and only for document skills. Do not add more without a
strong reason. A skill that needs an API key or a paid service is a skill this repo
does not want.

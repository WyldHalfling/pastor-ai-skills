---
argument-hint: "what the skill should do"
description: "Scaffold a new pastor skill against the repo's standards"
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
---

Think hard.

Build a new skill for: $ARGUMENTS

## Before writing anything

Read these in order. Do not skip them; the structure here is not freeform.

```bash
cat .ai/guidelines/project-guidelines.md   # tiers, guardrails, Rule Zero
cat .ai/guidelines/skill-standards.md      # anatomy, voice, output conventions
cat .ai/guidelines/features-guidelines.md  # what already exists
```

Then read two existing skills closest to what is being asked for, so the new one
matches the house style rather than inventing its own.

## Step 1: Decide the tier, and say so out loud

This is the first decision, and it governs everything downstream.

- **Tier 1** (sermon prep, personal study): research, structure, and questions only.
  No prose Phil would speak.
- **Tier 2** (pastoral care): preparation, logistics, structure, what to ask, what not
  to say. Formulaic liturgy is fine. The personal words about a specific human being
  are not.
- **Tier 3** (admin and communication): draft fully, ready to send.

If the skill as described would require producing a sermon manuscript or the personal
words of a pastoral moment, stop and say so. Propose the version that stays inside
Rule Zero instead. Do not quietly build the thing that crosses the line.

## Step 2: Check it does not already exist

If an existing skill covers 80% of this, extending it is better than adding a
near-duplicate. Say so and recommend that instead.

## Step 3: Build it

```
<category>/<skill-name>/
├── SKILL.md
├── generate-pdf.py     # only if it produces a document worth printing
└── references/         # only if it needs lookup tables
```

`SKILL.md` must have:

1. Frontmatter: `name` (kebab-case, matches the directory) and a `description` written
   so Claude can decide when the skill applies
2. Title plus a one-line promise
3. `> Requires: pastor-foundation skill`
4. **What You Need to Provide**, split required vs. optional, with a stated minimum
   viable input that the skill actually honors. Never interrogate Phil through five
   questions before doing any work.
5. Numbered workflow steps
6. Output Format, including the JSON schema if there is a generator
7. A quality bar: what "done" looks like and the failure modes to avoid

## Step 4: Wire the output

Markdown output goes to `output/`. If it produces a document worth printing, add a
`generate-pdf.py` that imports from `shared/pdf_utils.py`. Do not redefine colors or
restyle from scratch. Include a `markdown` key in the JSON payload.

Decide the branding mode deliberately: congregation-facing documents get
`add_church_footer`, desk documents do not.

## Step 5: Update the inventory

Add the skill to `.ai/guidelines/features-guidelines.md` in the same change. A skill
that is not in the inventory does not exist.

## Step 6: Verify

- Voice check against the banned-phrase and banned-structure lists. Enforce literally.
- No em dashes.
- Ends with "Why this works." Tier 1 and 2 also hand the work back to Phil.
- If there is a generator, run it against a sample payload and confirm the PDF and the
  markdown twin both land in `output/`.
- Tell Phil to run `/install-skills <name>` to make it live.

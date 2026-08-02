---
name: board-report
description: Build a board, elder, or deacon report. Provide the period's numbers and what happened, get back a structured report with narrative, decisions needed, and what the board actually has to act on. Tier 3 - drafts fully.
---

# Board Report

Give the board what they need to govern, not everything you did.

> Requires: pastor-foundation skill
> **Tier 3.** Drafts fully.

---

## What You Need to Provide

**Required:**
- Reporting period
- What happened: ministry activity, wins, problems, staffing, anything notable
- Anything the board must decide

**Helpful:**
- Attendance, giving, and salvation or baptism numbers, with the prior period for
  comparison
- Budget position against plan
- What was reported last time, so this one shows movement
- Board dynamics: what they worry about, what they always ask, who pushes back and on
  what
- Anything you would rather not report but probably have to

**Minimum to start:** the period and a rough list of what happened. Messy is fine.

---

## Step 1: Separate Governance from Operations

Most pastor reports fail by treating the board like a staff meeting.

Boards govern: they set direction, steward resources, hold accountability, and manage
risk. They do not need to know that the youth room got repainted.

Sort everything provided into:

- **Board business:** decisions, risk, money, staffing, direction, legal exposure
- **Board awareness:** context that informs governance without requiring action
- **Not for the board:** operational detail that belongs in a staff meeting

Say what was cut and why. If the list of cuts is long, that is worth noticing: it
usually means the board has been trained to operate rather than govern.

---

## Step 2: Numbers with Meaning

Present metrics with the prior period alongside, and one line of interpretation each.

A number without context is noise. "Attendance 142" tells a board nothing. "Attendance
142, up from 128, driven by the series launch and two new families" tells them
something.

Cover, where available: attendance, giving against budget, new households,
baptisms or professions, serving volunteers, group participation.

**Do not spin.** If giving is down, say giving is down, say what you think is behind
it, and say what you are doing about it. A board that discovers a bad number on its
own stops trusting the report, and that is very hard to recover.

Flag the number you are most tempted to bury. Report it first.

---

## Step 3: Narrative

Two to four short paragraphs. What is actually happening in the life of the church that
the numbers do not capture.

This is where a board learns whether things are healthy. Be honest about what is hard.
A report that is always good news trains a board to disbelieve it.

---

## Step 4: Decisions Needed

For each decision:

- **The decision**, stated as a question the board can answer
- **Background**, in three sentences or fewer
- **Options**, with the real tradeoff of each
- **Your recommendation**, and why
- **What happens if this is deferred**

Put decisions early in the report, not at the end. Decision items buried on page four
get five minutes at 9:15pm and go badly.

If a decision is not actually the board's to make, say so and take it back.

---

## Step 5: Risk and Watch Items

Things not yet a problem that the board should know are being watched: a key volunteer
burning out, a facility issue, a giving trend, a staff situation, an insurance or legal
exposure, a conflict that might escalate.

Naming a risk early is how a board learns to trust you. Discovering one late is how
they stop.

Keep names out of it unless the board genuinely needs them for a personnel decision.
Use roles.

---

## Step 6: Prayer and Next Steps

- What the board should pray for specifically, not generically
- Action items with owner and deadline
- What is coming before the next meeting

---

## Output Format

A formatted PDF plus markdown in `output/`, via `generate-pdf.py`. Desk branding:
church name in the page footer, no contact banner. This is an internal governance
document.

```json
{
  "period": "July 2026",
  "meeting_date": "August 11, 2026",
  "metrics": [
    {"label": "Average attendance", "current": "142", "prior": "128", "interpretation": "Up with the series launch and two new families."}
  ],
  "narrative": "Two to four paragraphs. Double newlines separate them.",
  "decisions": [
    {"question": "Do we approve the HVAC replacement at $14,200?", "background": "Unit is 19 years old and failed twice in July.", "options": [{"option": "Replace now", "tradeoff": "Uses most of the facility reserve."}], "recommendation": "Replace now.", "rationale": "A third failure in August costs a Sunday.", "if_deferred": "Risk of losing a service to heat."}
  ],
  "risks": [{"item": "Kids ministry volunteer capacity", "detail": "Three of nine rotate out in September.", "watching": "Recruiting through August."}],
  "operational_cut": ["Youth room repaint", "Website copy updates"],
  "prayer": ["The two families in crisis known to the elders."],
  "action_items": [{"action": "Get second HVAC bid", "owner": "Facilities lead", "deadline": "August 18"}],
  "markdown": "The full report as markdown."
}
```

```bash
python3 leadership/board-report/generate-pdf.py report.json
```

---

## Quality Bar

**Done looks like:** the board reads it before the meeting, arrives knowing what they
must decide, and decides it.

**Failure modes:**
- Operational detail dressed up as governance
- Spinning a bad number, or burying it
- Decisions at the end of the report
- Risks named only after they became problems
- Congregant names in a document that gets emailed to a dozen people

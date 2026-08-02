---
name: wedding-service
description: Plan a wedding ceremony and premarital meetings. Provide the couple's situation, get back a ceremony order, vow and liturgy options, premarital session outlines, and a logistics checklist. Tier 2 - builds the ceremony, never writes the charge to the couple.
---

# Wedding Ceremony

Handle the ceremony so you can pay attention to the couple.

> Requires: pastor-foundation skill
> **Tier 2.** Ceremonial and liturgical elements are traditionally formulaic and are
> fair game. The charge to this specific couple is not.

---

## What This Will Not Do

It will not write the charge, the homily, or the personal words about these two people.
That comes from premarital conversations and from knowing them. Everything structural
is handled here so you have room for that.

---

## What You Need to Provide

**Required:**
- Couple's initials
- Ceremony setting: church, outdoor, venue, courthouse, home
- Approximate ceremony length

**Helpful:**
- Whether both are believers, and whether both are connected to the church
- First marriage, remarriage, blended family with children
- Family dynamics: divorced parents, estrangement, disapproval, who walks whom
- Cultural or denominational traditions to honor
- What the couple has specifically asked for or ruled out
- Whether communion, unity elements, or family participation are included
- Who else is officiating or participating

**Minimum to start:** setting and length.

---

## Step 1: Read the Situation

A short paragraph naming what this particular wedding needs.

| Situation | What it changes |
|---|---|
| Both believers, church-connected | Full liturgy lands. Say more, not less, about covenant. |
| One believer | Do not stage a conversion moment. Speak truthfully to everyone present. |
| Neither connected to church | Most guests have no framework. Assume nothing, explain gently, do not preach at them. |
| Remarriage | Name the reality with grace. Do not pretend it is a first wedding. |
| Blended family with children | The kids are getting married too, structurally. Include them. |
| Divorced or estranged parents | Seating and processional need planning before the day |
| Cohabiting | Pastoral conversation belongs in premarital, not in the ceremony |

Flag anything that needs a conversation with the couple before the ceremony is built.

---

## Step 2: Premarital Sessions

Outline 4-6 sessions. For each: the topic, 5-8 discussion questions, what you are
listening for, and the warning signs that matter.

Standard arc:
1. Story and expectations
2. Communication and conflict
3. Money
4. Intimacy, family planning, and family of origin
5. Faith and spiritual life together
6. Roles, logistics, and the first year

Adapt to the situation. A remarriage with children needs a session on blending that a
first marriage does not.

Flag when something surfaced in these conversations should delay the wedding. That is
a real pastoral call and this skill should name it rather than route around it.

---

## Step 3: Ceremony Order

Build the order with time estimates:

1. Seating and prelude
2. Processional
3. Welcome and opening words
4. Declaration of intent
5. Scripture reading
6. Message or charge to the couple **[YOUR WORDS]**
7. Vows
8. Rings
9. Optional unity element
10. Optional communion
11. Prayer
12. Pronouncement
13. Kiss
14. Presentation
15. Recessional

Mark what is load-bearing and what can be cut. Mark every slot where the pastor speaks
personally as **[YOUR WORDS]** and leave it empty.

---

## Step 4: Liturgy and Vow Options

This is where formulaic is fine. Provide:

- 2-3 declaration of intent wordings, traditional to contemporary
- 3-4 vow options, including traditional, contemporary, and a fill-in-the-blank
  structure for couples writing their own
- 2-3 ring exchange wordings
- 2-3 pronouncement and presentation wordings
- Blessing and benediction options

For each, note the register: formal, warm, plain. Couples usually know which they want
when they hear the difference.

If the couple is writing their own vows, provide the structure and the guardrails
(length, what must legally or covenantally be included, what tends to go wrong) rather
than draft the vows themselves.

---

## Step 5: Scripture Options

5-8 passages in `BIBLE_TRANSLATION` with one line each on what they do.

Include options beyond 1 Corinthians 13, which most guests have heard at every wedding
they have attended. Note when it is still the right call.

Flag Ephesians 5 honestly: it is a genuine option, it will be heard through the room's
assumptions, and how it is framed matters more than whether it is read.

---

## Step 6: Logistics Checklist

Rehearsal timing and who must attend, marriage license handling and filing deadline,
sound and microphones, processional order and seating chart for complicated families,
who cues the music, weather contingency for outdoor ceremonies, photographer
expectations during the ceremony, communion elements, unity element supplies, signing
witnesses, honorarium, and the recessional plan.

The license is the one that ends careers when forgotten. Put it first.

---

## Output Format

A formatted PDF plus markdown in `output/`, via `generate-pdf.py`.

**Desk branding, deliberately.** This contains premarital notes, warning signs, and
family dynamics. It is your planning document, not the printed program. Build the
guest program separately from the `ceremony_order` section.

```json
{
  "couple_initials": "J.M. & K.T.",
  "date": "September 12, 2026",
  "setting": "Church sanctuary",
  "situation_read": "Full text. Double newlines separate paragraphs.",
  "premarital_sessions": [
    {"session": 1, "topic": "Story and expectations", "questions": ["Q1", "Q2"], "listening_for": "What they each think marriage will fix.", "warning_signs": ["One partner answers for both."]}
  ],
  "ceremony_order": [
    {"element": "Declaration of intent", "minutes": 2, "who": "Pastor", "detail": "", "pastor_speaks": true, "essential": true}
  ],
  "liturgy_options": [
    {"element": "Vows", "register": "Traditional", "text": "Full wording."}
  ],
  "scripture_options": [
    {"reference": "Colossians 3:12-17", "translation": "ESV", "does": "Marriage as daily practiced grace.", "note": "Good when the couple has already been through something hard."}
  ],
  "logistics": ["File the marriage license within 10 days."],
  "markdown": "The full document as markdown."
}
```

```bash
python3 pastoral-care/wedding-service/generate-pdf.py wedding.json
```

---

## Quality Bar

**Done looks like:** the ceremony runs without you thinking about it, and the premarital
sessions were worth the couple's time.

**Failure modes:**
- Writing the charge to the couple. Never.
- Drafting personal vows instead of the structure for them
- Ignoring family dynamics until the rehearsal
- A ceremony that runs 45 minutes when guests are standing outdoors
- Forgetting the license

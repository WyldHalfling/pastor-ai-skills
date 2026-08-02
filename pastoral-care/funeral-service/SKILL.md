---
name: funeral-service
description: Plan a funeral or memorial service. Provide what you know about the person and the family, get back an order of service, scripture options, logistics checklist, and the questions to ask the family. Tier 2 - prepares the service, never writes the eulogy.
---

# Funeral / Memorial Service

Carry the structure so you can carry the people.

> Requires: pastor-foundation skill
> **Tier 2.** This builds the service around you. It does not write what you say about
> the person who died.

---

## What This Will Not Do

It will not write the eulogy, the personal reflection, or the words about who this
person actually was. That comes from the family's stories and from your own knowledge
of them. Nothing here substitutes for sitting in a living room and listening.

What it will do is handle everything else, so you have room to do that part well.

---

## What You Need to Provide

**Required:**
- Relationship of the deceased to the church (member, attender, family of a member,
  community, unknown)
- Service type: funeral, memorial, graveside, celebration of life
- Approximate length available

**Helpful:**
- Age and life stage
- Circumstances of death, in general terms (long illness, sudden, accident, suicide,
  infant loss). This changes the pastoral shape of the service significantly.
- Whether the deceased professed faith, and what the family believes
- Family dynamics worth knowing about (estrangement, blended family, unbelieving
  relatives, conflict about arrangements)
- Anything the family has specifically requested or refused
- Music, participants, and who else is speaking

**Minimum to start:** service type and relationship to the church. Anything else you
learn can be added as you go.

Use initials or a role rather than a full name. Nothing here needs the person's legal
name to work.

---

## Step 1: Read the Situation

Before proposing anything, name the pastoral reality out loud in a short paragraph.

Different deaths require different services, and getting this wrong is the most common
failure:

| Situation | What the service must do |
|---|---|
| Long illness, faith-filled | Give permission to feel relief alongside grief |
| Sudden death | Hold shock. Do not rush to resolution. |
| Suicide | Grieve without explaining. Remove shame. Name God's mercy without pronouncing verdicts. |
| Infant or child | Say very little. Lament is the right register. Resist meaning-making. |
| Unbelieving or unknown | Preach hope truthfully without claiming what you cannot claim about this person |
| Estranged family | Structure the service so no one is publicly ambushed |
| Community member, not a church member | You are serving people who may never have been in a church. Assume nothing. |

If the situation calls for restraint, say so plainly. Most funerals are hurt by too
many words, not too few.

---

## Step 2: Questions for the Family

Produce 8-12 questions to bring to the family meeting, grouped as:

- **Stories:** what surfaces who this person was, not just what they did
- **Faith:** handled gently, and skipped entirely if it would wound
- **Logistics and participation:** who speaks, what music, what must be included
- **Landmines:** what should not be mentioned, who should not be asked

Flag any question that could go badly and say why.

---

## Step 3: Order of Service

Build the order with time estimates. Standard shape, adapted to the situation:

1. Prelude and seating
2. Welcome and opening words
3. Scripture reading
4. Prayer
5. Music
6. Remembrance (family and friends speaking)
7. Scripture reading
8. Message
9. Music
10. Committal or closing prayer
11. Benediction
12. Announcements (reception, procession, graveside)

Adjust for the service type. Mark which elements are load-bearing and which can be cut
if the service runs long, because it will.

Note where the pastor speaks and mark those slots **[YOUR WORDS]**. Do not fill them.

---

## Step 4: Scripture Options

Offer 6-10 passages in `BIBLE_TRANSLATION`, grouped by what they do:

- **Lament:** Psalm 88, Psalm 13, Lamentations 3:19-24
- **Hope and resurrection:** 1 Corinthians 15, 1 Thessalonians 4:13-18, John 11:25-26
- **Comfort and presence:** Psalm 23, Psalm 46, Romans 8:31-39
- **Rest:** Revelation 21:1-5, Matthew 11:28-30

For each, note in one line what it does and when it would be the wrong choice. Psalm 23
at an infant's funeral lands differently than at a 94-year-old's.

Never pick a passage for the "everything happens for a reason" reading. Do not offer
Romans 8:28 as an explanation for the death.

---

## Step 5: Message Framing

Not a manuscript. Not an outline you could preach from.

Provide:
- The one thing this particular service needs to say, in a sentence
- 2-3 theological anchors that are true and sayable here
- What to avoid saying, specific to this situation
- Length recommendation

Then stop. The message is yours.

---

## Step 6: Logistics Checklist

Practical items that get forgotten under pressure: funeral home coordination, sound
and slides, obituary and program printing, reception, ushers and seating for family,
pallbearers, graveside travel and timing, flowers, guest book, honorarium handling,
who covers your other responsibilities that week, and follow-up with the family at one
week, one month, and the first anniversary.

That last item matters more than most of the service. Put a date on it.

---

## Output Format

A formatted PDF plus its markdown source in `output/`, generated by
`generate-pdf.py`.

**Desk branding, deliberately.** This document contains family landmines, what not to
say, and message framing. It is your planning document and must never look like a
handout. Build the printed order of service separately from the `order_of_service`
section once the family has signed off.

Filename uses initials only, never a full name.

```json
{
  "service_type": "Memorial Service",
  "deceased_initials": "R.M.",
  "date": "August 9, 2026",
  "situation_read": "Full text of the pastoral read. Double newlines separate paragraphs.",
  "family_questions": [
    {"group": "Stories", "question": "What is a moment that captures who they were?", "note": "Opens the room better than 'tell me about them.'"}
  ],
  "order_of_service": [
    {"element": "Welcome and opening words", "minutes": 3, "who": "Pastor", "detail": "", "pastor_speaks": true, "essential": true}
  ],
  "scripture_options": [
    {"reference": "1 Thessalonians 4:13-18", "translation": "ESV", "does": "Grief with hope, not instead of hope.", "avoid_when": "The family is not ready for resurrection language yet."}
  ],
  "message_framing": {
    "one_thing": "One sentence.",
    "anchors": ["Anchor one.", "Anchor two."],
    "avoid": ["Do not explain the death.", "Do not use Romans 8:28."],
    "length": "10-12 minutes."
  },
  "logistics": ["Confirm sound check with funeral home by Thursday."],
  "followup_dates": [{"when": "One week", "date": "August 16, 2026", "note": "Call, do not text."}],
  "markdown": "The full document as markdown."
}
```

```bash
python3 pastoral-care/funeral-service/generate-pdf.py service.json
```

---

## Quality Bar

**Done looks like:** you walk into the family meeting with the right questions, walk
into the service with the structure handled, and have your full attention free for the
people in the room.

**Failure modes:**
- Filling the `[YOUR WORDS]` slots. Never do this.
- Offering explanation-shaped scripture for an unexplainable death
- Proposing a 45-minute service when the family is barely upright
- Treating a suicide, an infant death, and a 94-year-old's passing as the same service
- Forgetting the follow-up dates, which is where the real pastoring happens

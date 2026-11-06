# Features: Living Inventory

Status of every skill in the repo. Update this file when a skill is added, changed, or
retired. Tier definitions live in `project-guidelines.md`.

Legend: **Done** shipped · **MD** markdown output only · **PDF** PDF + markdown

---

## Foundation

| Skill | Status | Notes |
|---|---|---|
| `pastor-foundation` | Done | Reads `church-profile.md`. Voice, guardrails, church context. Required by every skill. |

---

## Sermon Prep: Tier 1 (research and thinking only)

| Skill | Status | Output | Cadence |
|---|---|---|---|
| `sermon-research` | Done | PDF (desk) | Weekly |
| `sermon-brainstorm` | Done | PDF (desk) | Weekly |
| `sermon-series` | Done | PDF (desk) | Monthly |

Hard boundary: none of these produce a manuscript, and none ever will.

---

## Pastoral Care: Tier 2 (preparation, not substitution)

| Skill | Status | Output | Cadence |
|---|---|---|---|
| `funeral-service` | Done | PDF (desk) | As needed |
| `wedding-service` | Done | PDF (desk) | As needed |
| `pastoral-visit` | Done | MD (private) | As needed |

Funeral and wedding PDFs are **planning documents**, not handouts. They contain family
landmines, warning signs, and what-not-to-say. Printed programs get built separately
from the order-of-service section once the family or couple has signed off.

`pastoral-visit` never writes a congregant's name to disk unless explicitly told to,
and never searches the web for a named person.

---

## Teaching & Discipleship: Tier 3

| Skill | Status | Output | Cadence |
|---|---|---|---|
| `small-group-curriculum` | Done | MD | Per series |
| `new-members-class` | Done | MD | Quarterly |

---

## Leadership & Admin: Tier 3

| Skill | Status | Output | Cadence |
|---|---|---|---|
| `board-report` | Done | PDF (desk) | Monthly |
| `volunteer-development` | Done | MD | As needed |
| `meeting-agenda` | Done | PDF (desk) | Weekly |

---

## Personal Study: Tier 1

| Skill | Status | Output | Cadence |
|---|---|---|---|
| `personal-study` | Done | MD | As needed |

Feeds the pastor, not the congregation. Output is explicitly not sermon material, and
the skill says so. Pairs with the `seminary-desk` project for M.Div. coursework.

---

## Written Communication: Tier 3

| Skill | Status | Output | Cadence |
|---|---|---|---|
| `church-email` | Done | MD | Weekly |
| `announcement-script` | Done | PDF (desk) | Weekly |
| `church-letter` | Done | PDF (congregation) | As needed |
| `midweek-devotional` | Done | PDF (congregation) | Weekly |

`midweek-devotional` is Tier 3 with a Tier 2 limit. It drafts the whole devotional and
never claims the pastor's experience of the passage. See the Tier 3 note in
`project-guidelines.md`.

---

## Sermon Repurposing: Tier 3

| Skill | Status | Output | Cadence |
|---|---|---|---|
| `small-group-questions` | Done | PDF (congregation) | Weekly |
| `sermon-to-blog` | Done | MD | Weekly |
| `sermon-to-youtube` | Done | MD | Weekly |

---

## Social Media: Tier 3

| Skill | Status | Output | Cadence |
|---|---|---|---|
| `church-social-post` | Done | MD | 3-5x/week |
| `social-media-calendar` | Done | MD | Weekly |

---

## Commands

| Command | Purpose |
|---|---|
| `/prime` | Load full project context before working on the repo |
| `/install-skills` | Sync skills from this repo into `~/.claude/skills/` |
| `/new-skill` | Scaffold a new skill against these standards |
| `/sunday` | Run the weekly ministry rhythm end to end |

---

## Backlog

Not built. Listed so the idea is not lost.

- `baptism-prep`: interview questions, testimony coaching, service logistics
- `benevolence-response`: framework for financial-request conversations, policy-shaped
- `annual-planning`: calendar, teaching arc, and emphasis mapping for a year
- `budget-narrative`: turning a spreadsheet into language a congregation understands
- `reading-plan`: personal or congregational scripture reading plans
- `staff-one-on-one`: recurring check-in prep and development tracking
- PDF generators for the markdown-only skills, if print versions turn out to matter

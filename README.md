# Pastor AI Skills

21 workflow skills that take the administrative weight off a pastor's week.

Built for [Claude Code](https://claude.com/claude-code). Personal toolkit, not a product.

---

## Rule Zero

**The Holy Spirit is the driver. The AI is never the driver.**

This is a rule about authority, not about output format, and it is enforced in the
skills themselves rather than left as a disclaimer.

The Spirit leads the pastor. The pastor directs the tool. The tool cannot hear from the
Spirit, so it holds no independent authority and never originates. Nothing enters the
work that the pastor did not allow.

- **Nothing gets added that you did not allow.** Not content, not emphasis, not a
  theological position, not an extra section, not an unrequested improvement.
- **Everything is proposed, never inserted.** You decide what stays.
- **Gaps get flagged, not filled.** If something seems missing, the skill says so and
  asks. Filling it quietly would take a decision that is yours.
- **Scope comes from you.** No widening because a fuller version would be better.
- **No personal words in a pastoral moment.** The eulogy reflection, the charge to a
  couple, what gets said at a bedside. Those require having been in the room.
- **No resolving contested passages.** Show the fault line and the best case on each
  side. Resolving it decides on your behalf.

The test: is there anything here you did not ask for and have not approved? If so it
comes out, or it gets flagged as an addition rather than buried.

**Standing instruction:** no sermon manuscripts. Ask for one and the skill will say no,
then offer the research, the structural options, and the questions instead. That is one
specific limit, not the whole of Rule Zero, which governs everything.

---

## Content Tiers

Every skill declares a tier, and the tier sets how much it may write.

| Tier | Covers | Produces | Never produces |
|---|---|---|---|
| **1** | Sermon prep, personal study | Research, context, tensions, questions, structural options | Prose you would speak |
| **2** | Pastoral care, life events | Preparation, logistics, questions to ask, things not to say, formulaic liturgy | The personal words about a specific person |
| **3** | Admin, communication | Complete, ready-to-send drafts | n/a |

Tier 3 is where the time savings live, and it holds nothing back. Tiers 1 and 2 are
where the line is, and the line holds.

---

## The Skills

| Skill | What it does | Tier | Cadence |
|---|---|---|---|
| **Sermon Prep** | | | |
| `/sermon-research` | Commentaries, historical context, word studies, thinking prompts | 1 | Weekly |
| `/sermon-brainstorm` | Guided questions that produce a sermon brief in your words | 1 | Weekly |
| `/sermon-series` | Multi-week series with titles, passages, and big ideas | 1 | Monthly |
| **Pastoral Care** | | | |
| `/funeral-service` | Order of service, family questions, scripture, follow-up dates | 2 | As needed |
| `/wedding-service` | Ceremony order, liturgy options, premarital sessions | 2 | As needed |
| `/pastoral-visit` | Prep for a hospital visit, grief call, or hard conversation | 2 | As needed |
| **Teaching** | | | |
| `/small-group-curriculum` | A whole multi-week study built for volunteer leaders | 3 | Per series |
| `/new-members-class` | Session plan, handout, and the path into real involvement | 3 | Quarterly |
| **Leadership** | | | |
| `/board-report` | Governance report with decisions up front and honest numbers | 3 | Monthly |
| `/volunteer-development` | Diagnose, define the role, recruit, onboard, keep | 3 | As needed |
| `/meeting-agenda` | Time-blocked agenda that ends on time and decides things | 3 | Weekly |
| **Personal** | | | |
| `/personal-study` | Scripture for your own soul. Deliberately not sermon material. | 1 | As needed |
| **Written Communication** | | | |
| `/church-email` | Weekly email: subject line, preview text, body | 3 | Weekly |
| `/announcement-script` | 60-90 second spoken script for Sunday morning | 3 | Weekly |
| `/church-letter` | Transitions, updates, celebrations, hard news | 3 | As needed |
| **Sermon Repurposing** | | | |
| `/small-group-questions` | Sunday's sermon into Monday's discussion guide | 3 | Weekly |
| `/sermon-to-blog` | An 800-1200 word article, not a transcript | 3 | Weekly |
| `/sermon-to-youtube` | Title, description, tags, thumbnail, clip recommendation | 3 | Weekly |
| **Social Media** | | | |
| `/church-social-post` | Facebook, Instagram, and Twitter versions of one idea | 3 | 3-5x/week |
| `/social-media-calendar` | A week or month mapped to dates and platforms | 3 | Weekly |
| **Foundation** | | | |
| `pastor-foundation` | Shared voice, guardrails, and church context. Required by all. | n/a | Once |

---

## Commands

| Command | What it does |
|---|---|
| `/prime` | Load full project context before working on this repo |
| `/install-skills` | Sync skills into `~/.claude/skills/` so they work everywhere |
| `/new-skill` | Scaffold a new skill against the repo standards |
| `/sunday` | Run the weekly rhythm: prep, communicate, repurpose |

---

## Setup

### 1. Fill in your church profile

`church-profile.md` is the single source of truth. Every skill reads it, and nothing is
ever guessed at generation time.

```ini
CHURCH_NAME: <FILL IN>
PASTOR_NAME: Phil Konsor
PASTOR_TITLE: <FILL IN>
DENOMINATION: <FILL IN>
LOCATION: <FILL IN>
ATTENDANCE: <FILL IN>
BIBLE_TRANSLATION: <FILL IN>
CHURCH_WEBSITE: <FILL IN>
CHURCH_ADDRESS: <FILL IN>
SERVICE_TIMES: <FILL IN>
CHURCH_TAGLINE: <FILL IN>
```

Anything left unfilled is omitted from output rather than invented. `ATTENDANCE` is
load-bearing: it right-sizes every recommendation, because a church of 80 is not a
church of 800.

### 2. Install the skills

```bash
./scripts/install-skills.sh              # everything
./scripts/install-skills.sh --list       # see what is available
./scripts/install-skills.sh sermon-research church-email
```

Skills only work as `/skill-name` once they are in `~/.claude/skills/`. Editing a
SKILL.md here does nothing until it is synced. `pastor-foundation` and `shared/` are
always included.

### 3. Install reportlab (document skills only)

```bash
pip install reportlab
```

---

## Output

Everything generated lands in `output/`, which is gitignored. Sermon prep, letters, and
care notes stay on the machine and never reach a commit.

Document skills produce **both a PDF and its markdown source**. The PDF is for handing
out. The markdown is for pasting into email, a slide, or next week's file.

Override the location with `PASTOR_OUTPUT_DIR`.

### Branding

Documents carry your church's identity or nothing. There is no agency or vendor
branding anywhere in this repo.

- **Congregation-facing** documents get full letterhead: church name, tagline, service
  times, address, website.
- **Desk documents** get the church name in the page footer and nothing else.

Anything containing what a subject should not read (family landmines, warning signs,
governance candor) is a desk document by rule, so it never looks distributable. The
letterhead skips itself entirely if the profile fields are unfilled.

---

## Confidentiality

Ministry generates some of the most sensitive information a person handles.

**Everything you type reaches Anthropic.** Gitignored output protects your disk, not
your request. A diagnosis, a confession, or a personnel matter leaves the machine the
moment it enters a prompt and cannot be recalled, and clergy confidentiality does not
travel across that boundary. Working from the situation instead of the identity is the
only protection that acts before the data leaves, which is why the care skills insist on
it. Some conversations belong on paper or with a colleague instead, and the skills will
say so.

- No congregant name, diagnosis, marital situation, financial state, or disciplinary
  matter goes into a filename, a commit message, or anything leaving the machine.
  Care documents use initials or a role.
- `/pastoral-visit` works from the situation, not the identity, and writes nothing to
  disk unless asked.
- No web search is ever run on a named congregant.

If you make this repo public, scrub `church-profile.md` first or move it out and point
`PASTOR_PROFILE_PATH` at the new location.

---

## Working On This Repo

Read `CLAUDE.md`, then `.ai/guidelines/`:

- `project-guidelines.md`: intent, tiers, guardrails, confidentiality (authoritative)
- `skill-standards.md`: anatomy, voice, banned patterns, PDF conventions
- `features-guidelines.md`: living inventory and backlog

Or just run `/prime`.

---

## Credit

Forked from [Thomas Costello's pastor-ai-skills](https://github.com/tkcostello/pastor-ai-skills)
and retooled: Rule Zero and the tier system made explicit and enforced, agency branding
replaced with church letterhead, a single church profile as the source of truth,
gitignored output, confidentiality rules, and skills added for pastoral care, teaching,
leadership, and personal study.

The original is a genuinely good piece of work and the communications skills are close
to his design.

## License

MIT.

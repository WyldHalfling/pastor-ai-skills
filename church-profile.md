# Church Profile

This is the single source of truth for every skill in this repo. The `pastor-foundation`
skill reads it for voice and context, and `shared/church_profile.py` reads it so PDF
generators can stamp letterhead.

Anything left as `<FILL IN>` falls back to a neutral default or is omitted from
documents entirely. Nothing here is guessed at generation time.

> **STATUS: PRE-PLACEMENT.** Phil is not currently serving a church. `FaithBuilt Church`
> is a placeholder used for testing and formatting, not a real congregation. Do not
> treat it as one. Before any document goes to real people, this file has to be updated
> with the actual church. Say so if a task assumes a congregation that does not exist yet.

```ini
# --- Identity ---
CHURCH_NAME: FaithBuilt Church
PASTOR_NAME: Phil Konsor
PASTOR_TITLE: Pastor
DENOMINATION: Evangelical Free Church (EFCA)

# --- Context ---
LOCATION: Ham Lake, MN
ATTENDANCE: <FILL IN>
BIBLE_TRANSLATION: ESV
BIBLE_TRANSLATION_SECONDARY: NIV

# --- Letterhead (used on congregation-facing PDFs) ---
CHURCH_WEBSITE: <FILL IN>
CHURCH_ADDRESS: <FILL IN>
SERVICE_TIMES: <FILL IN>
CHURCH_TAGLINE: <FILL IN>
```

---

## Current State of This Profile

**Placeholder:** `CHURCH_NAME` is a stand-in. See the status note above.

**Deliberately unfilled:**

- `ATTENDANCE` is blank because there is no congregation to count. Right-sizing is
  therefore off: recommendations will stay generic instead of scaling to a real church.
  Ask for a number before giving staffing, program, or volunteer advice that depends on
  size, rather than assuming one.
- The four letterhead fields are blank, so the contact banner **skips itself entirely**
  on congregation-facing PDFs. Documents still carry the church name in the page footer.
  This is correct for now, not an oversight.

**Denomination in flux:** EFCA currently, with a possible move to the Evangelical
Covenant Church. Hold the EFCA lens for now. Where the two traditions differ in a way
that actually affects the output, say so rather than quietly picking one.

---

## Translations

`BIBLE_TRANSLATION` is the default for every quoted verse. `BIBLE_TRANSLATION_SECONDARY`
is for comparison, not for general use.

- Quote ESV by default, always with book, chapter, and verse.
- Bring in NIV when the two render a phrase differently in a way that changes the
  meaning, or when a word study turns on the difference. Label which is which.
- Do not stack both translations on routine quotations. It clutters the page and helps
  no one.

---

## Field Notes

| Field | Used for | If left blank |
|---|---|---|
| `CHURCH_NAME` | PDF banner, every reference to "the church" | Documents say "the church"; banner is omitted |
| `PASTOR_NAME` | Sign-offs, PDF author metadata, page footer | Sign-offs are left blank for you to fill |
| `PASTOR_TITLE` | Letters, formal communication | Omitted |
| `DENOMINATION` | Theological lens. See guardrails in `pastor-foundation` | Broad evangelical center |
| `LOCATION` | Local references, seasonal and regional context | No local references made |
| `ATTENDANCE` | Right-sizing recommendations | Recommendations stay generic |
| `BIBLE_TRANSLATION` | Every quoted verse | NIV |
| `BIBLE_TRANSLATION_SECONDARY` | Comparison when renderings differ meaningfully | No comparison offered |
| `CHURCH_WEBSITE` | Contact block on congregation-facing PDFs | Contact block omitted |
| `CHURCH_ADDRESS` | Contact block, letterhead | Omitted from contact block |
| `SERVICE_TIMES` | Contact block, invitation language | Omitted |
| `CHURCH_TAGLINE` | Contact block on congregation-facing PDFs | Omitted |

---

## Privacy

This file contains real details about a real church once it is filled in properly. It is
tracked in git.

If this repo is ever made public, either scrub this file first or move it out of the
repo and point `PASTOR_PROFILE_PATH` at the new location:

```bash
export PASTOR_PROFILE_PATH=~/.config/pastor/church-profile.md
```

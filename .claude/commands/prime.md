---
argument-hint: "topic or area to prime on"
description: "Prime Claude with context about a specific topic or area of the pastor skills repo"
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch
---

Think hard.

Search the repo to gain comprehensive context and understanding about: $ARGUMENTS

# Prime Context for Claude Code: Pastor AI Skills

**CRITICAL**: Always start with reading context files in this specific order:

1. **Primary Context Files**: Read these FIRST:
   ```bash
   # Product intent, content tiers, theological guardrails (AUTHORITATIVE)
   cat .ai/guidelines/project-guidelines.md

   # Voice, banned patterns, PDF and output conventions (AUTHORITATIVE for craft)
   cat .ai/guidelines/skill-standards.md

   # Living inventory of every skill and its status
   cat .ai/guidelines/features-guidelines.md

   # Phil's actual church details. Never guess these.
   cat church-profile.md

   # Claude instructions
   cat CLAUDE.md

   # Public-facing overview
   cat README.md
   ```

2. **Project Structure**:
   ```bash
   tree -I '__pycache__|.git|output|venv' --dirsfirst -L 3
   ```

3. **The Shared Layer** (every document skill depends on it):
   ```bash
   cat foundation/pastor-foundation/SKILL.md
   cat shared/pdf_utils.py
   cat shared/church_profile.py
   ```

4. **The Skills Themselves**: read the SKILL.md files in the area you are priming on.
   ```bash
   ls */*/SKILL.md
   head -20 <category>/<skill>/SKILL.md
   ```

Focus on:
- **Rule Zero above all**: the Holy Spirit is the driver, Claude is never the driver.
  This is about authority, not output format. The Spirit leads Phil, Phil directs the
  tool, and the tool cannot hear from the Spirit, so it never originates. Add nothing
  Phil has not allowed. Propose, never insert. Flag gaps rather than fill them. If you
  internalize one thing here, this is it.
- The three content tiers and which tier the area you are working in falls into
- Skill anatomy: frontmatter, minimum viable input, numbered workflow, output format
- The `church-profile.md` → `merge()` → generator data flow
- Branding split: congregation-facing documents get the contact banner, desk documents
  do not
- Output convention: PDF plus markdown into gitignored `output/`
- Voice rules and the banned-phrase list, which are enforced literally
- Confidentiality: nothing about a named congregant goes into a filename, a commit, or
  a web search
- Right-sizing to `ATTENDANCE`: a church of 80 is not a church of 800

**Theological Care** (when the topic touches scripture or doctrine):
1. Check which guardrails in `project-guidelines.md` apply
2. Stay in the evangelical mainstream on contested secondary issues unless
   `DENOMINATION` is set in `church-profile.md`
3. Never fabricate a commentary quote, citation, or attribution
4. Quote scripture in `BIBLE_TRANSLATION`, always with book, chapter, and verse

**Web Research for External Third-Party Technologies** (when applicable):
If the topic involves external APIs, libraries, or integrations:
1. Identify external dependencies
2. Search for official documentation via WebSearch
3. Document findings including links

Never web-search for a named congregant. Ever.

Search the repo thoroughly to build a complete understanding.

After studying this you should have a good understanding of:
- Repo structure and the foundation/shared/skill layering
- The pastoral domain: Phil's weekly rhythm, what actually saves him time, and what he
  must never hand off
- Rule Zero and the tier system that enforces it
- Key files and their purposes
- The PDF pipeline and church-profile data flow
- Conventions for adding a skill without breaking consistency
- Any important dependencies and configuration

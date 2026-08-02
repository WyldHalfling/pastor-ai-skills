---
argument-hint: "[skill names, or blank for all]"
description: "Sync skills from this repo into ~/.claude/skills/ so they work everywhere"
allowed-tools: Bash, Read, Glob
---

Install or refresh skills from this repo into `~/.claude/skills/`: $ARGUMENTS

Skills only work as `/skill-name` once they live in `~/.claude/skills/`. Editing a
SKILL.md in this repo does nothing until it is synced.

## Steps

1. Show what is currently available and installed:
   ```bash
   ./scripts/install-skills.sh --list
   ```

2. Install. With no arguments, install everything. With names, install just those.
   `pastor-foundation` and `shared/` are always included because every other skill
   depends on them.
   ```bash
   ./scripts/install-skills.sh $ARGUMENTS
   ```

3. Confirm the result and report which skills are now live.

4. If `church-profile.md` still contains `<FILL IN>` placeholders, tell Phil which
   fields are unfilled and what each one affects. Do not fill them in yourself and do
   not guess a church name, attendance figure, or location.

5. If any installed skill has a `generate-pdf.py`, verify `reportlab` is importable:
   ```bash
   python3 -c "import reportlab; print(reportlab.Version)"
   ```
   If it is missing, tell Phil to run `pip install reportlab`. Do not attempt a system
   package install without asking.

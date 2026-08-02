---
argument-hint: "passage, series, or 'status'"
description: "Run the weekly ministry rhythm: prep, communicate, repurpose"
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

Work the week for: $ARGUMENTS

This chains the skills that recur every week so Phil does not have to invoke them one
at a time and re-supply the same context to each.

## Ground rule

Rule Zero governs this entire flow. You are doing the mechanical and administrative
work of the week. You are not preparing the message. The research and the brief feed
Phil's study; they do not replace it, and nothing in this flow produces a manuscript.

This flow chains several skills, which makes it the easiest place to overstep. Add
nothing Phil did not ask for. If a step seems worth running and he did not name it,
ask before running it rather than running it and reporting afterward.

Read `.ai/guidelines/project-guidelines.md` before starting if it is not already in
context.

## Step 0: Orient

Read `church-profile.md`. If required fields are still `<FILL IN>`, say which, and
work without them rather than inventing values.

Then ask what is actually needed this week, in **one** message, not a five-question
interrogation:

- The passage or topic for Sunday
- Anything that must go in the email or announcements (events, deadlines, volunteer
  needs)
- Whether last Sunday's sermon needs repurposing, and if so where the transcript or
  notes live

If Phil said `status`, just report what already exists in `output/` for this week and
what has not been produced yet. Then stop.

## Step 1: Prep the message (Tier 1)

If a passage was given:
- Run `sermon-research` on it
- Offer `sermon-brainstorm` if Phil wants to think it through rather than read research

Hand back research and questions. Stop there. Do not drift into outlining the sermon.

## Step 2: Communication (Tier 3)

From the announcements provided:
- `church-email` for the weekly send
- `announcement-script` for Sunday morning, if there is anything worth saying aloud

Flag anything that should be cut rather than communicated. Ruthless prioritization is
the value here, not coverage.

## Step 3: Repurpose last Sunday (Tier 3)

If a transcript or notes were provided:
- `small-group-questions` for the groups
- `sermon-to-blog` and `sermon-to-youtube` if that content actually gets published.
  Skip them if it does not; do not generate content nobody will post.

## Step 4: Rhythm

- `midweek-devotional` if Wednesday sends are part of the rhythm
- `social-media-calendar` if the week's posts are not already planned

## Step 5: Report

List what landed in `output/`, what still needs Phil, and anything you deliberately
skipped and why.

Close by naming the one thing in this batch that most needs prayer before it goes out.

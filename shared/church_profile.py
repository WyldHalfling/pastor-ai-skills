#!/usr/bin/env python3
"""
Church profile loader.

Reads `church-profile.md` and returns a plain dict of KEY -> value. Values still set
to the `<FILL IN>` placeholder are treated as absent, so downstream code can rely on
`profile.get("CHURCH_WEBSITE")` being falsy until the pastor actually fills it in.

Lookup order:
  1. $PASTOR_PROFILE_PATH (explicit override)
  2. church-profile.md walking up from this file toward the repo root
  3. ~/.config/pastor/church-profile.md
"""

import os
import re

PLACEHOLDER = "<FILL IN>"

# Matches `KEY: value` lines. Keys are SCREAMING_SNAKE_CASE so prose in the surrounding
# markdown (and the `# --- Section ---` comments inside the block) never match.
_FIELD_RE = re.compile(r"^([A-Z][A-Z0-9_]*):\s*(.*)$")


def _candidate_paths():
    override = os.environ.get("PASTOR_PROFILE_PATH")
    if override:
        yield os.path.expanduser(override)

    here = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        yield os.path.join(here, "church-profile.md")
        parent = os.path.dirname(here)
        if parent == here:
            break
        here = parent

    yield os.path.expanduser("~/.config/pastor/church-profile.md")


def find_profile_path():
    """Return the path to the first church-profile.md found, or None."""
    for path in _candidate_paths():
        if os.path.isfile(path):
            return path
    return None


def load_profile(path=None):
    """Load the church profile into a dict.

    Unfilled placeholders and blank values are omitted from the result, so a missing
    key and an unfilled key behave identically to callers.
    """
    path = path or find_profile_path()
    if not path or not os.path.isfile(path):
        return {}

    profile = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("|"):
                continue
            match = _FIELD_RE.match(line)
            if not match:
                continue
            key, value = match.group(1), match.group(2).strip()
            if not value or value == PLACEHOLDER:
                continue
            profile[key] = value

    return profile


def merge(data, profile=None):
    """Fill missing church fields in a generator's JSON payload from the profile.

    Explicit values in `data` always win. This lets a skill pass an override without
    the profile silently clobbering it.
    """
    profile = load_profile() if profile is None else profile
    merged = dict(data)

    aliases = {
        "church_name": "CHURCH_NAME",
        "pastor_name": "PASTOR_NAME",
        "pastor_title": "PASTOR_TITLE",
        "translation": "BIBLE_TRANSLATION",
        "translation_secondary": "BIBLE_TRANSLATION_SECONDARY",
        "church_website": "CHURCH_WEBSITE",
        "church_address": "CHURCH_ADDRESS",
        "service_times": "SERVICE_TIMES",
        "church_tagline": "CHURCH_TAGLINE",
    }

    for json_key, profile_key in aliases.items():
        if not merged.get(json_key) and profile.get(profile_key):
            merged[json_key] = profile[profile_key]

    return merged


if __name__ == "__main__":
    found = find_profile_path()
    print(f"Profile: {found or 'not found'}")
    for k, v in sorted(load_profile().items()):
        print(f"  {k}: {v}")

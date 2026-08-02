#!/usr/bin/env bash
# Sync skills from this repo into ~/.claude/skills/ so they are callable as /skill-name.
#
#   ./scripts/install-skills.sh              # install everything
#   ./scripts/install-skills.sh sermon-research church-email
#   ./scripts/install-skills.sh --list       # show what is available and what is installed
#   ./scripts/install-skills.sh --dry-run    # show what would change
#
# pastor-foundation is always installed. Every other skill depends on it.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
DRY_RUN=0

find_skills() {
    find "$REPO_ROOT" -mindepth 3 -maxdepth 3 -name SKILL.md -not -path "*/.git/*" \
        | sort
}

skill_name_of() { basename "$(dirname "$1")"; }

if [[ "${1:-}" == "--list" ]]; then
    printf '%-28s %-18s %s\n' "SKILL" "STATUS" "CATEGORY"
    while IFS= read -r skill_md; do
        dir="$(dirname "$skill_md")"
        name="$(basename "$dir")"
        category="$(basename "$(dirname "$dir")")"
        if [[ -d "$DEST/$name" ]]; then status="installed"; else status="-"; fi
        printf '%-28s %-18s %s\n' "$name" "$status" "$category"
    done < <(find_skills)
    exit 0
fi

if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=1
    shift
fi

mkdir -p "$DEST"

# Explicitly named skills, or all of them. Foundation is never optional.
requested=("$@")
installed_count=0

while IFS= read -r skill_md; do
    dir="$(dirname "$skill_md")"
    name="$(basename "$dir")"

    if [[ ${#requested[@]} -gt 0 && "$name" != "pastor-foundation" ]]; then
        match=0
        for want in "${requested[@]}"; do
            [[ "$want" == "$name" ]] && match=1
        done
        [[ $match -eq 1 ]] || continue
    fi

    if [[ $DRY_RUN -eq 1 ]]; then
        echo "would install $name -> $DEST/$name"
    else
        rm -rf "${DEST:?}/$name"
        cp -r "$dir" "$DEST/$name"
        echo "installed $name"
    fi
    installed_count=$((installed_count + 1))
done < <(find_skills)

# Document skills do `sys.path.insert(0, <this file>/../../shared)`. From an installed
# skill at $DEST/<name>/ that resolves to $(dirname $DEST)/shared, NOT inside $DEST.
# Putting it anywhere else gives ModuleNotFoundError: pdf_utils at generation time.
SHARED_DEST="$(dirname "$DEST")/shared"

if [[ $DRY_RUN -eq 0 ]]; then
    # Clean up the location used by earlier versions of this script.
    rm -rf "${DEST:?}/pastor-shared"

    rm -rf "$SHARED_DEST"
    cp -r "$REPO_ROOT/shared" "$SHARED_DEST"
    echo "installed shared/ -> $SHARED_DEST"

    # The profile is symlinked, not copied, so edits to church-profile.md take effect
    # immediately. A copy would go stale silently and put wrong church details on a
    # real document. If the symlink ever dangles, load_profile() returns nothing and
    # fields are omitted rather than wrong.
    if ln -sfn "$REPO_ROOT/church-profile.md" "$SHARED_DEST/church-profile.md" 2>/dev/null; then
        echo "linked church-profile.md -> $SHARED_DEST/church-profile.md (live)"
    else
        cp "$REPO_ROOT/church-profile.md" "$SHARED_DEST/church-profile.md"
        echo "copied church-profile.md -> $SHARED_DEST (re-run this script after editing it)"
    fi
fi

echo
echo "$installed_count skill(s) synced to $DEST"

# Match only real field lines (KEY: <FILL IN>), never prose that mentions the marker.
unfilled="$(grep -oE '^[A-Z][A-Z0-9_]*(?=: *<FILL IN>)' -P "$REPO_ROOT/church-profile.md" 2>/dev/null \
            || grep -E '^[A-Z][A-Z0-9_]*: *<FILL IN>' "$REPO_ROOT/church-profile.md" 2>/dev/null | cut -d: -f1)"

if [[ -n "$unfilled" ]]; then
    echo
    echo "NOTE: church-profile.md still has unfilled fields:"
    echo "$unfilled" | sed 's/^/      /'
    echo "      Those details are omitted from output until filled in."
fi

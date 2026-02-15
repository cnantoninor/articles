#!/usr/bin/env bash
# sync-rules.sh — Create/update symlinks for AI rules and commands across Cursor and Claude Code
#
# Sources of truth:
#   .ai/rules/*.md      — file-pattern and manual rules
#   .ai/commands/*.md    — reusable command/prompt templates
# Targets:
#   .cursor/rules/*.mdc     (rule symlinks with .mdc extension for Cursor)
#   .cursor/commands/*.mdc   (command symlinks with .mdc extension for Cursor)
#   .claude/rules/*.md       (rule symlinks with .md extension for Claude Code)
#   .claude/commands/*.md    (command symlinks with .md extension for Claude Code)
#   CLAUDE.md                (symlink to .ai/context.md — always-applied)
#
# Usage: bash .ai/sync-rules.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AI_RULES_DIR="$REPO_ROOT/.ai/rules"
AI_COMMANDS_DIR="$REPO_ROOT/.ai/commands"
CURSOR_RULES_DIR="$REPO_ROOT/.cursor/rules"
CURSOR_COMMANDS_DIR="$REPO_ROOT/.cursor/commands"
CLAUDE_RULES_DIR="$REPO_ROOT/.claude/rules"
CLAUDE_COMMANDS_DIR="$REPO_ROOT/.claude/commands"

created=0
updated=0
removed=0
errors=0

log()   { echo "  $1"; }
ok()    { echo "  ✓ $1"; }
warn()  { echo "  ⚠ $1"; }
err()   { echo "  ✗ $1"; errors=$((errors + 1)); }

echo "=== sync-rules.sh ==="
echo ""

# --- 1. Create target directories ---
echo "Creating directories..."
for dir in "$CURSOR_RULES_DIR" "$CURSOR_COMMANDS_DIR" "$CLAUDE_RULES_DIR" "$CLAUDE_COMMANDS_DIR"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        ok "Created $dir"
    else
        log "Exists: $dir"
    fi
done
echo ""

# --- 2. Sync rule files ---
echo "Syncing rule files from .ai/rules/..."

for src in "$AI_RULES_DIR"/*.md; do
    [ -f "$src" ] || continue
    basename="$(basename "$src" .md)"

    # Cursor: .mdc extension, relative symlink
    cursor_link="$CURSOR_RULES_DIR/${basename}.mdc"
    cursor_target="../../.ai/rules/${basename}.md"
    if [ -L "$cursor_link" ]; then
        current="$(readlink "$cursor_link")"
        if [ "$current" = "$cursor_target" ]; then
            log "Up to date: .cursor/rules/${basename}.mdc"
        else
            ln -sf "$cursor_target" "$cursor_link"
            ok "Updated: .cursor/rules/${basename}.mdc"
            updated=$((updated + 1))
        fi
    else
        [ -e "$cursor_link" ] && rm "$cursor_link"  # Remove non-symlink if exists
        ln -s "$cursor_target" "$cursor_link"
        ok "Created: .cursor/rules/${basename}.mdc"
        created=$((created + 1))
    fi

    # Claude Code: .md extension, relative symlink
    claude_link="$CLAUDE_RULES_DIR/${basename}.md"
    claude_target="../../.ai/rules/${basename}.md"
    if [ -L "$claude_link" ]; then
        current="$(readlink "$claude_link")"
        if [ "$current" = "$claude_target" ]; then
            log "Up to date: .claude/rules/${basename}.md"
        else
            ln -sf "$claude_target" "$claude_link"
            ok "Updated: .claude/rules/${basename}.md"
            updated=$((updated + 1))
        fi
    else
        [ -e "$claude_link" ] && rm "$claude_link"
        ln -s "$claude_target" "$claude_link"
        ok "Created: .claude/rules/${basename}.md"
        created=$((created + 1))
    fi
done
echo ""

# --- 2b. Sync command files ---
echo "Syncing command files from .ai/commands/..."

for src in "$AI_COMMANDS_DIR"/*.md; do
    [ -f "$src" ] || continue
    basename="$(basename "$src" .md)"

    # Cursor: .mdc extension, relative symlink
    # Cursor commands may use a namespace prefix (e.g. "ar:command-name.mdc").
    # If an existing symlink already points to the same target, skip creation
    # to avoid duplicates with different names.
    cursor_link="$CURSOR_COMMANDS_DIR/${basename}.mdc"
    cursor_target="../../.ai/commands/${basename}.md"
    existing_cursor=""
    for candidate in "$CURSOR_COMMANDS_DIR"/*.mdc; do
        [ -L "$candidate" ] || continue
        if [ "$(readlink "$candidate")" = "$cursor_target" ]; then
            existing_cursor="$candidate"
            break
        fi
    done
    if [ -n "$existing_cursor" ]; then
        log "Up to date: .cursor/commands/$(basename "$existing_cursor")"
    elif [ -L "$cursor_link" ]; then
        ln -sf "$cursor_target" "$cursor_link"
        ok "Updated: .cursor/commands/${basename}.mdc"
        updated=$((updated + 1))
    else
        [ -e "$cursor_link" ] && rm "$cursor_link"  # Remove non-symlink if exists
        ln -s "$cursor_target" "$cursor_link"
        ok "Created: .cursor/commands/${basename}.mdc"
        created=$((created + 1))
    fi

    # Claude Code: .md extension, relative symlink
    claude_link="$CLAUDE_COMMANDS_DIR/${basename}.md"
    claude_target="../../.ai/commands/${basename}.md"
    if [ -L "$claude_link" ]; then
        current="$(readlink "$claude_link")"
        if [ "$current" = "$claude_target" ]; then
            log "Up to date: .claude/commands/${basename}.md"
        else
            ln -sf "$claude_target" "$claude_link"
            ok "Updated: .claude/commands/${basename}.md"
            updated=$((updated + 1))
        fi
    else
        [ -e "$claude_link" ] && rm "$claude_link"
        ln -s "$claude_target" "$claude_link"
        ok "Created: .claude/commands/${basename}.md"
        created=$((created + 1))
    fi
done
echo ""

# --- 3. Root symlinks (always-applied context) ---
echo "Syncing root symlinks..."

for root_link in "CLAUDE.md"; do
    link_path="$REPO_ROOT/$root_link"
    target=".ai/context.md"
    if [ -L "$link_path" ]; then
        current="$(readlink "$link_path")"
        if [ "$current" = "$target" ]; then
            log "Up to date: $root_link"
        else
            ln -sf "$target" "$link_path"
            ok "Updated: $root_link -> $target"
            updated=$((updated + 1))
        fi
    else
        [ -e "$link_path" ] && rm "$link_path"  # Remove existing file
        ln -s "$target" "$link_path"
        ok "Created: $root_link -> $target"
        created=$((created + 1))
    fi
done
echo ""

# --- 4. Remove stale symlinks ---
echo "Checking for stale symlinks..."

# Stale .cursor/rules/*.mdc
for link in "$CURSOR_RULES_DIR"/*.mdc; do
    [ -L "$link" ] || continue
    basename="$(basename "$link" .mdc)"
    if [ ! -f "$AI_RULES_DIR/${basename}.md" ]; then
        rm "$link"
        ok "Removed stale: .cursor/rules/${basename}.mdc"
        removed=$((removed + 1))
    fi
done

# Stale .cursor/commands/*.mdc
# Note: Cursor commands may use a namespace prefix (e.g. "ar:") that differs
# from the .ai/commands/ basename.  Check whether the symlink target resolves
# rather than relying on name matching alone.
for link in "$CURSOR_COMMANDS_DIR"/*.mdc; do
    [ -L "$link" ] || continue
    basename="$(basename "$link" .mdc)"
    if [ ! -e "$link" ]; then
        rm "$link"
        ok "Removed stale: .cursor/commands/${basename}.mdc"
        removed=$((removed + 1))
    fi
done

# Stale .claude/rules/*.md
for link in "$CLAUDE_RULES_DIR"/*.md; do
    [ -L "$link" ] || continue
    basename="$(basename "$link" .md)"
    if [ ! -f "$AI_RULES_DIR/${basename}.md" ]; then
        rm "$link"
        ok "Removed stale: .claude/rules/${basename}.md"
        removed=$((removed + 1))
    fi
done

# Stale .claude/commands/*.md
for link in "$CLAUDE_COMMANDS_DIR"/*.md; do
    [ -L "$link" ] || continue
    basename="$(basename "$link" .md)"
    if [ ! -e "$link" ]; then
        rm "$link"
        ok "Removed stale: .claude/commands/${basename}.md"
        removed=$((removed + 1))
    fi
done
echo ""

# --- 5. Verify all symlinks resolve ---
echo "Verifying symlinks..."

verify_count=0
for link in "$CURSOR_RULES_DIR"/*.mdc "$CURSOR_COMMANDS_DIR"/*.mdc "$CLAUDE_RULES_DIR"/*.md "$CLAUDE_COMMANDS_DIR"/*.md; do
    [ -L "$link" ] || continue
    if [ -e "$link" ]; then
        verify_count=$((verify_count + 1))
    else
        err "Broken symlink: $link -> $(readlink "$link")"
    fi
done

for root_link in "$REPO_ROOT/CLAUDE.md"; do
    if [ -L "$root_link" ] && [ -e "$root_link" ]; then
        verify_count=$((verify_count + 1))
    elif [ -L "$root_link" ]; then
        err "Broken symlink: $root_link -> $(readlink "$root_link")"
    fi
done
echo ""

# --- 6. Summary ---
echo "=== Summary ==="
echo "  Created: $created"
echo "  Updated: $updated"
echo "  Removed: $removed"
echo "  Verified: $verify_count symlinks OK"
if [ $errors -gt 0 ]; then
    echo "  Errors: $errors"
    exit 1
else
    echo "  No errors."
fi

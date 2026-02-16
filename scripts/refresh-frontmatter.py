#!/usr/bin/env python3
"""Refresh computable front-matter fields in Markdown files.

Updates current_length and estimated_reading_time based on actual body word count.
Does not touch last_updated (semantic, not computed).

Usage:
    python scripts/refresh-frontmatter.py topics/ templates/
    python scripts/refresh-frontmatter.py topics/epistemic_debt/
"""

import sys
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml")
    sys.exit(1)

READING_WPM = 238


def _parse_frontmatter(filepath: Path) -> tuple[Optional[dict], str, str]:
    """Return (parsed YAML dict or None, raw front-matter, body) or (None, "", full_text)."""
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, "", text
    end = text.find("\n---", 3)
    if end == -1:
        return None, "", text
    raw = text[3:end].strip()
    body = text[end + 4 :]
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        return None, raw, body
    if not isinstance(data, dict):
        return None, raw, body
    return data, raw, body


def _count_body_words(body: str) -> int:
    """Count words in the Markdown body."""
    return len(body.split())


def _compute_reading_time(words: int) -> str:
    """Compute estimated_reading_time as '{N} min' at READING_WPM."""
    mins = max(1, round(words / READING_WPM))
    return f"{mins} min"


def _collect_md_files(paths: list[str]) -> list[Path]:
    """Given CLI paths (files or dirs), return sorted list of .md files."""
    files: list[Path] = []
    for p in paths:
        path = Path(p)
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        else:
            print(f"Skipping non-existent path: {p}", file=sys.stderr)
    return sorted(set(files))


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    paths = sys.argv[1:]
    md_files = _collect_md_files(paths)

    if not md_files:
        print("No .md files found in the specified paths.")
        return 0

    changed: list[Path] = []

    for filepath in md_files:
        data, raw_fm, body = _parse_frontmatter(filepath)
        if data is None:
            continue

        words = _count_body_words(body)
        new_length = words
        new_reading_time = _compute_reading_time(words)

        updated = False
        if data.get("current_length") != new_length:
            data["current_length"] = new_length
            updated = True
        if data.get("estimated_reading_time") != new_reading_time:
            data["estimated_reading_time"] = new_reading_time
            updated = True

        if not updated:
            continue

        # Re-serialize YAML and write back
        new_fm = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_fm.rstrip()}\n---\n{body}"
        filepath.write_text(new_content, encoding="utf-8")
        changed.append(filepath)

    for p in changed:
        print(f"Updated: {p}")

    if changed:
        print(f"\n{len(changed)} file(s) updated.")
    else:
        print("No files needed updates.")

    return 0


if __name__ == "__main__":
    sys.exit(main())

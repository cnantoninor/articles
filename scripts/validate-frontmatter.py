#!/usr/bin/env python3
"""Validate YAML front-matter in Markdown files.

Scans article files, templates, and any other Markdown files with YAML
front-matter.  Reports required/recommended/publication field checks,
value constraints, and consistency warnings.

Usage:
    python scripts/validate-frontmatter.py topics/ templates/
    python scripts/validate-frontmatter.py topics/epistemic_debt/
    python scripts/validate-frontmatter.py path/to/single-file.md
"""

import re
import sys
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VALID_STATUSES = {"draft", "review", "published"}
VALID_TYPES = {"article", "slides", "research"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PLACEHOLDER_DATE = "YYYY-MM-DD"

READING_WPM = 238
WORD_COUNT_TOLERANCE = 0.10  # warn if current_length differs by >10%
READING_TIME_RE = re.compile(r"^(\d+)\s*min", re.IGNORECASE)

SOCIAL_TEASER_KEYS = {"linkedin", "twitter", "instagram_caption", "substack_notes"}
SOCIAL_TEASERS_PLATFORMS = {"linkedin", "twitter", "instagram", "substack_notes"}

ARTICLE_REQUIRED = ["title", "status", "type"]
ARTICLE_RECOMMENDED = [
    "audience",
    "target_length",
    "current_length",
    "created",
    "last_updated",
    "estimated_reading_time",
]
ARTICLE_PUBLICATION = ["published_date", "publication_url", "social_teasers"]

# When status is published, these must all be present and filled (blocking error if not)
PUBLISHED_REQUIRED = ARTICLE_REQUIRED + ARTICLE_RECOMMENDED + ["published_date", "publication_url"]

DATE_FIELDS = ("created", "last_updated", "published_date")

TEASERS_TEMPLATE_KEYS = ["article", "article_url", "date_prepared", "platforms"]

# ANSI colour helpers
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _colour(text: str, colour: str) -> str:
    if not sys.stdout.isatty():
        return text
    return f"{colour}{text}{RESET}"


def _parse_frontmatter(filepath: Path):
    """Return parsed YAML dict or None if no front-matter block found."""
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    raw = text[3:end].strip()
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return {"__yaml_error__": str(exc)}
    if not isinstance(data, dict):
        return None
    return data


def _is_date(value) -> bool:
    return isinstance(value, str) and bool(DATE_RE.match(value))


def _is_placeholder_date(value) -> bool:
    return isinstance(value, str) and value == PLACEHOLDER_DATE


def _is_filled(data: dict, field: str) -> bool:
    """Return True if the field is present and has a valid non-empty value."""
    val = data.get(field)
    if val is None:
        return False
    if field in DATE_FIELDS:
        return _is_date(str(val)) and not _is_placeholder_date(str(val))
    if field == "audience":
        return isinstance(val, list) and len(val) > 0
    if field in ("target_length", "current_length"):
        return isinstance(val, (int, float))
    if field in ("publication_url", "title", "estimated_reading_time"):
        return isinstance(val, str) and val.strip() != ""
    if field in ("status", "type"):
        return True
    return bool(val)


def _count_body_words(filepath: Path) -> int:
    """Count words in the Markdown body (everything after front-matter)."""
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return len(text.split())
    end = text.find("\n---", 3)
    if end == -1:
        return len(text.split())
    body = text[end + 4:]
    return len(body.split())


def _parse_reading_time(value) -> Optional[int]:
    """Extract minutes from estimated_reading_time (e.g. '5 min' -> 5)."""
    if not isinstance(value, str):
        return None
    m = READING_TIME_RE.match(value.strip())
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------

class FileResult:
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.infos: list[str] = []

    def error(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    def info(self, msg: str):
        self.infos.append(msg)

    @property
    def status_label(self) -> str:
        if self.errors:
            return _colour("FAIL", RED)
        if self.warnings:
            return _colour("WARN", YELLOW)
        return _colour("PASS", GREEN)

    def print_report(self):
        rel = self.filepath
        print(f"\n{BOLD if sys.stdout.isatty() else ''}{rel}{RESET if sys.stdout.isatty() else ''}  [{self.status_label}]")
        for msg in self.errors:
            print(f"  {_colour('FAIL', RED)}: {msg}")
        for msg in self.warnings:
            print(f"  {_colour('WARN', YELLOW)}: {msg}")
        for msg in self.infos:
            print(f"  {_colour('INFO', CYAN)}: {msg}")


def _detect_file_kind(filepath: Path, data: dict) -> str:
    """Determine file kind: 'article', 'teaser_template', 'template', or 'other'."""
    parts = filepath.parts
    if filepath.name == "social-teasers.md" and "templates" in parts:
        return "teaser_template"
    if "templates" in parts:
        return "template"
    if data.get("type") in VALID_TYPES:
        return "article"
    if "topics" in parts:
        return "article"
    return "other"


def _validate_article(data: dict, result: FileResult):
    """Validate article front-matter."""
    for field in ARTICLE_REQUIRED:
        if field not in data:
            result.error(f"Missing required field: {field}")

    for field in ARTICLE_RECOMMENDED:
        if field not in data:
            result.warn(f"Missing recommended field: {field}")

    for field in ARTICLE_PUBLICATION:
        if field not in data:
            result.info(f"Missing publication field: {field} (expected empty when status is draft)")

    status = data.get("status")
    if status is not None and status not in VALID_STATUSES:
        result.error(f"Invalid status '{status}'; expected one of: {', '.join(sorted(VALID_STATUSES))}")

    ftype = data.get("type")
    if ftype is not None and ftype not in VALID_TYPES:
        result.error(f"Invalid type '{ftype}'; expected one of: {', '.join(sorted(VALID_TYPES))}")

    for date_field in ("created", "last_updated"):
        val = data.get(date_field)
        if val is not None:
            if _is_placeholder_date(val):
                result.info(f"Placeholder date in {date_field}: {val}")
            elif not _is_date(str(val)):
                result.error(f"Invalid date format for {date_field}: '{val}' (expected YYYY-MM-DD)")

    pub_date = data.get("published_date")
    if pub_date is not None and pub_date != "" and pub_date is not None:
        if _is_placeholder_date(str(pub_date)):
            result.info(f"Placeholder date in published_date: {pub_date}")
        elif not _is_date(str(pub_date)):
            result.error(f"Invalid date format for published_date: '{pub_date}' (expected YYYY-MM-DD)")

    # -- Word count and reading-time consistency --------------------------
    actual_words = _count_body_words(result.filepath)

    current_length = data.get("current_length")
    if current_length is not None and isinstance(current_length, (int, float)) and current_length > 0:
        diff_ratio = abs(actual_words - current_length) / current_length
        if diff_ratio > WORD_COUNT_TOLERANCE:
            result.warn(
                f"current_length ({current_length}) differs from actual "
                f"word count ({actual_words}) by {diff_ratio:.0%}"
            )

    reading_time = data.get("estimated_reading_time")
    if reading_time is not None:
        claimed_min = _parse_reading_time(reading_time)
        if claimed_min is not None and actual_words > 0:
            expected_min = max(1, round(actual_words / READING_WPM))
            if abs(claimed_min - expected_min) > 1:
                result.warn(
                    f"estimated_reading_time ('{reading_time}') appears inconsistent "
                    f"with actual word count ({actual_words} words "
                    f"\u2248 {expected_min} min at {READING_WPM} wpm)"
                )

    teasers = data.get("social_teasers")
    if teasers is not None and isinstance(teasers, dict):
        missing_keys = SOCIAL_TEASER_KEYS - set(teasers.keys())
        if missing_keys:
            result.warn(f"social_teasers missing keys: {', '.join(sorted(missing_keys))}")

    if status == "published":
        for field in PUBLISHED_REQUIRED:
            if not _is_filled(data, field):
                result.error(
                    f"Status is 'published' but required field '{field}' is missing or empty"
                )
        if teasers is None or not isinstance(teasers, dict):
            result.warn("Status is 'published' but social_teasers is missing")
        elif not all(teasers.get(k) for k in SOCIAL_TEASER_KEYS):
            empty = [k for k in SOCIAL_TEASER_KEYS if not teasers.get(k)]
            result.warn(
                f"Status is 'published' but social_teasers empty for: {', '.join(sorted(empty))}"
            )
        pub_date = data.get("published_date")
        last_up = data.get("last_updated")
        if (
            pub_date is not None
            and last_up is not None
            and _is_date(str(pub_date))
            and not _is_placeholder_date(str(pub_date))
            and _is_date(str(last_up))
            and not _is_placeholder_date(str(last_up))
        ):
            if str(pub_date) > str(last_up):
                result.warn(
                    f"published_date ({pub_date}) is after last_updated ({last_up})"
                )


def _validate_teaser_template(data: dict, result: FileResult):
    """Validate social-teasers.md template front-matter."""
    for field in TEASERS_TEMPLATE_KEYS:
        if field not in data:
            result.warn(f"Missing expected field: {field}")

    platforms = data.get("platforms")
    if platforms is not None:
        if isinstance(platforms, list):
            actual = set(platforms)
            missing = SOCIAL_TEASERS_PLATFORMS - actual
            if missing:
                result.warn(f"platforms list missing: {', '.join(sorted(missing))}")
        else:
            result.warn(f"platforms should be a list, got {type(platforms).__name__}")

    for field in ("article", "article_url", "date_prepared"):
        val = data.get(field)
        if val is not None and isinstance(val, str) and val == "":
            result.info(f"Placeholder value in {field} (expected in template)")

    date_prepared = data.get("date_prepared")
    if date_prepared is not None and isinstance(date_prepared, str):
        if _is_placeholder_date(date_prepared):
            result.info(f"Placeholder date in date_prepared: {date_prepared}")


def _validate_template(data: dict, result: FileResult):
    """Validate a generic template file (YAML syntax already confirmed)."""
    for key, val in data.items():
        if isinstance(val, str) and val == PLACEHOLDER_DATE:
            result.info(f"Placeholder date in {key}: {val}")
    result.info(f"Template front-matter fields: {', '.join(sorted(data.keys()))}")


def _validate_other(data: dict, result: FileResult):
    """Generic fallback -- report fields found."""
    result.info(f"Front-matter fields: {', '.join(sorted(data.keys()))}")


# ---------------------------------------------------------------------------
# File collection
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    paths = sys.argv[1:]
    md_files = _collect_md_files(paths)

    if not md_files:
        print("No .md files found in the specified paths.")
        sys.exit(0)

    results: list[FileResult] = []
    skipped = 0

    for filepath in md_files:
        data = _parse_frontmatter(filepath)
        if data is None:
            skipped += 1
            continue

        result = FileResult(filepath)

        if "__yaml_error__" in data:
            result.error(f"YAML parse error: {data['__yaml_error__']}")
            results.append(result)
            continue

        kind = _detect_file_kind(filepath, data)

        if kind == "article":
            _validate_article(data, result)
        elif kind == "teaser_template":
            _validate_teaser_template(data, result)
        elif kind == "template":
            _validate_template(data, result)
        else:
            _validate_other(data, result)

        results.append(result)

    # Print results
    print(f"\n{'=' * 60}")
    print("Front-matter Validation Report")
    print(f"{'=' * 60}")

    for r in results:
        r.print_report()

    # Summary
    total = len(results)
    passed = sum(1 for r in results if not r.errors and not r.warnings)
    warned = sum(1 for r in results if r.warnings and not r.errors)
    failed = sum(1 for r in results if r.errors)

    print(f"\n{'=' * 60}")
    print(f"Summary: {total} files scanned, {skipped} skipped (no front-matter)")
    print(f"  {_colour(f'{passed} PASS', GREEN)}  "
          f"{_colour(f'{warned} WARN', YELLOW)}  "
          f"{_colour(f'{failed} FAIL', RED)}")
    print(f"{'=' * 60}\n")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Ensure articles include an end-of-post call-to-action (CTA).

This is designed to run as part of the repo's pre-push checks.

Behavior:
- Scans Markdown files with YAML front-matter and `type: article`.
- If a CTA is missing near the end, inserts a standard CTA block.
- Comment/share links are added only when `publication_url` is present in front-matter.
  If `publication_url` is missing/empty, the CTA uses plain text for comment/share and a
  WARNING is printed to stderr.

Usage:
    python scripts/check-cta.py topics/
    python scripts/check-cta.py path/to/article.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


CTA_TAIL_WORDS = 350

CTA_KEYWORDS_ALL = ("subscribe",)
CTA_KEYWORDS_ANY = ("comment", "share", "restack")

SUBSCRIBE_URL = "https://antoninorau.substack.com/subscribe"

REFERENCES_MARKERS_RE = re.compile(
    r"(?m)^(##\s+References\s*$|\*\*References\*\*\s*$|__References__\s*$)"
)

CTA_BLOCK_RE = re.compile(
    r"\n\n---\n\n\*If you found this article valuable,[\s\S]*?"
    + re.escape(f"[subscribe]({SUBSCRIBE_URL})")
    + r"[\s\S]*?\*\n\n---\n",
    re.MULTILINE,
)


def _collect_md_files(paths: list[str]) -> list[Path]:
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


def _split_frontmatter(text: str) -> tuple[Optional[dict], str, str]:
    """Return (data, prefix, body).

    - data: parsed YAML dict, or None if no (valid) YAML front-matter.
    - prefix: everything up to and including the closing delimiter marker `\\n---`
      (but not including the newline after it). This is chosen to mirror the existing
      parsing style used elsewhere in the repo.
    - body: remainder of file after the closing delimiter marker.
    """
    if not text.startswith("---"):
        return None, "", text

    end = text.find("\n---", 3)
    if end == -1:
        return None, "", text

    raw = text[3:end].strip()
    body = text[end + 4 :]
    prefix = text[: end + 4]

    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        return None, prefix, body

    if not isinstance(data, dict):
        return None, prefix, body

    return data, prefix, body


def _tail_words(text: str, n: int) -> str:
    words = text.split()
    if len(words) <= n:
        return " ".join(words)
    return " ".join(words[-n:])

def _dedupe_cta_blocks(body: str) -> tuple[str, int]:
    """Remove duplicate CTA blocks inserted by this script.

    Returns (new_body, removed_count). Keeps the last CTA block when multiple exist.
    """
    matches = list(CTA_BLOCK_RE.finditer(body))
    if len(matches) <= 1:
        return body, 0

    remove_spans = [(m.start(), m.end()) for m in matches[:-1]]
    remove_spans.sort()

    out: list[str] = []
    idx = 0
    for start, end in remove_spans:
        if start < idx:
            continue
        out.append(body[idx:start])
        idx = end
    out.append(body[idx:])
    return "".join(out), len(remove_spans)


def _cta_probe_text(body: str) -> str:
    """Return the portion of the body where CTA is expected to be found.

    If a References marker exists, CTA is expected *before* References (since the
    reference list can be long and would otherwise push the CTA out of the tail window).
    """
    m = REFERENCES_MARKERS_RE.search(body)
    if not m:
        return body
    return body[: m.start()]

def _upgrade_cta_links(body: str, publication_url: Optional[str]) -> tuple[str, bool]:
    """If our CTA exists but lacks links, upgrade it when publication_url is present."""
    pub_url = (publication_url or "").strip()
    if not pub_url:
        return body, False

    post_url = pub_url.rstrip("/")

    def upgrade_block(match: re.Match[str]) -> str:
        block = match.group(0)
        if "[leave a comment](" in block or "[share it](" in block:
            return block
        return block.replace(
            "Please leave a comment, share it,",
            f"Please [leave a comment]({post_url}/comments), [share it]({post_url}),",
        )

    upgraded_body, n = CTA_BLOCK_RE.subn(upgrade_block, body)
    return upgraded_body, n > 0 and upgraded_body != body


def _has_cta(body: str) -> bool:
    probe = _cta_probe_text(body).lower()
    tail = _tail_words(probe, CTA_TAIL_WORDS)
    has_required = all(k in tail for k in CTA_KEYWORDS_ALL)
    has_any = any(k in tail for k in CTA_KEYWORDS_ANY)
    return has_required and has_any


def _build_cta(publication_url: Optional[str]) -> tuple[str, Optional[str]]:
    """Return (cta_block, warning_msg_or_none)."""
    subscribe = f"[subscribe]({SUBSCRIBE_URL})"

    pub_url = (publication_url or "").strip()
    if pub_url:
        post_url = pub_url.rstrip("/")
        # Substack exposes a dedicated discussion thread URL at `<post_url>/comments`.
        # This provides a direct link to the comment UI.
        comment = f"[leave a comment]({post_url}/comments)"
        share = f"[share it]({post_url})"
        warning = None
    else:
        comment = "leave a comment"
        share = "share it"
        warning = (
            "WARNING: Article missing publication_url - comment/share links not added to CTA"
        )

    cta_line = (
        "*If you found this article valuable, I'd love to hear your thoughts. "
        f"Please {comment}, {share}, and eventually {subscribe} to The AI Mirror "
        "for more explorations at the intersection of AI, software engineering and a bit of philosophy.*"
    )

    block = "\n\n---\n\n" + cta_line + "\n\n---\n"
    return block, warning


def _insert_cta(body: str, cta_block: str) -> str:
    """Insert CTA before references marker when present, else append at end."""
    m = REFERENCES_MARKERS_RE.search(body)
    if not m:
        if body.endswith("\n"):
            return body + cta_block
        return body + "\n" + cta_block

    insert_at = m.start()
    before = body[:insert_at]
    after = body[insert_at:]

    if not before.endswith("\n"):
        before += "\n"
    return before + cta_block + after


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
    missing_publication_url_for_cta: list[Path] = []

    for filepath in md_files:
        text = filepath.read_text(encoding="utf-8")
        data, prefix, body = _split_frontmatter(text)
        if data is None:
            continue

        if data.get("type") != "article":
            continue

        body, removed = _dedupe_cta_blocks(body)
        body, upgraded = _upgrade_cta_links(body, data.get("publication_url"))
        if removed or upgraded:
            filepath.write_text(prefix + body, encoding="utf-8")
            changed.append(filepath)
            print(f"Updated: {filepath}")

        if _has_cta(body):
            continue

        publication_url = data.get("publication_url")
        cta_block, warning = _build_cta(str(publication_url) if publication_url else None)
        if warning:
            missing_publication_url_for_cta.append(filepath)

        new_body = _insert_cta(body, cta_block)
        if new_body == body:
            continue

        filepath.write_text(prefix + new_body, encoding="utf-8")
        changed.append(filepath)
        print(f"Updated: {filepath}")

    if missing_publication_url_for_cta:
        count = len(missing_publication_url_for_cta)
        paths_preview = ", ".join(str(p) for p in missing_publication_url_for_cta[:5])
        more = "" if count <= 5 else f" (+{count - 5} more)"
        print(
            "WARNING: publication_url missing — CTA comment/share links were not added "
            f"for {count} article(s): {paths_preview}{more}",
            file=sys.stderr,
        )

    if changed:
        print(f"\n{len(changed)} file(s) updated.")
    else:
        print("No files needed updates.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


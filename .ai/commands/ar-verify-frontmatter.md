---
description: "Command: Verify and fix article frontmatter (status, dates, word counts, URLs) against Substack and local sources."
alwaysApply: false
---

# Frontmatter Verification

Verify all article frontmatter across topics/ against their sources of truth: Substack for published articles, local file content for unpublished ones.

## Prompt

Scan all article files under `topics/*/artifacts/articles/*.md` and verify their frontmatter fields are accurate. Use the Substack archive at https://antoninorau.substack.com/ as the source of truth for published articles.

### Fields to Verify

For **published** articles (fetched from Substack):

| Field | Source of Truth |
|-------|-----------------|
| `title` | Substack article title |
| `subtitle` | Substack article subtitle |
| `status` | Must be `published` |
| `publication_url` | Substack article URL (not the base URL) |
| `published_date` | Substack publication date |
| `current_length` | Substack word count (body only) |
| `estimated_reading_time` | Calculated from word count at ~250 wpm |

For **unpublished** articles (local file as source):

| Field | Source of Truth |
|-------|-----------------|
| `status` | Must NOT be `published` |
| `publication_url` | Must be empty string `''` |
| `published_date` | Must be `null` |
| `current_length` | Local word count (body only, excluding frontmatter) |
| `estimated_reading_time` | Calculated from local word count at ~250 wpm |

### Steps

1. **Discover** all article markdown files (skip non-article files like `*-latex-formulas.md`).
2. **Fetch** the Substack archive page to get the list of published articles and their URLs.
3. **For each published article**, fetch the Substack page and extract title, subtitle, date, and word count. Compare against frontmatter.
4. **For each unpublished article**, count words in the local file body (excluding YAML frontmatter). Compare against frontmatter.
5. **Report** a table of all discrepancies found.
6. **Ask** the user for confirmation before applying fixes.

### Output Format

```markdown
# Frontmatter Verification Report

## Discrepancies Found

| File | Field | Current Value | Correct Value |
|------|-------|---------------|---------------|
| ... | ... | ... | ... |

## No Issues
- [list of articles with no discrepancies]
```

If no discrepancies are found, report that all frontmatter is up to date.

---

## Example Invocation

> /ar-verify-frontmatter

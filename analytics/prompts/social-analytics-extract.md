# Social Media Analytics Extraction Prompt

Use this prompt with the Claude Chrome plugin when viewing social media post analytics (LinkedIn, Twitter/X, Instagram) to extract engagement metrics.

---

## Prompt

Look at this [LinkedIn / Twitter / Instagram] post analytics page. Extract the following metrics:

- Impressions
- Likes
- Comments
- Shares
- Link clicks (if available)

Format as a CSV row matching this schema (`analytics/data/manual/social_engagement.csv`):

```csv
date_posted,article_slug,platform,impressions,likes,comments,shares,link_clicks,notes
```

**Important notes:**
- Use the date the post was published (YYYY-MM-DD format)
- Extract `article_slug` from the Substack URL in the post: `https://antoninorau.substack.com/p/<slug>` → `<slug>`
- Set `platform` to: `linkedin`, `twitter`, or `instagram` (lowercase)
- If a metric is not available, use `0` or leave empty
- Add any relevant notes in the `notes` column (e.g., "Post went viral", "Low engagement")

---

## Usage

1. Open the analytics page for a specific social media post
2. Activate the Claude Chrome extension
3. Copy and paste this prompt (replace `[LinkedIn / Twitter / Instagram]` with the actual platform)
4. Copy Claude's CSV output
5. Append to `social_engagement.csv` using `ingest.py` or manually

Example:
```bash
# Paste Claude's output for social engagement
echo "2026-02-15,epistemic-debt-part-1,linkedin,1250,45,12,8,23,\"Strong engagement\"" | python analytics/scripts/ingest.py --target social_engagement
```

---

## Platform-Specific Notes

- **LinkedIn**: Analytics available in post dropdown → "Analytics"
- **Twitter/X**: Analytics available in post dropdown → "View post analytics" (may require Twitter Analytics account)
- **Instagram**: Analytics available in post → "View insights" (business/creator account required)

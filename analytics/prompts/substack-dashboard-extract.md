# Substack Dashboard Extraction Prompt

Use this prompt with the Claude Chrome plugin when viewing your Substack dashboard to extract subscriber and engagement metrics.

---

## Prompt

Look at this Substack dashboard. Extract ONLY the following metrics:

1. **Subscriber counts** (total, free, paid split)
2. **For each recent post** (last 4-6 posts):
   - Email open rate
   - Email click rate
   - Likes
   - Restacks
   - Comments

Format the output as CSV rows matching these schemas:

**For subscribers** (`analytics/data/manual/subscribers.csv`):
```csv
date,total_subscribers,free_subscribers,paid_subscribers,net_new,source_notes
```

**For email metrics** (`analytics/data/manual/email_metrics.csv`):
```csv
date_published,article_slug,emails_sent,opens,open_rate,clicks,click_rate
```

**For Substack engagement** (`analytics/data/manual/substack_engagement.csv`):
```csv
date_published,article_slug,likes,comments,restacks
```

**Important notes:**
- Use today's date (YYYY-MM-DD format) for the subscriber snapshot
- Extract `article_slug` from the Substack URL: `https://antoninorau.substack.com/p/<slug>` → `<slug>`
- Skip traffic/pageview data — that comes from GA4 automatically
- If a metric is not visible or unavailable, leave it empty

---

## Usage

1. Open your Substack dashboard: https://antoninorau.substack.com/
2. Activate the Claude Chrome extension
3. Copy and paste this prompt
4. Copy Claude's CSV output
5. Append to the appropriate CSV files using `ingest.py` or manually

Example:
```bash
# Paste Claude's output for subscribers
echo "2026-02-15,42,40,2,3,\"LinkedIn post drove 2 new subs\"" | python analytics/scripts/ingest.py --target subscribers
```

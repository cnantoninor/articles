# Weekly Analytics Collection Checklist

This checklist guides the weekly analytics data collection process. Most data is automated via GA4; only Substack-specific and social media metrics require manual collection (~5 minutes total).

**Time estimate:** ~5 minutes for semi-manual steps + ~30 seconds for automated steps

---

## Automated Collection (GA4)

### Step 1: Fetch GA4 Data

Run the automated fetch script to pull page views, traffic sources, referrals, and user behavior:

```bash
python analytics/scripts/fetch_ga4.py
```

**Options:**
- `--days N` - Fetch last N days (default: 7)
- `--start YYYY-MM-DD --end YYYY-MM-DD` - Custom date range
- `--replace` - Replace existing data instead of appending

**What this collects:**
- ✅ Page views per article
- ✅ Traffic sources (LinkedIn, Twitter, direct, organic search)
- ✅ Referral paths
- ✅ User behavior (bounce rate, session duration)
- ✅ Geographic and device breakdown

**Note:** GA4 data may have a 24-48 hour processing delay. For real-time data, use the GA4 MCP server in Cursor for conversational queries.

---

## Semi-Manual Collection (Substack + Social Media)

### Step 2: Substack Dashboard Metrics

**Time:** ~3 minutes

1. Open your Substack dashboard: https://antoninorau.substack.com/
2. Activate Claude Chrome extension
3. Use the prompt from [`analytics/prompts/substack-dashboard-extract.md`](prompts/substack-dashboard-extract.md)
4. Copy Claude's CSV output
5. Append to CSV files:

```bash
# Subscribers (weekly snapshot)
echo "DATE,SUBSCRIBERS_DATA" | python analytics/scripts/ingest.py --target subscribers

# Email metrics (per post)
echo "DATE_PUBLISHED,ARTICLE_SLUG,EMAIL_DATA" | python analytics/scripts/ingest.py --target email_metrics

# Substack engagement (per post)
echo "DATE_PUBLISHED,ARTICLE_SLUG,ENGAGEMENT_DATA" | python analytics/scripts/ingest.py --target substack_engagement
```

**What this collects:**
- ✅ Total subscribers (free/paid split)
- ✅ Email open rates and click rates per post
- ✅ Substack-native engagement (likes, restacks, comments)

**Article slug convention:** Extract from Substack URL:
- URL: `https://antoninorau.substack.com/p/my-article-title`
- Slug: `my-article-title` (strip `/p/` prefix)

---

### Step 3: Social Media Engagement

**Time:** ~2 minutes per platform

For each platform (LinkedIn, Twitter/X, Instagram):

1. Open the analytics page for recent posts
2. Activate Claude Chrome extension
3. Use the prompt from [`analytics/prompts/social-analytics-extract.md`](prompts/social-analytics-extract.md)
4. Copy Claude's CSV output
5. Append to social engagement CSV:

```bash
echo "DATE_POSTED,ARTICLE_SLUG,PLATFORM,ENGAGEMENT_DATA" | python analytics/scripts/ingest.py --target social_engagement
```

**What this collects:**
- ✅ Impressions
- ✅ Likes, comments, shares
- ✅ Link clicks

**Platforms:**
- LinkedIn: Post dropdown → "Analytics"
- Twitter/X: Post dropdown → "View post analytics" (may require Twitter Analytics)
- Instagram: Post → "View insights" (business/creator account required)

---

## Data Validation

### Step 4: Validate Manual Data

Before proceeding, validate the manually entered data:

```bash
# Dry run to check for errors
python analytics/scripts/ingest.py --target subscribers --dry-run < new_data.csv
```

The `ingest.py` script will:
- ✅ Validate column names and types
- ✅ Check for duplicate entries
- ✅ Report any errors before writing

---

## Generate Report

### Step 5: Merge and Analyze

Once all data is collected:

```bash
# Merge GA4 + manual data
python analytics/scripts/merge.py

# Generate weekly report
python analytics/scripts/report.py
```

Or use the convenience script:

```bash
./scripts/run-analytics.sh
```

The report will be written to `analytics/reports/weekly-YYYY-MM-DD.md`.

---

## Troubleshooting

### GA4 Fetch Fails

- **Error: Credentials not found**
  - Ensure `analytics/credentials/ga4-service-account.json` exists
  - See [`docs/mcp-setup.md`](../docs/mcp-setup.md) for setup instructions

- **Error: API quota exceeded**
  - GA4 has rate limits; wait a few minutes and retry
  - Consider reducing date range if fetching large datasets

### Manual Data Validation Fails

- **Error: Missing column**
  - Check CSV format matches schema exactly
  - See schema definitions in this checklist or in CSV headers

- **Error: Duplicate entry**
  - Check if data for this date/article already exists
  - Use `--replace` flag or manually edit CSV to update existing rows

### Claude Chrome Extraction Issues

- **Claude misreads numbers**
  - Manually verify extracted values against dashboard
  - Adjust prompt if needed (see `analytics/prompts/`)

- **Missing metrics**
  - Some metrics may not be visible in dashboard
  - Leave empty or use `0` as appropriate

---

## Calendar Reminder

Set a weekly calendar reminder (e.g., Sunday evening) to:
1. ✅ Run GA4 fetch
2. ✅ Collect Substack metrics
3. ✅ Collect social media metrics
4. ✅ Generate report
5. ✅ Review report and adjust strategy

---

## Quick Reference

| Task | Command | Time |
|------|---------|------|
| Fetch GA4 data | `python analytics/scripts/fetch_ga4.py` | ~30s |
| Validate manual data | `python analytics/scripts/ingest.py --target <type> --dry-run` | ~10s |
| Merge data | `python analytics/scripts/merge.py` | ~5s |
| Generate report | `python analytics/scripts/report.py` | ~5s |
| Full pipeline | `./scripts/run-analytics.sh` | ~1m |

**Total automated time:** ~1 minute  
**Total manual time:** ~5 minutes  
**Total weekly time:** ~6 minutes

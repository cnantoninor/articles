# Publishing Workflow

This document describes the end-to-end weekly process for publishing to **The AI Mirror** (Substack) and distributing to social channels. It is for the human author and for AI assistants that help draft, export, or cross-post.

**Related docs:** [MCP Server Setup](mcp-setup.md) (Substack, Crosspost, GA4) · [.ai/rules/publication.md](../.ai/rules/publication.md) (teaser conventions) · [templates/article.md](../templates/article.md) (front-matter) · [templates/social-teasers.md](../templates/social-teasers.md) (teaser drafting)

---

## Weekly Publishing Cycle

1. **Write and finalize** the article under `topics/<name>/artifacts/articles/` (flat layout; no `published/` subdir). Use the article template; keep front-matter and body in sync. Publication state lives in frontmatter (`status`, `published_date`, `publication_url`).
2. **Export** formats (e.g. HTML/Markdown for Substack) with:
   ```bash
   ./scripts/export-all.sh <topic_name>
   ```
3. **Push draft to Substack**  
   - **MCP:** Use the Substack MCP tool `create_draft_post(title, subtitle, body)` with exported content.  
   - **Fallback:** Copy-paste from the exported file into a new Substack post in the dashboard.  
   - If the MCP fails (e.g. auth/session expired), re-extract credentials per [mcp-setup.md](mcp-setup.md) or use the manual paste method.
4. **Review and publish** in the Substack editor. Add cover image, adjust formatting, then publish. Fill in `publication_url` and `published_date` in the article's front-matter.
5. **Generate social teasers** using [templates/social-teasers.md](../templates/social-teasers.md). Draft platform-specific copy; copy final text into the article's `social_teasers` block (linkedin, twitter, instagram_caption, substack_notes).
6. **Distribute**
   - **LinkedIn & Twitter/X:** Crosspost MCP (if configured) or manual post with teaser + link.
   - **Instagram:** Manual only (no MCP support). Use caption from template; add visual or quote card; CTA to link in bio.
   - **Substack Notes:** Post the Substack Notes teaser manually from the Substack dashboard to leverage native discovery.

---

## Workflow Overview

```mermaid
flowchart TD
    subgraph publish [Weekly Publish Flow]
        Write[Write Article] --> Review[Review Draft]
        Review --> Export[Export Formats]
        Export --> SubstackDraft[Push to Substack Draft]
        SubstackDraft --> PublishStep[Review and Publish]
    end

    subgraph distribute [Distribution]
        PublishStep --> Teasers[Generate Social Teasers]
        Teasers --> LinkedIn[Post LinkedIn]
        Teasers --> Twitter[Post Twitter]
        Teasers --> Instagram[Create Instagram Visual]
        PublishStep --> Notes[Post Substack Notes]
    end

    subgraph analytics [Weekly Analytics Cycle]
        GA4[GA4 API Auto Fetch] --> Merge[Merge Data Sources]
        Calendar[Calendar Reminder] --> Dashboard[Substack Dashboard]
        Dashboard --> ChromePlugin[Claude Chrome Extract]
        ChromePlugin --> ManualCSV[Append Manual CSV]
        ManualCSV --> Merge
        Merge --> Scripts[Run Python Analysis]
        Scripts --> Report[Growth Report]
        Report --> Adjust[Adjust Strategy]
    end

    distribute --> Calendar
    Adjust --> Write
```

---

## Analytics Cycle

The analytics system combines automated GA4 data collection with semi-manual Substack and social media metrics.

### Automated Collection

Run the GA4 fetch script weekly to pull page views, traffic sources, referrals, and user behavior:

```bash
python analytics/scripts/fetch_ga4.py
```

Or use the convenience script for the full pipeline:

```bash
./scripts/run-analytics.sh
```

**What's automated:**
- Page views per article
- Traffic sources (LinkedIn, Twitter, direct, organic search)
- Referral paths
- User behavior (bounce rate, session duration)
- Geographic and device breakdown

### Semi-Manual Collection

Weekly calendar reminder to collect Substack-specific and social media metrics (~5 minutes):

1. **Substack dashboard** — Use Claude Chrome plugin with prompts from [`analytics/prompts/substack-dashboard-extract.md`](../analytics/prompts/substack-dashboard-extract.md) to extract:
   - Subscriber counts (total, free, paid)
   - Email open/click rates per post
   - Substack-native engagement (likes, restacks, comments)

2. **Social media analytics** — Use prompts from [`analytics/prompts/social-analytics-extract.md`](../analytics/prompts/social-analytics-extract.md) to extract:
   - Impressions, likes, comments, shares, link clicks per platform

3. **Validate and append** — Use `ingest.py` to validate and append manual data:

```bash
python analytics/scripts/ingest.py --target subscribers < data.csv
```

### Generate Report

After collecting all data, generate the weekly report:

```bash
python analytics/scripts/report.py
```

The report includes:
- Subscriber growth summary and projection to 100 subscribers
- Traffic breakdown by channel
- Top performing articles
- Week-over-week changes
- Actionable recommendations

**Full workflow:** See [`analytics/COLLECTION-CHECKLIST.md`](../analytics/COLLECTION-CHECKLIST.md) for the complete weekly checklist.

**Setup:** GA4 credentials and MCP configuration are documented in [mcp-setup.md](mcp-setup.md).

---

## Growth Playbook

Flexible guidelines to support growth over time. Adopt what fits your cadence; adjust as you learn what works.

- **Substack Notes** — Post regularly (e.g. daily or several times per week) for organic discovery. Short teasers, links to articles, and genuine engagement with other writers’ notes help visibility.
- **Niche engagement** — Engage with writers in the AI / philosophy / spirituality space: read, comment, restack. Relationship-driven growth doesn’t scale via automation but does build a real audience.
- **Substack Recommendations** — Enable Recommendations for your publication and add cross-recommendation partners. Rotate or refresh partners periodically so more readers discover you.
- **Provocative hooks** — Use each article’s most surprising or provocative claim as the social hook (especially Twitter/X and LinkedIn). Exploratory tone still allows a strong opening line.
- **Experiment and track** — Try different teaser formats, lengths, and hashtags. Once Phase 5 analytics are in place, compare which channels and formats correlate with traffic and new subscribers; double down on what works.

---

## LinkedIn Engagement Automation

Automated weekly scan that finds LinkedIn posts relevant to your published articles and generates engagement opportunities.

**How it works:** The Claude Chrome extension runs a saved prompt on a weekly schedule that:
1. Reads your Substack RSS feed to build an article matching profile
2. Scrolls your LinkedIn feed and scores posts against your articles (1=weak, 2=medium, 3=strong)
3. Checks your recent LinkedIn activity to avoid duplicate engagement
4. Drafts contextual comments for each matched post
5. Composes a Gmail draft report with all matches, rationale, scores, and draft comments
6. Tracks state (last run date) via a Google Keep note

**Setup:**
1. Create a pinned Google Keep note titled `LINKEDIN_SCAN_STATE` with content: `last_run_date: YYYY-MM-DD`
2. Save the prompt from [`analytics/prompts/linkedin-engagement-scan.md`](../analytics/prompts/linkedin-engagement-scan.md) as a Claude Chrome extension shortcut
3. Replace `[YOUR_EMAIL]` in the prompt with your email address
4. Schedule the shortcut to run weekly (Monday mornings recommended)

**Using the report:** Check Gmail Drafts after each run. Prioritize score 3 matches for same-day engagement. Adjust draft comments to your voice before posting.

---

## References

| Resource | Purpose |
|----------|---------|
| [docs/mcp-setup.md](mcp-setup.md) | Substack, Crosspost, and GA4 MCP setup; credential extraction; semi-manual collection |
| [.ai/rules/publication.md](../.ai/rules/publication.md) | Publication target, social channels, platform-specific teaser conventions |
| [templates/article.md](../templates/article.md) | Article front-matter (including `social_teasers`, `publication_url`, `published_date`) |
| [templates/social-teasers.md](../templates/social-teasers.md) | Teaser drafting template with examples and fill-in blocks |
| [analytics/prompts/linkedin-engagement-scan.md](../analytics/prompts/linkedin-engagement-scan.md) | Claude Chrome extension prompt for weekly LinkedIn engagement scan |

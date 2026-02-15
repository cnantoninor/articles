# MCP Server Setup Guide

This guide covers configuration of the three MCP (Model Context Protocol) servers used for The AI Mirror publication workflow: **Substack** (draft creation), **Crosspost** (social media), and **Google Analytics 4** (analytics). The real config file `.mcp.json` and credentials are gitignored; use `.mcp.json.example` in the repo root as a template.

**Prerequisites**: Node.js and NPX for Substack and Crosspost; Python 3.10+ for GA4 MCP.

---

## 1. Substack MCP (`marcomoauro/substack-mcp`)

### What it does

- Exposes a single tool: **`create_draft_post(title, subtitle, body)`**
- Uses a reverse-engineered Substack API (Substack has no official public API)
- Creates drafts only; you review and publish manually in the Substack editor (by design)
- Works with Cursor, Claude Desktop, and other MCP clients

### Prerequisites

- Node.js and NPX installed

### Credential extraction

Substack MCP needs three values, all from your logged-in Substack session:

1. **Log into Substack** in your browser (your publication: https://antoninorau.substack.com/).

2. **Session token**  
   - Open DevTools (F12) → **Application** (Chrome) or **Storage** (Firefox) → **Cookies** → select your Substack domain  
   - Find the cookie named **`substack.sid`** and copy its **Value**.  
   - This is `SUBSTACK_SESSION_TOKEN`.

3. **Publication URL**  
   - Your publication URL, e.g. `https://antoninorau.substack.com`  
   - No trailing slash. This is `SUBSTACK_PUBLICATION_URL`.

4. **User ID**  
   - With DevTools open, go to **Network** and refresh the Substack dashboard or open your publication settings  
   - Find a request to the Substack API that returns JSON containing your user/profile id (often under a key like `user_id` or `id` in the response body)  
   - Copy that numeric id. This is `SUBSTACK_USER_ID`.  
   - Alternatively, some MCP docs suggest the session or dashboard HTML may expose it; check the Substack MCP repo README for the current method.

### Security warning

The session token grants full access to your Substack account. **Never commit it to git.** Keep it only in `.mcp.json` (gitignored) or in environment variables. Rotate it if you suspect exposure.

### Known limitations

- **Draft-only**: Final publish is always done manually in Substack (intended).
- **Token lifetime**: [UNKNOWN] — session cookies may expire after hours or months; re-extract if the MCP starts failing with auth errors.
- **Unofficial API**: Substack can change internal APIs at any time; the MCP may break until the package is updated.

### Config block for `.mcp.json`

```json
"substack-api": {
  "command": "npx",
  "args": ["-y", "substack-mcp@latest"],
  "env": {
    "SUBSTACK_PUBLICATION_URL": "https://antoninorau.substack.com",
    "SUBSTACK_SESSION_TOKEN": "YOUR_SUBSTACK_SID_COOKIE_VALUE",
    "SUBSTACK_USER_ID": "YOUR_USER_ID"
  }
}
```

---

## 2. Crosspost MCP (`@humanwhocodes/crosspost`)

### What it does

- Posts text (and images: PNG, JPEG, GIF) to multiple social platforms from one MCP tool
- **Primary platforms for this workflow**: Twitter/X (`-t`), LinkedIn (`-l`)
- **Other supported platforms** (documented for future use): Mastodon, Bluesky, Discord, Dev.to
- **Instagram**: Not supported. Use manual posting or a paid API (e.g. Later) if you need automation.

### Prerequisites

- Node.js and NPX installed
- API credentials for each platform you enable

### Platform credential setup

- **Twitter/X**  
  - Create a project and app in the [Twitter Developer Portal](https://developer.twitter.com/)  
  - Obtain: API Key, API Secret, Access Token, Access Token Secret  
  - **Note**: The free tier may not include write/posting access; check current [Twitter API pricing](https://developer.twitter.com/en/products/twitter-api) (Basic tier is paid).

- **LinkedIn**  
  - Create an app in [LinkedIn Developer Portal](https://www.linkedin.com/developers/)  
  - Request the required OAuth scopes for posting (e.g. `w_member_social`)  
  - **Note**: Posting via API often requires app review; approval can take days or weeks.

Credentials are loaded from a `.env` file; path is passed via `CROSSPOST_DOTENV`. Never commit `.env`.

### `.env` structure (example)

Variable names and format should be confirmed from the [Crosspost package documentation](https://www.npmjs.com/package/@humanwhocodes/crosspost) at configuration time. Typical pattern:

```bash
# Twitter/X
TWITTER_API_KEY=...
TWITTER_API_SECRET=...
TWITTER_ACCESS_TOKEN=...
TWITTER_ACCESS_TOKEN_SECRET=...

# LinkedIn (OAuth or app credentials as required by the package)
LINKEDIN_CLIENT_ID=...
LINKEDIN_CLIENT_SECRET=...
# ... (see package docs for exact vars)
```

### Config block for `.mcp.json`

Use the path to your **absolute** `.env` path (e.g. in the repo root or a secure location):

```json
"crosspost": {
  "command": "npx",
  "args": ["@humanwhocodes/crosspost", "-t", "-l", "--mcp"],
  "env": {
    "CROSSPOST_DOTENV": "/absolute/path/to/your/.env"
  }
}
```

To add more platforms later (e.g. Bluesky, Mastodon), check the package docs for the correct flags and env vars.

### Instagram workaround

Crosspost does not support Instagram. Options: post Instagram content manually, or use a third-party service (e.g. Later) with an API; document your chosen approach in your workflow.

---

## 3. Google Analytics 4 MCP

GA4 MCP lets you ask natural-language questions in Cursor (e.g. “What were the top referral sources this week?”) and get answers from your GA4 data. Two implementations are available; document both and choose one when configuring.

### Option A: Official Google (`googleanalytics/google-analytics-mcp`)

- **Status**: Experimental
- **Pros**: Official, likely better long-term support
- **Install**: Clone or run from the [GitHub repo](https://github.com/googleanalytics/google-analytics-mcp); see repo for run instructions (often `python -m` or similar)
- **Config**: Property ID and `GOOGLE_APPLICATION_CREDENTIALS` path to the service account JSON

### Option B: Community PyPI (`google-analytics-mcp`)

- **Status**: Production/stable (e.g. v2.0.0)
- **Pros**: Smart context-window management, 200+ dimensions/metrics
- **Install**: `pip install google-analytics-mcp`
- **Run**: `python -m google_analytics_mcp` (confirm module name in [PyPI](https://pypi.org/project/google-analytics-mcp/))
- **Config**: Same as above: property ID and credentials path

### Prerequisites

- Python 3.10+
- A GCP project and GA4 property (this repo uses property ID `361268692`)

### GA4 setup walkthrough

1. **GCP project**  
   Create a project in [Google Cloud Console](https://console.cloud.google.com/) or use an existing one.

2. **Enable GA4 Data API**  
   In the same project: APIs & Services → Enable APIs → enable **Google Analytics Data API**.

3. **Service account**  
   Create a service account (e.g. “ga4-mcp”) and download its JSON key. Do not commit this file.

4. **Grant access to GA4**  
   In [Google Analytics](https://analytics.google.com/) → Admin → Property → Property access management, add the service account email with **Viewer** (or read-only) role so it can read reporting data for property `361268692`.

5. **Credentials path**  
   Place the JSON key in `analytics/credentials/` (e.g. `analytics/credentials/ga4-service-account.json`). This directory is gitignored. Set `GOOGLE_APPLICATION_CREDENTIALS` to the **absolute** path of this file.

### Config block for `.mcp.json`

Use an absolute path for the credentials file:

```json
"google-analytics": {
  "command": "python",
  "args": ["-m", "google_analytics_mcp"],
  "env": {
    "GA4_PROPERTY_ID": "361268692",
    "GOOGLE_APPLICATION_CREDENTIALS": "/absolute/path/to/analytics/credentials/ga4-service-account.json"
  }
}
```

For the **official** Google server, the module name in `args` may differ; check the repo.

### Example natural-language queries

- “Show traffic sources for the last 7 days.”
- “Which articles had the most views this month?”
- “What were the top referral sources this week?”

### Data processing lag

GA4 batch reporting can have a 24–48 hour delay. Real-time reports via the MCP may show fresher data for recent activity. Plan weekly reporting with this lag in mind.

---

## 4. Semi-Manual Data Collection

GA4 MCP and scripts cover a large share of analytics (page views, traffic sources, referrals, behavior). The following still need manual or semi-manual collection.

### What GA4 covers (automated)

- Page views, sessions, unique users per article
- Traffic sources (LinkedIn, Twitter, direct, organic search, etc.)
- Referral paths and user behavior (bounce rate, session duration, scroll depth)
- Geographic and device breakdown
- Real-time traffic (via MCP or GA4 UI)

### What still needs manual collection

- Substack subscriber counts (total, free, paid)
- Email open and click rates (Substack dashboard)
- Substack-native engagement (likes, restacks, comments)
- Social post engagement (likes, comments, shares on LinkedIn/Twitter/Instagram)

### Three-tier approach

1. **Tier 1 — Calendar + checklist**  
   Weekly reminder (e.g. Sunday) to open the Substack dashboard and a short checklist of only the metrics GA4 does not provide (~3 minutes).

2. **Tier 2 — Claude Chrome plugin**  
   Open the Substack dashboard (and social analytics pages) in Chrome, use the Claude extension with a saved prompt that asks Claude to extract the needed numbers and format them as CSV-ready rows. You paste/append into the repo’s CSV files. Same idea for LinkedIn/Twitter post analytics.

3. **Tier 3 — Browser-use MCP (optional)**  
   Full browser automation from Cursor; more fragile, use as an option rather than the primary path.

### Claude Chrome plugin saved prompts

**Substack dashboard**

> Look at this Substack dashboard. Extract ONLY: total subscribers (free/paid split), and for each recent post: email open rate, click rate, likes, restacks, comments. Format as CSV rows matching the schemas in this repo’s analytics docs (subscribers.csv, email_metrics.csv, substack_engagement.csv). Skip traffic/pageview data — that comes from GA4.

**Social media (per platform)**

> Look at this [LinkedIn / Twitter] post analytics. Extract: impressions, likes, comments, shares, link clicks. Format as a CSV row: date_posted, article_slug, platform, impressions, likes, comments, shares, link_clicks, notes.

### Weekly time estimate

About **5 minutes** for the semi-manual steps once the checklist and prompts are in place; GA4 and scripts handle the rest.

---

## File reference

| Item                    | Location                    | Gitignored |
|-------------------------|----------------------------|------------|
| MCP config              | `.mcp.json` (repo root)     | Yes        |
| Config template         | `.mcp.json.example`        | No         |
| Social / Crosspost keys | `.env` (repo root or safe path) | Yes   |
| GA4 credentials         | `analytics/credentials/*.json` | Yes   |
| Setup guide             | `docs/mcp-setup.md`        | No         |

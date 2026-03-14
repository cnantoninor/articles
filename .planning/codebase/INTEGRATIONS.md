# External Integrations

**Analysis Date:** 2026-03-14

## APIs & External Services

**Content Publishing:**
- Substack - Publishing platform for articles
  - SDK/Client: `substack-mcp` (via MCP server)
  - Auth: `SUBSTACK_SESSION_TOKEN` (SID cookie), `SUBSTACK_USER_ID`
  - Configuration: `.mcp.json` (example: `.mcp.json.example`)
  - Usage: Draft post creation via `create_draft_post()` MCP tool
  - Entry point: `analytics/scripts/fetch_ga4.py` references Substack property 361268692

**Social Media Distribution:**
- LinkedIn - Professional network sharing
  - SDK/Client: `@humanwhocodes/crosspost` (via MCP server)
  - Auth: Token in `CROSSPOST_DOTENV` environment file
  - Usage: Cross-posting via MCP; manual fallback available

- Twitter/X - Microblogging and engagement
  - SDK/Client: `@humanwhocodes/crosspost` (via MCP server)
  - Auth: Token in `CROSSPOST_DOTENV` environment file
  - Usage: Cross-posting via MCP; manual fallback available

- Instagram - Visual content sharing
  - Integration: Manual only (no MCP support)
  - Auth: Browser-based login
  - Usage: Direct post creation with captions and hashtags

**Analytics & Measurement:**
- Google Analytics 4 - Web analytics and user behavior tracking
  - SDK/Client: `google-analytics-data` (BetaAnalyticsDataClient)
  - Auth: GCP service account JSON at `analytics/credentials/ga4-service-account.json`
  - Property ID: 361268692 (configured in `GA4_PROPERTY_ID`)
  - Usage: `analytics/scripts/fetch_ga4.py` fetches:
    - Page views, sessions, average session duration per article
    - Traffic sources (session source/medium), new/returning users, bounce rate
    - Referral paths and full page URLs
    - User behavior metrics (bounce rate, average session duration)
  - Output: CSV files in `analytics/data/ga4/` (pageviews.csv, traffic_sources.csv, referrals.csv, user_behavior.csv)

## Data Storage

**Databases:**
- None configured (stateless content and analytics collection system)

**File Storage:**
- Local filesystem only
  - Analytics data: CSV files in `analytics/data/ga4/`
  - Article content: Markdown files in `topics/<topic_name>/`
  - Exported artifacts: PDF, HTML in `topics/<topic_name>/exports/`

**Caching:**
- None configured

## Authentication & Identity

**Auth Providers:**
- GCP Service Account - For Google Analytics API access
  - Implementation: File-based credential at `analytics/credentials/ga4-service-account.json`
  - Configured via `GOOGLE_APPLICATION_CREDENTIALS` environment variable
  - Used by: `google.analytics.data_v1beta.BetaAnalyticsDataClient`

- Substack Session Token - For Substack API integration
  - Implementation: Browser session cookie (SID)
  - Configured in `.mcp.json` via `SUBSTACK_SESSION_TOKEN`
  - Used by: `substack-mcp` MCP server for draft creation

- Crosspost Token - For LinkedIn/Twitter cross-posting
  - Implementation: API token file reference
  - Configured in `.mcp.json` via `CROSSPOST_DOTENV`
  - Used by: `@humanwhocodes/crosspost` MCP server

- GitHub Personal Access Token - For GitHub API integration
  - Implementation: PAT token
  - Configured in `.mcp.json` via `GITHUB_PERSONAL_ACCESS_TOKEN`
  - Used by: `@modelcontextprotocol/server-github` MCP server

## Monitoring & Observability

**Error Tracking:**
- None detected

**Logs:**
- Console output from Python scripts and Node.js utilities
- Analytics collection logs: `analytics/scripts/fetch_ga4.py` prints status to stdout
- Export progress: `scripts/styles/export-pdf.js` prints file size and status to stdout

## CI/CD & Deployment

**Hosting:**
- Vercel - Deployment platform for Next.js infographics
  - Current deployment: `https://articles-4d5hts7kg-cnantoninors-projects.vercel.app/` (article-2 infographics)
  - Configuration: Vercel auto-detects Next.js; supports one-click deploy from GitHub or Vercel CLI

**CI Pipeline:**
- GitHub Actions - Python test automation
  - Workflow file: `.github/workflows/python-tests.yml`
  - Trigger: Push to main branch, pull requests to main
  - Actions:
    - Checkout code
    - Setup Python 3.12 (GA uses 3.12; local development uses 3.13)
    - Install dependencies from `requirements-dev.txt`
    - Run pytest on test paths defined in `pytest.ini`

## Environment Configuration

**Required env vars:**
- `GOOGLE_APPLICATION_CREDENTIALS` - Path to GCP service account JSON (default: `analytics/credentials/ga4-service-account.json`)
- `GA4_PROPERTY_ID` - GA4 property ID (default: 361268692)
- `SUBSTACK_PUBLICATION_URL` - Substack publication URL (e.g., https://antoninorau.substack.com)
- `SUBSTACK_SESSION_TOKEN` - Substack SID cookie from authenticated session
- `SUBSTACK_USER_ID` - Substack user ID (numeric)
- `CROSSPOST_DOTENV` - Absolute path to .env file with crosspost credentials
- `GITHUB_PERSONAL_ACCESS_TOKEN` - GitHub PAT for GitHub API access

**Secrets location:**
- GCP credentials: `analytics/credentials/ga4-service-account.json` (git-ignored)
- Substack/Crosspost tokens: In `.mcp.json` (git-ignored; example template in `.mcp.json.example`)
- All secrets are listed in `.gitignore`

## Webhooks & Callbacks

**Incoming:**
- None detected

**Outgoing:**
- Substack draft creation - Called by `substack-mcp` MCP server when publishing workflow creates drafts
- GitHub webhook - Triggered by push/PR events to run CI tests

---

*Integration audit: 2026-03-14*

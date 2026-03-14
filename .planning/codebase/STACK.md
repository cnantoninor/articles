# Technology Stack

**Analysis Date:** 2026-03-14

## Languages

**Primary:**
- Python 3.13 - Analytics, content validation, PDF export tooling
- JavaScript (Node.js) - PDF export engine, MCP servers, Vercel deployment
- Markdown - Article content, slides (Marp format)

**Secondary:**
- YAML - Front-matter metadata for articles
- CSS - PDF styling for exported documents
- HTML - PDF generation via Puppeteer

## Runtime

**Environment:**
- Python 3.13 (specified in `pyproject.toml` and `.python-version`)
- Node.js (via npm packages)

**Package Manager:**
- npm (for Node.js dependencies)
  - Lockfile: `package-lock.json` present
- pip (for Python dependencies)
  - Requirements: `requirements.txt` and `requirements-dev.txt`

## Frameworks

**Core:**
- No web framework (primarily content and tooling focused)
- Next.js (v13+) - For interactive infographics deployment to Vercel (optional, article-2 infographics only)

**Testing:**
- pytest - Python testing framework
- Test location: `topics/ai_craft/code/vibe_designing` and `topics/ai_craft/code/ship_of_theseus`
- Config: `pytest.ini`

**Build/Dev:**
- Puppeteer - Headless browser for PDF generation from HTML
- markdown-it - Markdown parser and renderer
- markdown-it-footnote - Footnote support for markdown rendering

## Key Dependencies

**Critical:**
- `puppeteer` (v23.0.0) - High-quality PDF export from HTML with footnote support
- `markdown-it` (v14.0.0) - Core markdown rendering for PDF export
- `markdown-it-footnote` (v4.0.0) - Enables footnote syntax in exported content
- `google-analytics-data` (v0.20.0) - GA4 API client for analytics collection

**Infrastructure:**
- `pyyaml` (v6.0.3) - YAML parsing for front-matter validation and refresh
- `pandas` (v3.0.0+) - Data analysis for analytics pipeline
- `numpy` (v2.4.2) - Numerical computing for analytics
- `scipy` (v1.17.0) - Scientific computing for analytics
- `matplotlib` (v3.10.8) - Data visualization for analytics reports

## Configuration

**Environment:**
- Credentials: `analytics/credentials/ga4-service-account.json` (GCP service account for Google Analytics)
- Environment variables (optional):
  - `GOOGLE_APPLICATION_CREDENTIALS` - Path to GA4 service account JSON
  - `GA4_PROPERTY_ID` - GA4 property ID (default: 361268692)
- MCP servers configured in `.mcp.json` (example template: `.mcp.json.example`)

**Build:**
- `Makefile` - Installation, pre-push checks, validation
- `.github/workflows/python-tests.yml` - Python test automation on push/PR
- `scripts/styles/export-pdf.js` - PDF export entry point
- Script locations:
  - `scripts/styles/export-pdf.js` - PDF generation
  - `scripts/validate-frontmatter.py` - Front-matter validation
  - `scripts/refresh-frontmatter.py` - Front-matter updates
  - `scripts/check-cta.py` - Content validation
  - `analytics/scripts/fetch_ga4.py` - GA4 data collection
  - `analytics/scripts/report.py` - Analytics reporting

## Platform Requirements

**Development:**
- Python 3.13
- Node.js (version unspecified, but npm required)
- Git for version control
- Pre-push hook support for validation

**Production:**
- Vercel - Deployment target for interactive infographics (Next.js applications)
- GitHub Actions - Runs Python tests on push/PR to main branch
- Google Cloud Platform - GA4 service account for analytics data access

---

*Stack analysis: 2026-03-14*

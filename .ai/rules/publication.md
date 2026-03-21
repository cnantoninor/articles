---
globs: topics/**/artifacts/**
paths: topics/**/artifacts/**
description: "Publication workflow, social media distribution, and teaser conventions"
alwaysApply: false
---

# Publication & Distribution

## Primary Platform

- **Name**: The AI Mirror
- **Platform**: Substack
- **URL**: https://antoninorau.substack.com/
- **Tagline**: AI, philosophy, and spirituality
- **Cadence**: Weekly
- **Subscribers**: 26-50 (goal: 100)

## Article CTA Footer

Every article ends with a standard CTA paragraph before References. The subscribe link must always read `[subscribe for **free**](https://antoninorau.substack.com/subscribe)` — never just `[subscribe](...)`.

## Social Media Channels

- **LinkedIn**: https://www.linkedin.com/in/antoninorau/
- **Twitter/X**: https://x.com/antoninorau
- **Instagram**: https://www.instagram.com/eckardius_/
- **Substack Notes**: Native short-form posting on Substack

## Platform-Specific Teaser Conventions

### LinkedIn
- Professional framing with industry relevance
- 1-3 short paragraphs, ending with a question or call to read
- Use relevant hashtags sparingly (3-5 max)
- Tone: thoughtful and accessible, matching the exploratory writing style

### Twitter/X
- Hook + insight format (1-2 tweets max)
- Lead with the most provocative or surprising claim
- End with a link to the full article
- Tone: concise, punchy, but still exploratory

### Instagram
- Visual-first: pair with a relevant image or quote card
- Caption: 2-3 sentences summarizing the core insight
- Use relevant hashtags (10-15 in first comment)
- Tone: accessible, slightly more casual

### Substack Notes
- Brief teaser (2-3 sentences) with a direct link
- Leverage Substack's native discovery for organic reach
- Tone: matches the article's exploratory voice

## Distribution Workflow

The full weekly workflow (write → export → publish → distribute → analytics) is documented in **[docs/publishing-workflow.md](../../docs/publishing-workflow.md)**. In short:

1. **Publish** article on Substack
2. **Create teasers** for each platform (see conventions above; use [templates/social-teasers.md](../../templates/social-teasers.md))
3. **Cross-post** teasers to LinkedIn, Twitter/X, Instagram, Substack Notes
4. **Monitor** engagement and adjust cadence/format

## MCP Servers (Phase 2)

MCP servers for Substack drafting, social cross-posting, and GA4 analytics are documented in **[docs/mcp-setup.md](../../docs/mcp-setup.md)**. Use that guide for credential extraction, config templates (`.mcp.json.example`), and semi-manual data collection.

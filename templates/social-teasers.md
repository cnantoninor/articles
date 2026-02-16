---
article: ''
article_url: ''
date_prepared: YYYY-MM-DD
platforms:
- linkedin
- twitter
- instagram
- substack_notes
current_length: 657
estimated_reading_time: 3 min
---


# Social Teasers

Use this template to draft platform-specific teasers when promoting an article. Conventions below are summarized; the authoritative source is [.ai/rules/publication.md](.ai/rules/publication.md). When done, copy the final text into the article's YAML `social_teasers` block in its front-matter.

---

## Conventions at a glance

| Platform      | Tone              | Format                          | Hashtags   |
|---------------|-------------------|----------------------------------|------------|
| LinkedIn      | Professional, thoughtful | 1–3 short paragraphs, CTA or question | 3–5 max    |
| Twitter/X     | Concise, punchy   | Hook + insight, 1–2 tweets, link | As needed  |
| Instagram     | Accessible, casual| Caption 2–3 sentences + visual  | 10–15 in first comment |
| Substack Notes| Exploratory       | 2–3 sentences + direct link     | —          |

Teasers must match the article's **exploratory** writing style — present ideas as investigations, not prescriptions.

---

## LinkedIn

**Conventions:** Professional framing with industry relevance. 1–3 short paragraphs ending with a question or call to read. Use 3–5 relevant hashtags. Tone: thoughtful and accessible.

### Example (hypothetical article: "Why Epistemic Debt Matters in AI-Assisted Development")

> We treat AI-generated code as a productivity win. But what happens when the team no longer understands why the system behaves the way it does?
>
> I've been looking at the gap between "it works" and "we know why it works" — and how that gap compounds over time. The result isn't just technical debt; it's something subtler: epistemic debt.
>
> In this piece I explore how it shows up, why it's easy to miss, and what we can do before it becomes irreversible. Read it here: [link]

### Fill-in template

```yaml
linkedin: |
  [Opening hook or question that ties the article to your audience's work or concerns.]

  [1–2 sentences on what the article investigates and the main idea.]

  [Closing: invite to read with a clear CTA. Include link to article.]
  #hashtag1 #hashtag2 #hashtag3
```

---

## Twitter/X

**Conventions:** Hook + insight format. Lead with the most provocative or surprising claim. 1–2 tweets max, end with link. Tone: concise, punchy, still exploratory.

### Example (same hypothetical article)

> Epistemic debt: when the code runs but nobody knows why. AI-assisted dev is great until the "why" disappears. I wrote about how it compounds and what to do before it's too late. [link]

### Fill-in template

```yaml
twitter: |
  [One sharp hook or provocative claim from the article.]

  [Optional second line: key insight or implication.] [link]
```

---

## Instagram

**Conventions:** Visual-first — pair with a relevant image or quote card. Caption: 2–3 sentences summarizing the core insight. Put 10–15 hashtags in the first comment. Tone: accessible, slightly more casual. CTA: "link in bio" or direct link if allowed.

### Example (caption only; add your own visual or quote card)

> We celebrate AI-generated code that "just works" — but when nobody on the team can explain why it works, we're building epistemic debt. I wrote about how it shows up and how to catch it early. Link in bio.

### Fill-in template

```yaml
instagram_caption: |
  [1–2 sentences: core insight or question from the article, in plain language.]

  [CTA: e.g. "Link in bio" or "Full piece in my Substack — link in bio."]

  (Add 10–15 relevant hashtags in first comment, not in caption.)
```

---

## Substack Notes

**Conventions:** Brief teaser (2–3 sentences) with a direct link. Leverage Substack's native discovery. Tone: matches the article's exploratory voice.

### Example

> Epistemic debt in AI-assisted development: when the code runs but the "why" disappears. I explore how it compounds and what to do before it becomes irreversible. https://antoninorau.substack.com/p/…

### Fill-in template

```yaml
substack_notes: |
  [One sentence: main idea or hook.]

  [One sentence: what the reader will get.] [full Substack URL]
```

---

## After drafting

1. Copy each platform's final text into the article's front-matter under `social_teasers` (keys: `linkedin`, `twitter`, `instagram_caption`, `substack_notes`).
2. Use the Crosspost MCP or manual posting for LinkedIn and Twitter/X; post Instagram and Substack Notes manually.
3. See [docs/publishing-workflow.md](docs/publishing-workflow.md) for the full weekly workflow.

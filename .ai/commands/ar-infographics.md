---
description: "Command: Generate a complete Next.js infographic project for an article — analyzes content, proposes visualizations, and scaffolds an interactive static site."
alwaysApply: false
---

# Generate Interactive Infographics for an Article

Analyze an article's key concepts, formulas, and metaphors, then generate a complete Next.js 14 infographic project with interactive visualizations deployed as a static export to Vercel.

## Placeholders

| Placeholder | Description | Example |
| ----------- | ----------- | ------- |
| `{{TOPIC}}` | Topic directory name | `epistemic_debt` |
| `{{ARTICLE_PATH}}` | Article filename under `topics/{{TOPIC}}/artifacts/articles/` | `article-2-a-new-lens.md` |

## Prompt

Generate an interactive infographic project for the article at `topics/{{TOPIC}}/artifacts/articles/{{ARTICLE_PATH}}`.

The output directory is auto-derived:

```
topics/{{TOPIC}}/artifacts/infographics/<article-slug>/
```

Where `<article-slug>` is the article filename with `.md` stripped (e.g., `article-2-a-new-lens`).

---

## Phase 1: Article Analysis

1. Read the article at `topics/{{TOPIC}}/artifacts/articles/{{ARTICLE_PATH}}`
2. Extract:
   - Key concepts and their relationships
   - Formulas, equations, or mathematical models
   - Comparisons, contrasts, or taxonomies
   - Processes, timelines, or sequences
   - Metaphors that lend themselves to visual representation
3. Propose **5–8 infographic components** with names and brief descriptions
4. **Discuss the proposed components with the user before generating** — wait for approval or adjustments

---

## Phase 2: Project Generation

After user approval of the component list, generate a complete Next.js project with this structure:

```
<article-slug>/
├── package.json
├── next.config.js
├── README.md
├── .gitignore
├── public/
└── app/
    ├── layout.js
    ├── page.js
    ├── globals.css
    └── Infographics.js
```

### Mandatory Conventions

Follow these conventions exactly — they are derived from the existing `article-2` infographic project and ensure visual and structural consistency across all infographic deployments.

#### package.json

- Name: `<topic>-<article-slug>-infographics` (e.g., `epistemic-debt-article-2-infographics`). Use hyphens, not underscores.
- Dependencies: `next ^14.2.0`, `react ^18.3.0`, `react-dom ^18.3.0`
- Scripts: `dev`, `build`, `start`
- Private: true

#### next.config.js

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: { unoptimized: true },
};

module.exports = nextConfig;
```

#### globals.css

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background: #0c0e13;
  color: #e2e4e9;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

::-webkit-scrollbar {
  width: 4px;
}

::-webkit-scrollbar-thumb {
  background: #252a36;
  border-radius: 4px;
}

input[type="range"] {
  height: 4px;
}

button {
  transition: all 0.2s;
}

button:hover {
  filter: brightness(1.15);
}
```

#### layout.js

- Google Fonts: JetBrains Mono, Space Grotesk, Inter
- OpenGraph + Twitter Card metadata derived from the article title
- Author attribution to Antonino Rau / The AI Mirror

#### page.js

```js
import Infographics from './Infographics';

export default function Home() {
  return <Infographics />;
}
```

#### Infographics.js — Design System

Start with `"use client"` and these exact shared design tokens:

```js
const T = {
  bg: "#0c0e13",
  surface: "#14171e",
  surfaceHover: "#1a1e28",
  border: "#252a36",
  text: "#e2e4e9",
  textMuted: "#8a8f9e",
  accent: "#f97316",    // orange
  accentAlt: "#3b82f6", // blue
  danger: "#ef4444",
  success: "#22c55e",
  purple: "#a855f7",
  cream: "#fef3c7",
  font: "'JetBrains Mono', 'SF Mono', 'Fira Code', monospace",
  fontDisplay: "'Space Grotesk', 'Inter', sans-serif",
};
```

Include these reusable utilities:

- `useAnimatedValue(target, duration)` hook for smooth numeric transitions (ease-out cubic)
- Reusable sub-components as needed: `Legend`, `Formula`, `Stat`, `MiniSparkline`

#### Infographics.js — Component Patterns

- Each visualization is a **self-contained function component**
- Use `useState` for interactivity (toggles, sliders, selections)
- **Canvas** for mathematical/curve visualizations (2x DPI for retina)
- **SVG** for structured diagrams (balance beams, timelines, circular layouts)
- Styled inline with design tokens — **no CSS modules or external libs**
- **No external charting libraries** — all built with Canvas + SVG + HTML

#### Infographics.js — Main Component

- Renders all visualizations in a vertical scroll layout
- Each section: numbered header + description + interactive component
- Section styling: surface background, border, rounded corners, padding

#### .gitignore

```
node_modules/
.next/
out/
.vercel
```

#### README.md

Include:

- Project title and description
- Deploy to Vercel (GitHub push + one-click, or Vercel CLI)
- Local development instructions (`npm install`, `npm run dev`)
- Embedding in Substack (direct link approach — Substack doesn't support iframe embeds)
- List of all infographics with titles and descriptions

---

## Phase 3: Deployment Instructions

After generating all files, provide these instructions:/clear

1. Navigate to the output directory:

   ```bash
   cd topics/{{TOPIC}}/artifacts/infographics/<article-slug>/
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Preview locally:

   ```bash
   npm run dev
   ```

4. Deploy to Vercel via CLI or GitHub import

---

## Example Invocation

> Generate infographics for the article `article-2-a-new-lens.md` in the `epistemic_debt` topic.

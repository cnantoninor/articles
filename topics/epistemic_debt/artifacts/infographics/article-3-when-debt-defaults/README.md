# When Epistemic Debt Defaults — Interactive Infographics

Seven interactive visualizations for [Part 3 of the Epistemic Debt series](https://antoninorau.substack.com/) from The AI Mirror by Antonino Rau.

## Infographics

| # | Title | What it shows |
|---|-------|---------------|
| 01 | What LLMs Changed | Pre vs post-LLM pipeline — animate away the friction nodes that forced comprehension |
| 02 | Collapse of Competence | Three-group bar chart (Manual / Scaffolded AI / Unrestricted AI) with success/failure rate toggle |
| 03 | The Trust–Verify Gap | 96% distrust, 48% verify, 42% AI code — the stated vs actual behavior gap |
| 04 | Industry Signals | Four quality metrics trending wrong, plus AI vs human code comparison |
| 05 | Two Defaults | Interactive formula mapping for Case 1 (SaaStr DB deletion) and Case 2 (AlterSquare 10:1) |
| 06 | The t₀ Lever | Slider: position t₀ on the sprint timeline and watch the cost ratio emerge |
| 07 | Scale Spectrum | Same L3 gap, three blast radii: SaaStr → AlterSquare → AWS/Kiro |

## Local development

```bash
npm install
npm run dev
```

Visit `http://localhost:3000`.

## Deploy to Vercel

**Via GitHub:** Push to a GitHub repo and import at [vercel.com/new](https://vercel.com/new). Vercel auto-detects Next.js and runs `next build` + static export.

**Via CLI:**
```bash
npm i -g vercel
vercel
```

## Embedding in Substack

Substack does not support iframe embeds. Share the deployed Vercel URL as a direct link in the article body or as a card preview.

## Tech

Next.js 14 · React 18 · Static export (`output: 'export'`) · No external chart libraries — all Canvas + SVG + HTML.

# Epistemic Debt — Interactive Infographics

Seven interactive visualizations for **"Epistemic Debt: The Math, The Cost, and Why It's Not Technical Debt"** from *The Epistemic Shift* by Antonino Rau.

## Deploy to Vercel

### Option A: One-click (fastest)

1. Push this folder to a **GitHub repo**:
   ```bash
   cd epistemic-debt-infographics
   git init
   git add .
   git commit -m "initial commit"
   gh repo create epistemic-debt-infographics --public --push
   ```

2. Go to [vercel.com/new](https://vercel.com/new)
3. Import the repo — Vercel auto-detects Next.js
4. Click **Deploy** — done

### Option B: Vercel CLI

```bash
npm i -g vercel
cd epistemic-debt-infographics
npm install
vercel
```

Follow the prompts. Your site will be live in ~60 seconds.

## Local development

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Embedding in Substack

Once deployed (e.g. `https://epistemic-debt-infographics.vercel.app`), add this to your Substack post:

> **[Explore the interactive infographics →](https://your-url.vercel.app)**

Substack doesn't support iframe embeds from custom domains, so a direct link is the cleanest approach. Place it after the subtitle or at the end of the article.

## Infographics included

1. **The Widening Gap** — Cs(t) vs Gc(t) area chart with adjustable AI adoption point
2. **Abstraction Layer Cascade** — L1–L4 stack with cascade multipliers
3. **Break-Even Scale** — Net benefit balance visualization
4. **t₀ Timeline** — Early vs. late detection cost comparison
5. **Tech Debt vs. Epistemic Debt** — Interactive comparison table
6. **Epistemic Credit Buffer** — Tank/reservoir metaphor with adjustable ratio
7. **Green CI Trap** — Circular confirmation loop with break points

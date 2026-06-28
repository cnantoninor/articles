---
globs: topics/divulgative/**
paths: topics/divulgative/**
description: "Voice, audience, and terminology rules for divulgative (general-audience) articles"
alwaysApply: false
---

# Divulgative Articles

Rules for content under `topics/divulgative/`. These articles target a far broader, non-technical readership than the rest of the repository. Where this rule conflicts with the repo-wide defaults in `writing-style.md` or `terminology.md`, **this rule wins for files in `topics/divulgative/`**.

## Audience

- **Primary**: pubblico generale colto, educatori, lettori interessati a IA e cultura.
- Do **not** assume familiarity with programming or ML internals. The default tech-professional audience does not apply here.
- Cultural and humanistic angle is welcome (philosophy, education, society), not just engineering relevance.

## Language

- Italian by default (at least for the first draft). Keep the author's Italian voice; the author is a non-native English speaker with a philosophical, nuanced register.

## Terminology

- Define **every** technical term on first use, in plain language (e.g., "temperatura", "meccanismi di attenzione", "vettori"). The repo default of assuming programming concepts does not apply.
- Prefer concrete metaphors and everyday examples over jargon. If a term cannot be made accessible, reconsider whether it belongs.
- Author-introduced terms (e.g., *pensieri morti / pensiero vivo*) may go to `GLOSSARY.md` after the final draft; attribute borrowed terms to their source (e.g., *LLMorphism* → Valerio Capraro).

## Voice & Tone

- Exploratory, not prescriptive (same as repo default), but warmer and more essayistic.
- Be explicit when an interpretation is the author's own thesis rather than an established fact (e.g., "è la tesi che provo a sostenere", "si direbbe") instead of asserting it flatly.
- No em-dashes as parenthetical separators in prose (repo-wide rule still applies); use commas or parentheses.

## Fact-Checking & Prudence

- The standard fact-check gate still applies before publication (see `fact-checking.md`).
- Apply the Author's Prudence Principle strongly: soften or attribute claims rather than overstating. For scientific claims, attribute to the researcher ("Damasio mostra", "Lakoff e Johnson aggiungono") rather than stating them as universal fact, and note where empirical support is still debated.

## Collaboration

- Some divulgative pieces are co-authored (e.g., with Antonio Spadaro). Preserve both voices and flag open authorial decisions with `[QUESTION:]` rather than resolving them silently.

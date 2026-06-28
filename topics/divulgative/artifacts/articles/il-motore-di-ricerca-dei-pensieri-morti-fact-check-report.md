# Il motore di ricerca dei pensieri morti — Fact-Check Report

**Date:** 2026-06-28
**Article:** Il motore di ricerca dei pensieri morti
**Scope:** Tutte le affermazioni fattuali, le attribuzioni di concetti, i riferimenti accademici e le affermazioni tecniche

## Executive Summary

L'articolo è solido sul piano fattuale: tutti i riferimenti accademici esistono e sono attribuiti correttamente, e le affermazioni tecniche sugli LLM sono accurate. Sintesi: **9 VERIFIED, 1 INCORRECT (critico), 1 INCORRECT (minore), 3 OPINION-AS-FACT (accettabili nel registro esplorativo)**.

Il problema critico è uno solo ed è quello segnalato dall'autore: il termine **LLMorphism** è attualmente attribuito all'autore ("che chiamo LLMorphism") ma è stato coniato da **Valerio Capraro** (arXiv 2605.05419, maggio 2026). Va corretta l'attribuzione e aggiunto il riferimento.

Problema minore: il titolo italiano del libro di Lakoff e Johnson è *Metafora e vita quotidiana* (singolare), non *Metafore* (plurale); compare due volte.

Tutti i marcatori `[TODO: fact-check]` presenti nell'articolo possono essere rimossi: le affermazioni che marcano risultano verificate.

---

## Concetti nominati e attribuzioni

| Claim | Rating | Source | Notes |
|-------|--------|--------|-------|
| LLMorphism: modellare il proprio pensare sul funzionamento dell'LLM, fino a credere che pensare sia ricombinare. Articolo: "che chiamo LLMorphism" | INCORRECT (attribuzione) | Capraro, V. "LLMorphism: When humans come to see themselves as language models", arXiv:2605.05419 (maggio 2026) | Il termine è coniato da Valerio Capraro, non dall'autore. Definizione di Capraro: "the biased belief that human cognition works like a large language model". L'uso che ne fa l'articolo è coerente con la definizione; va corretta solo l'attribuzione. **Critico.** |
| Cognizione incarnata ("embodied cognition"): la mente è intessuta di corpo ed emozioni, non un calcolo nel vuoto | VERIFIED | Concetto consolidato in scienze cognitive (embodied cognition) | Attribuzione e descrizione accurate. |
| Damasio, in *L'errore di Cartesio*, mostra che le emozioni sono il presupposto della ragione; pazienti con lesioni conservavano logica e QI ma, persa la capacità di sentire, non riuscivano a decidere | VERIFIED | Damasio, *Descartes' Error* (1994); ipotesi del marcatore somatico; pazienti con danno alla corteccia prefrontale ventromediale (vmPFC), caso "Elliot" | Descrizione fedele all'ipotesi del marcatore somatico. Nota terminologica: è un'"ipotesi" scientifica, e l'articolo usa correttamente il verbo "mostra/mostrano" senza dire "dimostra". |
| Lakoff e Johnson: i concetti astratti poggiano sul corpo; l'affetto è "calore", la difficoltà è "peso" | VERIFIED | Lakoff & Johnson, *Metaphors We Live By* (1980) | AFFECTION IS WARMTH è una metafora concettuale introdotta nel libro del 1980. "Difficoltà come peso" corrisponde a DIFFICULTIES ARE BURDENS / la correlazione peso↔importanza. Contenuto corretto (vedi però errore nel titolo italiano, sotto). |
| Ricoeur: la "metafora viva" crea senso nuovo prima di logorarsi e diventare modo di dire | VERIFIED | Ricoeur, *La métaphore vive*, Seuil, 1975 | Opposizione metafora viva / metafora morta e creazione di senso: caratterizzazione accurata dell'opera. |
| L'IA è "una simulazione di conoscenza (cfr. Quattrociocchi ed Epistemia)" | VERIFIED | Quattrociocchi et al., "The simulation of judgment in LLMs", PNAS, ottobre 2025; termine "epistemia" | Attribuzione corretta. Precisazione: il paper parla di "simulazione del giudizio" e l'"epistemia" è definita come illusione/cortocircuito tra credibilità percepita e affidabilità reale. Il riferimento manca nell'elenco bibliografico (vedi suggerimento). |

## Affermazioni tecniche sugli LLM

| Claim | Rating | Source | Notes |
|-------|--------|--------|-------|
| Gli LLM rappresentano i segni come numeri/vettori; il vecchio motore di ricerca usava segni semplici normalizzati; oggi la rappresentazione tiene conto del contesto con meccanismi di attenzione | VERIFIED | Architettura transformer, word/token embeddings, self-attention | Descrizione corretta a livello divulgativo. |
| La casualità nei risultati è regolata da un parametro che gli addetti chiamano "temperatura" | VERIFIED | Parametro `temperature` nel sampling degli LLM | Accurato. |
| Si sta investigando se gli LLM possano risolvere problemi matematici mai incontrati nel dataset di training | VERIFIED | Aree di ricerca attive: FrontierMath (problemi inediti), MathArena (competizioni non contaminate), "memorization hypothesis" (caduta di performance su problemi post-cutoff) | Affermazione prudente e ben supportata. |
| Non spiegabilità, "allucinazioni", tendenza a compiacere (sycophancy), indeterminismo dei risultati | VERIFIED | Limiti documentati e ampiamente riconosciuti degli LLM attuali | Accurato. |

## Affermazioni interpretative / filosofiche

| Claim | Rating | Source | Notes |
|-------|--------|--------|-------|
| Gli LLM "non hanno alcun senso del tempo" | OPINION-AS-FACT | — | Affermazione difendibile (assenza di esperienza temporale vissuta) ma è una tesi interpretativa, non un fatto tecnico stabilito. Accettabile nel registro esplorativo; nessuna azione richiesta. |
| L'output dell'LLM "non è davvero nuovo": ricombinazione, non pensiero | OPINION-AS-FACT | — | Tesi centrale e dichiaratamente filosofica dell'articolo. Coerente con il registro esplorativo. Nessuna azione richiesta. |
| La macchina "non saprà mai di non sapere" | OPINION-AS-FACT | — | Affermazione retorica/interpretativa coerente col tono. Nessuna azione richiesta. |

---

## Critical Findings

1. **Attribuzione di "LLMorphism" (DA CORREGGERE PRIMA DELLA PUBBLICAZIONE).** Il termine è di Valerio Capraro (arXiv:2605.05419, maggio 2026), non dell'autore. Va riformulata la frase e aggiunto il riferimento bibliografico. Questo è anche un punto a favore della tesi dell'articolo: Capraro definisce LLMorphism proprio come il bias di credere che la cognizione umana funzioni come un LLM.

2. **Titolo italiano errato di Lakoff & Johnson.** L'articolo scrive *Metafore e vita quotidiana* (plurale); l'edizione Bompiani si intitola *Metafora e vita quotidiana* (singolare). Compare due volte: nel corpo (sezione "Il pensiero vivo è incarnato") e nella bibliografia.

---

## Actionable Suggestions

Ogni suggerimento è azionabile: l'autore può accettarlo, rifiutarlo o modificarlo. Le modifiche all'articolo verranno applicate solo dopo decisione esplicita.

| # | Location | Current Text | Suggested Change | Rationale | Decision |
|---|----------|-------------|-----------------|-----------|----------|
| 1 | §"Il rischio: credere che pensare sia ricombinare", ¶1 | "Qui si annida il pericolo, che chiamo LLMorphism:" | "Qui si annida il pericolo che Valerio Capraro ha chiamato LLMorphism:" | Corregge l'attribuzione: il termine è di Capraro (arXiv:2605.05419). | ✅ Accepted (applicato 2026-06-28) |
| 2 | Riferimenti | (assente) | Aggiungere: "Capraro, Valerio. *LLMorphism: When humans come to see themselves as language models*. arXiv:2605.05419, 2026. https://arxiv.org/abs/2605.05419" | Dare la fonte del termine ora attribuito a Capraro. | ✅ Accepted (applicato 2026-06-28) |
| 3 | §"Il pensiero vivo è incarnato", ¶1 | "in *Metafore e vita quotidiana*, aggiungono che..." | "in *Metafora e vita quotidiana*, aggiungono che..." | Titolo corretto dell'edizione italiana Bompiani (singolare). | ✅ Accepted (applicato 2026-06-28) |
| 4 | Riferimenti | "Lakoff, George, e Mark Johnson. *Metafore e vita quotidiana*. Bompiani (ed. orig. *Metaphors We Live By*, 1980)." | "Lakoff, George, e Mark Johnson. *Metafora e vita quotidiana*. Bompiani, 1998 (ed. orig. *Metaphors We Live By*, 1980)." | Titolo corretto e anno della prima edizione Bompiani (1998). | ✅ Accepted (applicato 2026-06-28) |
| 5 | §"Ma l'IA non crea pensieri nuovi?", ¶3 e Riferimenti | "una simulazione di conoscenza (cfr. Quattrociocchi ed Epistemia)" | Mantenere il testo e aggiungere alla bibliografia: "Quattrociocchi, Walter, et al. *The simulation of judgment in LLMs*. PNAS, 2025. (concetto di «epistemia»)" | Il riferimento è citato nel testo ma assente in bibliografia. | ✅ Accepted (applicato 2026-06-28) |
| 6 | §"Il pensiero vivo è incarnato" (riga `[TODO: fact-check]` ×2) e §"Ma l'IA non crea pensieri nuovi?" e Riferimenti | "[TODO: fact-check]" e "[TODO: completare e verificare i riferimenti prima della pubblicazione]" | Rimuovere i marcatori `[TODO: fact-check]` relativi a Damasio, Lakoff & Johnson, Ricoeur, embodied cognition e ricerca matematica/LLM | Tutte queste affermazioni risultano verificate in questo report. | ✅ Accepted (applicato 2026-06-28) |
| 7 | Riferimenti, Ricoeur | "Ricoeur, Paul. *La metafora viva*. Jaca Book (ed. orig. *La métaphore vive*, 1975)." | (Nessuna modifica obbligatoria) Opzionale: aggiungere l'anno dell'edizione Jaca Book se reperibile | L'originale 1975 (Seuil) è verificato; l'edizione italiana Jaca Book è plausibile ma l'anno non è stato confermato. Prudenza: lasciare senza anno è accettabile. | ✅ Accepted (applicato 2026-06-28) |

---

## Nota: embodied cognition, gli studi recenti confermano o moderano Damasio (1994)?

Sintesi: il **nucleo** della tesi regge ed è anzi rafforzato da lavori recenti, ma la parte sui **concetti astratti** va trattata con più cautela.

- **Confermano (concetti concreti).** Studi di neuroimaging recenti (es. fMRI, 2023) mostrano risorse neurali condivise tra pianificazione motoria e rappresentazione mentale, e attivazioni cross-modali (osservare un tocco attiva la corteccia somatosensoriale). C'è "considerevole" supporto empirico al fatto che i concetti concreti riattivino le modalità sensorimotorie.
- **Moderano (concetti astratti).** Per i concetti astratti, come "affetto" o "difficoltà", l'evidenza è descritta come "scarsa e limitata a domini ristretti". È esattamente il punto in cui l'articolo è più forte ("persino i concetti astratti poggiano sul corpo"): l'affermazione è corretta come tesi di Lakoff e Johnson, e l'articolo la attribuisce a loro, ma non è un fatto empirico consolidato quanto quello sui concetti concreti.
- **Dibattito metodologico aperto.** Il campo ha problemi di replicabilità e ambiguità definitoria (alcuni preferiscono "grounded cognition"); l'ipotesi del marcatore somatico ha avuto anche revisioni critiche. Nulla che smentisca l'articolo, ma conferma che la prudenza nel registro ("mostra", "aggiungono") è la scelta giusta.

Conseguenza pratica: l'attribuzione esplicita a Damasio e a Lakoff & Johnson è già la formulazione più onesta. Nessuna correzione obbligatoria; se si volesse essere ancora più prudenti, si potrebbe aggiungere un inciso sul fatto che per i concetti astratti la prova empirica è più dibattuta.

## Sources

- [LLMorphism — arXiv:2605.05419 (Valerio Capraro)](https://arxiv.org/abs/2605.05419)
- [Somatic marker hypothesis — Wikipedia](https://en.wikipedia.org/wiki/Somatic_marker_hypothesis)
- [Metaphors We Live By — Wikipedia](https://en.wikipedia.org/wiki/Metaphors_We_Live_By)
- [La Métaphore vive / The Rule of Metaphor — Internet Archive](https://archive.org/details/ruleofmetaphormu0000ricu)
- [Epistemìa (Quattrociocchi et al., PNAS 2025) — AI4Business](https://www.ai4business.it/intelligenza-artificiale/epistemia-la-parola-che-svela-il-rischio-invisibile-dei-modelli-linguistici/)
- [L'errore di Cartesio, Adelphi 1995 — Adelphi](https://www.adelphi.it/libro/9788845911811)
- [Metafora e vita quotidiana, Bompiani — Hoepli](https://www.hoepli.it/libro/metafora-e-vita-quotidiana/9788845233609.html)
- [FrontierMath — Epoch AI](https://epoch.ai/frontiermath/tiers-1-4/about)

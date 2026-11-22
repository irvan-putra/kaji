---
id: idsw-ai-safety-keynote
type: research-note
---
# Is AI safe? Yes, but: an IDSW keynote, checked (source note)

Public page: https://vanipy.com/kaji/ai-safety/ . Reading of the IDSW 2026 day-two keynote "Pesan Systems Engineering Modern dalam Membangun Purwarupa AI ke Sistem Produksi yang Aman, Teruji, dan Layak Dipercaya" (22 Nov 2026, 10:05-10:50, listed speaker Mansur Maturidi Arief, KFUPM AI Verification and Validation Lab, per the official agenda), based on photographed slides sent during the talk, which are not reproduced.

## Reference-check results (checked 22 Nov 2026)

- Geirhos et al. 2020, shortcut learning (Nature Machine Intelligence): confirmed, slide framing matches the paper.
- Goodfellow, Shlens & Szegedy 2014 (arXiv:1412.6572): confirmed. The pig-plus-noise slide with 90% confidences is the speaker's illustration, not a replicated benchmark.
- Ilyas et al. ICML 2018 (PMLR v80 ilyas18a): confirmed, black-box attacks with limited queries.
- Eykholt et al. CVPR 2018: confirmed, physical poster/sticker attacks; stop sign misread as speed limit across distances/angles, drive-by-style tests. The slide's comparison grid is from this paper.
- Wang et al. 2023 (arXiv:2302.12095), ChatGPT robustness: confirmed for the legible citation; the case table has word-level sentiment flips and sentence-level substitution. A second citation in the same slide's fine print was illegible in the photo; not guessed.
- ProPublica "Machine Bias" 2016: confirmed as the source of the two-arrests COMPAS example. Scope kept: one scoring system, one country, one investigation; Northpointe disputed the method; fairness-definition debate continued afterwards. Not generalized to every judicial system.

## Indonesia-context statistics (all dated, populations kept)

All from the Stanford HAI AI Index Report 2025 unless noted; none is a 2026 measurement.

- Notable AI models by geographic area, 2023-24 (sum): concentrated in US and China; "notable" is the report's selection.
- "Languages in the Internet" table: English dominant; underlying source/year not legible in the photo (W3Techs-style survey suspected, unverified).
- Relative AI hiring rate year-over-year ratio by geographic area, 2024 (LinkedIn via AI Index): Indonesia absent from the ranked list shown. Growth ratio, not absolute levels; absence is not "no AI jobs".
- Net AI talent migration per 10,000 LinkedIn members by geographic area, 2024: Indonesia low/negative. LinkedIn members only, normalized per member count.
- Ipsos 2024 opinion data (via AI Index): Indonesia near the top on agreement that AI improves time-to-get-things-done ("#2 most optimistic" is the slide's reading). One survey, one year, specific statements; not national AI readiness.
- "Are we truly optimistic, or simply ignorant?" heatmap: same Ipsos 2024 data, self-assessed familiarity statements. The "ignorant?" framing is the speaker's discussion prompt, not a survey finding.
- Agentic-coding gender-multiplier demonstration (Laki-laki 1.1 / Perempuan 0.9 in generated code): a single on-stage demonstration, not a prevalence measurement.

## Thesis and reuse

The "Yes, but..." thesis is presented on the page as safety-as-engineering-practice (evaluation plus monitoring), not a default property. Practice stages derived from the keynote live in Sanggup's Coding path (https://vanipy.com/sanggup/#coding, stages cd14-cd18): classifier lifecycle/OOD, shortcut hunting, adversarial reading, training-bias audit, eval-and-monitoring plan, with the same attributions.

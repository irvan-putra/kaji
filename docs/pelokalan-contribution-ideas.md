---
id: pelokalan-contribution-ideas
type: research-note
---
# Pelokalan contribution ideas (source note)

Written 24 Nov 2026. Source note for the review page at
https://vanipy.com/kaji/pelokalan/review/ .

## What this is

[Pelokalan](https://github.com/blankon/pelokalan) is Herpiko Dwi Aguno's web-based
gettext (PO/POT) translation editor for teams: Go 1.24 + Chi + htmx + PostgreSQL 16,
email one-time-code sign-in, glossaries, translation memory, AI pre-translation with
glossary-first rules, per-file version history, and a badge/achievement system.
MIT licensed; live instance at https://pelokalan.blankon.id . The maintainer is open
to contributions ("Bug reports, suggestions and code contributions are very welcome"
in the README) and to AI-assisted contribution in particular; his own commit style is
`fix(gen): ...` and the repo ships a CLAUDE.md.

The review page lists 19 candidate contributions in five groups, each with effort,
risk and whether maintainer buy-in is needed first. It is an options page, not a
plan: nothing is built or proposed upstream until each exact change and its PR
wording is approved, and any pull request will disclose the AI assistance.

## How the ideas were grounded

Checked against the source at commit `d565b6f` (24 Nov 2026), on the fork
https://github.com/irvan-putra/pelokalan :

- `go build`, `go vet` and all 20 package test suites pass.
- No CI workflow (`.github/` absent), no CONTRIBUTING.md, no SECURITY.md.
- Untested packages include netsafe (the SSRF guard), blobstore and the auth /
  SameOrigin middleware; po, glossary, ai, i18n, spelling, thesaurus and the web
  handlers do have tests.
- Security headers (nosniff, frame denial, referrer policy) and a sandboxed CSP for
  user content already exist, so header work is off the list.
- The public API is read-only and members-only today, so a progress endpoint plus an
  embeddable SVG badge extends an existing pattern rather than inventing one.
- The badge system (26 badges, 6 groups, tiers bronze-diamond, share cards, email
  announcements) was added in the two weeks before this note, which makes
  achievements-adjacent ideas (AI-draft reviewer badge, project milestones)
  natural follow-ups.

## Limits

- Effort and risk labels are estimates from a read of the code, not from building it.
- Upstream moves daily (commits through 23 Nov 2026), so any chosen work should be
  kept small and sequential, and re-based before a PR.
- Ideas that change translator-facing behavior (glossary warnings, review queue,
  validation defaults, badges, dark theme, mobile editor) need the maintainer's
  agreement on shape before code is written.

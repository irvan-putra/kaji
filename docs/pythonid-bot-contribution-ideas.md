---
id: pythonid-bot-contribution-ideas
type: research-note
---
# PythonID-bot contribution ideas (source note)

Written 24 Nov 2026. Source note for the review page at
https://vanipy.com/kaji/pythonid-bot/review/ .

## What this is

PythonID-bot is Rezha Julio's Telegram moderation bot for the PythonID community:
profile-photo and username checks, captcha for new members, layered anti-spam
(duplicate detection, bio-bait, contact cards, guest-bot blocking) and a
monitor-only AI spam classifier. Python 3.11+, aiogram 3, SQLModel, MIT licensed.
The repo is private at the moment, so both the review page and this note stay
high-level and quote no internals.

State verified locally at commit `8b2c65c` (24 Nov 2026): `uv sync --dev` clean,
1,390 tests pass, ruff clean, mypy clean (92 files), 97% line coverage overall
with five service modules between 70% and 95%.

The review page lists 9 candidate contributions in three groups plus one
attribution decision, each with effort, risk and whether Rezha's buy-in is needed
first. It is an options page, not a plan: nothing is pushed to the repo until
Irvan approves each exact change. Rezha is OK with AI-assisted contributions
(Irvan, 24 Nov); commit/PR attribution wording is the one open decision on the
page.

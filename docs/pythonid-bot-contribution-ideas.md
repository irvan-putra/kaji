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

The state was checked against the current source on 24 Nov 2026; specifics stay
out of this note because the repo is private.

The review page lists 9 candidate contributions in three groups plus one
attribution decision, each with effort, risk and whether Rezha's buy-in is needed
first. It is an options page, not a plan: nothing is pushed to the repo until
Irvan approves each exact change. Attribution wording is settled (Irvan, 24 Nov):
follow each project's own contribution rules - for this repo that means its own
norms apply to commit/PR wording, and nothing states or implies human authorship.

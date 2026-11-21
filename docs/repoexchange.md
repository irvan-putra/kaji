# Repo Exchange: a public catalogue of GitHub repos ranked by star growth

Checked 2026-11-21 (WIB). Everything below comes from the public pages of [repoexchange.web.id](https://repoexchange.web.id/), read signed out in a browser. The site does not name its operator on the page, and this note does not guess.

## What it is

Repo Exchange is a self-described "curated view of the projects moving open source forward": a public catalogue that tracks GitHub repositories and ranks them by star growth rather than total stars. The tagline is "Track what's gaining momentum."

What is on the public page at check time:

- **Repository leaderboard** ranked by GitHub star growth, switchable between 24 hours, 7 days and 30 days. Each row shows category, language, total stars, 7-day star change and a trend sparkline, with search and a category filter (AI, Developer Tools, Data, Design). A scrolling ticker of 7-day star changes runs across the top. About 300 repositories were tracked at check time, from very large projects to brand-new repos with zero 7-day growth; the catalogue already includes at least one vanipy repo (irvan-putra/pythonid-10-2026, listed with 0 stars gained in 7 days).
- **Star growth chart** for the tracked set, e.g. "Total star change: +21,439 · 2026-11-20 to 2026-11-21 (UTC)".
- **Editor's picks**, described as "editorial starting points, not paid placements" (cli/cli was featured at check time).
- **New listings**, ordered by when a repo was first added to the catalogue.
- **Collections**, four curated starting points for discovery.
- **Submit a repo**: anyone can submit a public GitHub repository URL with a category. The site says public repositories are reviewed before listing; submissions and decisions are stored in Neon, the site owner makes the final publishing decision, and rejected submissions remain visible to the owner with the reason.
- A **Sign in** button exists; it was not used or explored.

## How growth is measured, per the site's own methodology note

Growth compares the latest star count with a prior snapshot, with a maximum snapshot age tolerance of 6 hours for the 24-hour view, 2 days for 7 days, and 4 days for 30 days. A dash means there is not enough history. Repositories without enough history are unranked and shown after ranked entries, sorted by total stars. The page itself warns: "Star growth, not financial data."

## What is not offered at check time

- **No RSS, Atom feed or newsletter.** /feed, /rss, /feed.xml, /rss.xml, /sitemap.xml and /robots.txt all return 404, and the page head contains no feed link. Following the catalogue currently means revisiting the site.
- **No static rendering.** The leaderboard is populated client-side; a plain HTML fetch shows only "Loading…" placeholders.

## Not verified

Star counts and growth figures are the site's own snapshot data and were not cross-checked against GitHub. Review criteria beyond the public summary above, submission turnaround, and what sign-in unlocks are unknown from the public page.

## Source

- [Repo Exchange](https://repoexchange.web.id/) (public pages, checked 2026-11-21)

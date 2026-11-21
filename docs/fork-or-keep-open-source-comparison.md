# Fork or keep: comparing our repos with existing open source

Date: 2026-11-21. Scope: all 73 public repos under github.com/irvan-putra (live inventory via the GitHub API). Upstream facts (license, latest release, last commit) were checked on 2026-11-21 against each project's GitHub repo, README or official site; our repos' purposes come from their public READMEs. Maintenance signals (recent release, recent commits) are not a security audit, and no candidate here has had a proof-of-concept integration. License notes compare identifiers and documented clauses only; they are not legal advice. "Nothing covers it" claims are bounded to the candidates named beside each repo.

Nothing was changed, forked, relicensed or adopted as part of this research.

## Strongest candidates , evaluate first

1. **gitsafescan , evaluate gitleaks as a second scanner.** gitleaks (MIT, latest release v8.30.1, Mar 2026, commits into Oct 2026) and trufflehog (AGPL-3, released Nov 2026, verifies whether found keys are live) both scan full git history. Running them as external tools alongside gitsafescan avoids combining code in this pass; if one is ever bundled or distributed, its license obligations need review first. gitsafescan has no LICENSE file. Keep its own checks either way: personal data, private network references and risky tracked paths are not what the secret scanners look for.

2. **simak , evaluate publishing the agenda as .ics or frab XML.** Giggity (GPL-2.0, active) reads Pentabarf/frab/wafer/Pretalx/OSEM XML and plain .ics, and per its README already has talk selection, reminders and search. A feed export from schedule.json lets event attendees use it, while simak keeps its notes and on-device contact matching. A feed adapter keeps the two as separate programs, which sidesteps the GPL-2.0-only versus AGPL-3 combination question; actual obligations depend on how it is shipped.

3. **utak , evaluate Observable Framework for the first prototype.** utak is a concept with no app yet, so there is no rework cost. Observable Framework (ISC license, latest release Mar 2026) builds interactive, data-driven pages as a static site that fits GitHub Pages. Idyll matches the explorable-explanations domain exactly, but its repo has been dormant since Feb 2023.

4. **cabang , decide the strategy before going deeper.** cabang is GPL-3, the same license identifier as deltachat-android (upstream released v2.69.0 in Nov 2026). cabang's README says its Android flows have not run on a device or live account yet. A standalone client means maintaining a whole chat UI for one threaded-reply feature; a patch on a deltachat-android fork, or an upstream proposal, would keep the diff small. Matching identifiers alone do not settle distribution obligations , those need review before any fork ships.

## Open options , they change daily-use tools, so they wait for an explicit decision

5. **tindak vs Tasks.org.** Tasks.org (GPL-3, released Nov 2026) is a mature Android tasks app with widgets and recurrence; tindak has no LICENSE file yet. Using Tasks.org as an app needs no license decision; borrowing its GPL-3 code into tindak would make tindak a GPL-3 derivative , a separate licensing decision, not part of this comparison. tindak's DeltaChat webxdc shared lists and assistant feeds have no equivalent in Tasks.org, so tindak stays either way.

6. **menit vs ActivityWatch.** ActivityWatch (MPL-2, released Nov 2026, has an Android app) tracks app usage on-device, overlapping menit's core. menit's difference, per its README, is estimating how much phone time goes to AI specifically, with only Usage access and no network permission.

7. **jumpa vs Monica.** Monica (AGPL-3) is a full personal CRM. Its code is active (commits in Oct 2026) but its latest release, v4.1.2 (May 2024), is about 31 months old, and it needs a self-hosted server. jumpa is a zero-permission offline Android app (GPL-3).

8. **kokok vs Fossify Clock as a base.** kokok is AGPL-3; Fossify Clock is GPL-3 (latest release Jan 2026). GPLv3 section 13 provides a documented path for combining GPL-3 code into an AGPL-3 work, but the concrete obligations still need review before any fork. kokok's actual feature , alarms applied from an assistant's signed, encrypted feed , has no counterpart in Fossify Clock's published feature list, so that layer stays custom either way.

## Checked and kept custom , with the reason

- **tuju:** Transportr (GPL-3, active) and its data layer public-transport-enabler list providers for Europe, the UAE and the US only , no Indonesia (checked in the provider enum source). OpenTripPlanner could route from TransJakarta GTFS but needs a hosted server.
- **tampung:** Seedvault's README states it must be integrated into the Android ROM and cannot be installed as a regular app , ruled out on a stock phone. The restic append-only research remains the viable path.
- **tagih:** Crater (AGPL-3) is server-based and its latest release, 6.0.6, is from Mar 2022 (about 57 months ago). Invoice Ninja (release Nov 2026) uses the Elastic License 2.0, which is source-available, not OSI open source. Neither fits an offline, local-first Android tracker.
- **tengok:** Readwide and Amaze File Utilities (GPL-3, latest release Jul 2024) cover documents and media; neither reads MIDI. tengok's MIDI-first scope stays custom.
- **nada:** mido (MIT) and music21 (BSD-3) are Python-only, so they are not drop-in for nada's browser runtime. Using mido on the Python CLI side is possible in principle, but nada's README describes a byte-parity contract between its Python and JS implementations, so any such reuse needs a parity evaluation first , not a straight swap.
- **denting:** same runtime mismatch as nada: denting runs in the browser, mido and music21 are Python. Its deterministic, no-AI edit engine is the product; nothing checked covers it.
- **bedah:** likec4 (MIT, released Nov 2026) does C4 diagrams-as-code well, but bedah is a FreeForm-style infinite review canvas with generated self-review content; adopting likec4 would mean reworking the content pipeline. Worth evaluating only if the C4 layer grows on its own.
- **kemas:** Loop Habit Tracker (GPL-3, released Oct 2026) tracks recurring habit streaks; kemas is before-and-after cleaning photos with difference analysis , a different job.
- **bidik:** Open Recorder (GPL-3, released Oct 2026) overlaps only the screen-recording feature; the capture queue and pairing are the project.
- **kapan:** Mobilizon is a full federated events platform, far heavier than one static page; eventio is a 7-star scraper. kapan already publishes a standard events.ics feed.
- **denyut + jin:** the first candidate checked, deltabot (MPL-2), has been dormant since Oct 2023 , but Delta Chat's own documentation (py.delta.chat) recommends the JSON-RPC bindings, maintained by core developers, for new bots. jin already runs a bot from the phone through the Delta Chat core. Keep the apps custom on top of the maintained official bindings rather than any stale bot framework.
- **daya:** cookiecutter, Yeoman, Plop and Hygen are project scaffolding tools (project trees from templates); daya compiles a small chatbot-written recipe into a finished mini-app , a different problem.
- **sanggup:** Lingonaut is a community Duolingo alternative for language learning only, and an official source repo could not be verified. Nothing checked covers life-skills paths with instructor sign-off.
- **saku:** its README states license selection is still pending, no storage implementation is selected, and KeePassJava2 interoperability spikes are in progress (one known failing test). A synthetic demo APK exists; the KeePass-ecosystem path already avoids from-scratch crypto. No action.
- **patuh:** todogroup/repolinter (Apache-2.0, last push Feb 2026) lints repositories against generic open-source policies; patuh checks this app family's own conventions , package IDs, icon geometry, versions, gallery catalog , a different rule set. repolinter is a candidate only if generic policy checks are ever wanted.
- **sambung:** simonw/llm (Apache-2.0, active) packs prompts for the command line; sambung's reply-shape validation and Android share-target round trip are the product. A candidate for ideas, not adoption.
- **sapa:** already reuses Google's MediaPipe pose models on-device, per its README. Nothing checked covers question rounds and random audience picks.
- **unggah:** MGit (GPL-3, active, pushed Sep 2026) is a general Android git client; unggah's ZIP-to-commit-to-push flow is a narrower job. Evaluate MGit only if general git operations on the phone are ever wanted.

## Assessed at README level only (4)

- **tumbuh:** public proposals site plus an Android capture MVP (README, pushed Nov 2026). No dedicated upstream comparison in this pass.
- **kembang:** GitHub Actions experiment , new issue to AI processing to pull request (README, pushed Mar 2025). No license file. No upstream comparison in this pass.
- **picu:** no README and no description on GitHub (Python, pushed Mar 2025). Cannot be classified from public source; follow-up if wanted.
- **tayang:** a background-listening Python script with an open TODO for its requirements file (README, pushed Nov 2024). No license file. No upstream comparison in this pass.

## Already forks or previously decided

unggun (fork of Obtainium), animate (fork with an upstream PR open), encore (fork of chatmail/core carrying a local fix). saku's KeePass-ecosystem direction is recorded above.

## Content, research and idea repos (20)

kunjung, suaka, pustaka, kaji, kaca, gotong, mimpi, anyam, jejak, naga, pandu, catat, irvan, tapak, tangkai, onda, aiq, paper2repo, sapi, pythonid-10-2026. These are notes, demos, proposals and presentation pages rather than reusable wheels, so no upstream comparison applies to them.

## Legacy forks and pre-2026 sites (19) , not examined

awx, bitstarter, setup, hello-lambda-jakarta, hackathon, typing, org-ruby, pyconapac2024-teaser, minima, devguide, vault-cli, PL101ProjectTemplate, adaptechid, myschoolcampid, old-visi-web, haskell-intro, vnproject.id, irvan-putra, irvan-putra.github.io.

## Sources

- Live inventory: https://api.github.com/users/irvan-putra/repos
- https://github.com/gitleaks/gitleaks · https://github.com/trufflesecurity/trufflehog
- https://github.com/Wilm0r/giggity (README: supported feed formats, talk selection, reminders)
- https://github.com/observablehq/framework · https://github.com/idyll-lang/idyll
- https://github.com/deltachat/deltachat-android · https://py.delta.chat/ (maintained JSON-RPC bindings)
- https://github.com/tasks/tasks · https://github.com/ActivityWatch/activitywatch
- https://github.com/monicahq/monica · https://github.com/FossifyOrg/Clock
- https://github.com/schildbach/public-transport-enabler (NetworkId.java provider list) · https://github.com/grote/Transportr
- https://github.com/seedvault-app/seedvault (README: ROM integration required)
- https://github.com/crater-invoice-inc/crater · https://invoiceninja.github.io/docs/legal/license
- https://github.com/likec4/likec4 · https://github.com/mido/mido · https://github.com/cuthbertLab/music21
- https://github.com/iSoron/uhabits · https://github.com/NoneBaiano/OpenRecorder
- https://github.com/deltachat-bot/deltabot · https://github.com/TeamAmaze/AmazeFileUtilities
- https://github.com/todogroup/repolinter · https://github.com/maks/MGit · https://github.com/simonw/llm
- Our repos' public READMEs (tuju, simak, menit, jumpa, kokok, tengok, tampung, tagih, nada, denting, bedah, kemas, bidik, kapan, cabang, denyut, jin, daya, sanggup, saku, tindak, patuh, sambung, sapa, unggah, tumbuh, kembang, tayang)

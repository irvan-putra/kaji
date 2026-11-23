# Fork or keep: our repos vs open source

*73 public repos checked on 21 Nov 2026. Inventory coverage is split below into named candidate comparisons, code-inspected experiments, existing forks, content and unexamined legacy repos. Candidate licenses and maintenance signals were checked that day. Nothing was changed, forked or adopted.*

![Illustration: one branch merging into a shared river, another continuing on its own path](assets/illustrations/fork-or-keep-hero.png)

*Generated concept illustration of reuse and independent development, not a product screenshot or integration proof.*

## Strongest candidates, evaluate first

| Repo | Candidate to evaluate | Why |
| --- | --- | --- |
| gitsafescan | gitleaks (MIT, release ~8 months ago, commits into Oct 2026); trufflehog (AGPL-3, released 2 days ago, verifies live keys) | Both scan full git history. Running them as external tools alongside gitsafescan avoids combining code in this pass; if one is ever bundled or distributed, its license obligations need review first. gitsafescan has no LICENSE file. Keep its own checks either way: personal data, private network references and risky tracked paths are not what secret scanners look for. |
| simak | Publish the agenda as .ics or frab XML for Giggity (GPL-2.0, commits this week) | Giggity reads Pentabarf/frab/wafer/Pretalx/OSEM XML and plain .ics, and per its README already has talk selection, reminders and search. A feed export from schedule.json lets IDSW attendees use it, while simak keeps its notes and on-device contact matching. A feed adapter keeps the two as separate programs, which sidesteps the GPL-2.0-only versus AGPL-3 combination question; actual obligations depend on how it is shipped. |
| utak | Observable Framework (ISC license, latest release Mar 2026) | utak is a concept with no app yet, so there is no rework cost. Observable Framework builds interactive, data-driven pages as a static site that fits GitHub Pages. Idyll matches the explorable-explanations domain exactly, but its repo has been dormant for about 46 months. |
| cabang | Decide strategy before going deeper: deltachat-android fork, upstream proposal, or standalone | cabang is GPL-3, the same license identifier as deltachat-android (upstream released v2.69.0 eleven days ago). cabang's README says its Android flows have not run on a device or live account yet. A standalone client means maintaining a whole chat UI for one threaded-reply feature; a patch on a deltachat-android fork, or an upstream proposal, would keep the diff small. Matching identifiers alone do not settle distribution obligations; those need review before any fork ships. |

## Your call, these change what you use daily

| Repo | Compared with | The decision |
| --- | --- | --- |
| tindak | Tasks.org (GPL-3, released 4 days ago) | Tasks.org is a mature Android tasks app with widgets and recurrence; tindak has no LICENSE file yet. Using Tasks.org as an app needs no license decision. Borrowing its GPL-3 code into tindak would make tindak a GPL-3 derivative, a separate licensing decision, not part of this comparison. tindak's DeltaChat webxdc shared lists and assistant feeds have no equivalent in Tasks.org, so tindak stays either way; the open question is who handles personal tasks. |
| menit | ActivityWatch (MPL-2, released 6 days ago, has an Android app) | ActivityWatch tracks app usage on-device, overlapping menit's core. menit's difference, per its README, is estimating how much phone time goes to AI specifically, with only Usage access and no network permission. Adopt ActivityWatch and treat AI apps as a category, or keep menit deliberately narrow. |
| jumpa | Monica (AGPL-3; code active, latest release v4.1.2 about 31 months old) | Monica is a full personal CRM: notes, relationship history, reminders, but needs a self-hosted server. jumpa is a zero-permission offline Android app (GPL-3). If one hosted service is acceptable, Monica covers the concept and more; if offline-only matters, jumpa stays. |
| kokok | Fossify Clock (GPL-3, latest release about 9 months ago) | kokok is AGPL-3. GPLv3 section 13 provides a documented path for combining GPL-3 code into an AGPL-3 work, but the concrete obligations still need review before any fork. kokok's actual feature, alarms applied from an assistant's signed, encrypted feed, has no counterpart in Fossify Clock's published feature list, so that layer stays custom either way. |

## Checked and kept custom, with the reason

| Repo | Checked against | Reason it stays custom |
| --- | --- | --- |
| tuju | Transportr (GPL-3, active); public-transport-enabler; OpenTripPlanner | The provider list in public-transport-enabler's source covers Europe, the UAE and the US only, no Indonesia. OpenTripPlanner could route from TransJakarta GTFS but needs a hosted server. The offline single-screen map stays custom. |
| tampung | Seedvault | Seedvault's README states it must be integrated into the Android ROM and cannot be installed as a regular app; ruled out on a stock Samsung. tampung's restic append-only research remains the viable path. |
| tagih | Crater (AGPL-3); Invoice Ninja (Elastic License 2.0) | Crater is server-based and its latest release, 6.0.6, is about 57 months old. Invoice Ninja is source-available, not OSI open source. Neither fits an offline, local-first Android tracker. |
| tengok | Readwide; Amaze File Utilities (GPL-3, latest release about 28 months ago) | Both cover documents and media, neither reads MIDI. tengok's MIDI-first scope (piano roll, playback, planned game mode) stays custom. |
| nada | mido (MIT); music21 (BSD-3) | Both are Python-only, so they are not drop-in for nada's browser runtime. Using mido on the Python CLI side is possible in principle, but nada's README describes a byte-parity contract between its Python and JS implementations, so any such reuse needs a parity evaluation first, not a straight swap. |
| denting | mido, music21 | Same runtime mismatch as nada: denting runs in the browser. Its deterministic, no-AI edit engine is the product; nothing checked covers it. |
| bedah | likec4 (MIT, released 7 days ago) | likec4 does C4 diagrams-as-code well, but bedah is a FreeForm-style infinite review canvas with generated self-review content; likec4 covers neither, and adopting it would mean reworking the content pipeline. Worth evaluating only if the C4 layer grows on its own. |
| kemas | Loop Habit Tracker (GPL-3, released last month) | Loop tracks recurring habit streaks. kemas is before-and-after cleaning photos with difference analysis, a different job. |
| bidik | Open Recorder (GPL-3, released last month) | Overlaps only bidik's screen-recording feature. The capture queue and assistant pairing are the project; Open Recorder is a readable reference. |
| kapan | Mobilizon; eventio | Mobilizon is a full federated events platform, far heavier than one static page. eventio is a 7-star scraper. kapan already publishes a standard events.ics feed, which is the interop that matters here. |
| denyut + jin | deltabot (MPL-2, dormant ~38 months); Delta Chat JSON-RPC bindings | Delta Chat's own documentation (py.delta.chat) recommends the JSON-RPC bindings, maintained by core developers, for new bots. jin already runs a bot from the phone through the Delta Chat core. Keep the apps custom on top of the maintained official bindings rather than any stale bot framework. |
| daya | cookiecutter, Yeoman, Plop, Hygen | Those stamp out project trees from templates. daya compiles a small chatbot-written recipe into a finished mini-app, a different problem. Borrow their incremental-generation ideas at most. |
| sanggup | Lingonaut | Lingonaut is a community Duolingo alternative for language learning only, and its official source repo could not be verified. Nothing checked covers life-skills paths with instructor sign-off. |
| saku | KeePass ecosystem | saku's README says license selection is still pending, no storage implementation is selected, and KeePassJava2 interoperability spikes are in progress (one known failing test). A synthetic demo APK exists. Its KeePass-ecosystem path already avoids from-scratch crypto. No action. |
| patuh | todogroup/repolinter (Apache-2.0, last push Feb 2026) | repolinter lints repositories against generic open-source policies. patuh checks this app family's own conventions: package IDs, icon geometry, versions, gallery catalog. repolinter is a candidate only if generic policy checks are ever wanted. |
| sambung | simonw/llm (Apache-2.0, active) | llm packs prompts for the command line; sambung's reply-shape validation and Android share-target round trip are the product. A candidate for ideas, not adoption. |
| sapa | Google MediaPipe pose models | Already reuses MediaPipe on-device, per its README. Nothing checked covers question rounds and random audience picks. |
| unggah | MGit (GPL-3, active, pushed Sep 2026) | MGit is a general Android git client; unggah's ZIP-to-commit-to-push flow is a narrower job. Evaluate MGit only if general git operations on the phone are ever wanted. |

## Code-inspected this round

| Repo | What the code shows | Candidate / verdict |
| --- | --- | --- |
| tumbuh | Public proposals site plus the consolidated Android app (v0.2.2, AGPL-3 in android/, Java with no third-party libraries, no internet permission). The app is a manual triage list: items carry a 1 to 5 weight and a decision (keep, renegotiate, ask for help, let go, done), each with a first step and an editable draft message. | Checked against Tasks.org (GPL-3, released 4 days ago): mature, but no weighting, decision options or draft messages, so this flow stays custom. The proposal and economics pages are content; no upstream applies. |
| kembang | On each new issue the workflow branches, runs an AI step and opens a PR, but the AI step is a placeholder and the README says you must add your own AI service integration. So kembang is a scaffold, not a working automation. No license file. | OpenHands (MIT, about 94k stars, pushed this week) ships an official GitHub Action that does the real loop: label an issue fix-me or comment @openhands-agent and its agent opens a pull request. Candidate to evaluate instead of completing the scaffold; it needs an LLM API key and a trial run. |
| picu | No README, but the code is readable: roadmap_generator.py asks what triggered your learning journey, sends it to Alibaba Cloud DashScope (qwen-plus) and writes the returned JSON roadmap as interlinked markdown files with Next Steps links; example/ holds generated Python-topic roadmaps. Purpose reconstructed from code, not docs. Created and last pushed 6 Mar 2025, a single-day experiment with no license file. | simonw/llm (Apache-2.0, active) or fabric (MIT, active) could run such a prompt generically, but neither emits the interlinked node files picu writes; if revived, llm templates and schemas are the candidate to evaluate. |
| tayang | background_listening.py is a hands-free slide clicker: background microphone, local Whisper (base model) through the SpeechRecognition library, next/back voice commands driving pyautogui clicks and arrow keys. train_journey.py is not code but a slide deck in pysentation format (mimseyedi/pysentation, GPL-3, last push Mar 2025). Created and last pushed 30 Nov 2024, a single-day experiment with no license file. | It already reuses Whisper; if revived, faster-whisper (MIT, active) or whisper.cpp (MIT, active) are the maintained recognition backends to evaluate. |

## Already forks or previously decided

unggun is the Obtainium fork, animate is a fork with an upstream PR open, encore is the chatmail/core fork carrying our fix. saku's KeePass-ecosystem direction is recorded above.

## Content, research and idea repos (19)

kunjung, suaka, pustaka, kaji, kaca, gotong, mimpi, anyam, jejak, naga, kaidah, irvan, tapak, tangkai, onda, aiq, paper2repo, sapi, pythonid-10-2026. These are notes, demos, proposals and presentation pages rather than reusable wheels, so no upstream comparison applies to them.

## Legacy forks and pre-2026 sites (19, not examined)

awx, bitstarter, setup, hello-lambda-jakarta, hackathon, typing, org-ruby, pyconapac2024-teaser, minima, devguide, vault-cli, PL101ProjectTemplate, adaptechid, myschoolcampid, old-visi-web, haskell-intro, vnproject.id, irvan-putra, irvan-putra.github.io. Old forks and sites, left as they are; no archiving suggested.

## Read me first

Maintenance is judged from each project's latest release and last commit as observed on 21 Nov 2026; a recent release is not a security audit, and no candidate here has had a proof-of-concept integration. Lingonaut's source availability is unverified. License notes compare identifiers and documented clauses only; they are not legal advice, and no license changes are authorized. "Nothing covers it" claims are bounded to the candidates named beside each repo. For picu, kembang and tayang the purposes are reconstructed from reading their code (single-day experiments without docs) and are labeled as such.

## Sources

- Live repo inventory: https://api.github.com/users/irvan-putra/repos
- https://github.com/gitleaks/gitleaks
- https://github.com/trufflesecurity/trufflehog
- https://github.com/Wilm0r/giggity
- https://github.com/observablehq/framework
- https://github.com/idyll-lang/idyll
- https://github.com/deltachat/deltachat-android
- https://py.delta.chat/
- https://github.com/tasks/tasks
- https://github.com/ActivityWatch/activitywatch
- https://github.com/monicahq/monica
- https://github.com/FossifyOrg/Clock
- https://github.com/schildbach/public-transport-enabler
- https://github.com/grote/Transportr
- https://github.com/seedvault-app/seedvault
- https://github.com/crater-invoice-inc/crater
- https://invoiceninja.github.io/docs/legal/license
- https://github.com/likec4/likec4
- https://github.com/mido/mido
- https://github.com/iSoron/uhabits
- https://github.com/NoneBaiano/OpenRecorder
- https://github.com/deltachat-bot/deltabot
- https://github.com/TeamAmaze/AmazeFileUtilities
- https://github.com/todogroup/repolinter
- https://github.com/maks/MGit
- https://github.com/simonw/llm
- https://docs.openhands.dev/openhands/usage/run-openhands/github-action
- https://github.com/danielmiessler/Fabric
- https://github.com/SYSTRAN/faster-whisper
- https://github.com/ggml-org/whisper.cpp
- https://github.com/mimseyedi/pysentation
- https://github.com/irvan-putra/picu/blob/main/roadmap_generator.py
- https://github.com/irvan-putra/kembang/blob/main/.github/workflows/issue-to-pr.yml
- https://github.com/irvan-putra/tayang/blob/main/background_listening.py
- https://github.com/irvan-putra/tumbuh/blob/main/android/README.md

*Checked 21 Nov 2026 against each project's GitHub repo, README and releases, plus our repos' public READMEs and code. No repo, file or setting was changed; every "your call" item waits for the owner.*

# kaji

Research notes from building personal software, written up so they are useful beyond the project they started in.

Each note states when its facts were checked, links the official pages it relied on, and separates what is verified from what is still a proposal. Free tiers, platform rules and fees change without notice, so treat the check dates as part of the content.

## Recovered examples and visuals

The [`examples/`](examples/README.md) directory keeps three distinct Indomie variants together: the user-selected tabular recipe-box card, the [customizable Tangle recipe box](https://vanipy.com/kaji/indomie/) based on the card's 500 ml recipe, and the separate [400 ml engineering spec](https://vanipy.com/kaji/indomie/instinct/) preserved under its own path. They are distinct versions, not one reconciled recipe. The directory also contains an archived Tumbuh workshop landing-page draft and a conflict-resolution concept. The Tumbuh example is not an active offer; its signup controls are disabled. Conflict screenshots are concepts using invented items and names.

The [synthetic break-even charts](https://vanipy.com/kaji/economics-synthetic/) are a separate public-safe adaptation of an already-public hypothetical example. They are not the original private-valued comparisons.

This repo also includes illustrations alongside the Android-update, application-ID, zero-cash, and conflict-resolution research notes. They are explicitly labeled as illustrations, not product screenshots or measured evidence.

## Research index illustration

![An open blank notebook with blank index cards and tags on a desk.](docs/assets/illustrations/research-index-notebook.jpg)

*Generated illustration for the public research index, not a research record.*

## Notes

- [import zerotrust: an IDSW talk, checked](https://vanipy.com/kaji/zero-trust/) - five slide CVEs checked against primary advisories (one identifier mismatch, score-version caveats), the FBI ARTEX FLASH verified, and OpenZiti's network/host/application deployment models with their trust boundaries. [Source note](docs/idsw-zero-trust-talk.md).
- [Is AI safe? Yes, but: an IDSW keynote, checked](https://vanipy.com/kaji/ai-safety/) - the day-two keynote's references verified (shortcut learning, adversarial examples from pixels to stop signs to sentences, the COMPAS investigation) and its Indonesia-context charts kept to their survey year and population; illustrative numbers and the speaker's framings labeled as such. [Source note](docs/idsw-ai-safety-keynote.md).
- [from air to packets and back: an IDSW talk, checked](https://vanipy.com/kaji/voice-packets/) - a talk's six-stage voice pipeline explained with an original diagram and every number verified: G.711 at 64 kbit/s, 160-byte payloads in 20 ms packets, 172 bytes with the RTP header, 200 as a minimal IPv4 packet, and why the example is illustrative rather than universal. [Source note](docs/idsw-voice-talk.md).
- [(Human) Attention is All You Need: an IDSW talk, checked](https://vanipy.com/kaji/attention/) - the day-two attention-and-agents talk's references verified (Kahneman's WYSIATI, Asch 1946, Neff's three elements), its delegation boundary and Notice-Choose-Delegate-Review-Enough loop summarized, demo figures and slide-cited posts labeled as such. [Source note](docs/idsw-attention-talk.md).
- [Front-End Job is Dying: What I Own as a Design Engineer: an IDSW talk, checked](https://vanipy.com/kaji/frontend-job/) - the design-engineering talk's assembly-versus-judgment argument separated from what verifies: the typed-contract example, the drag-and-drop quality checklist and the virtualization demo check out, while the market framing stays the speaker's position. [Source note](docs/idsw-frontend-job-talk.md).

- [Hamming, Levenshtein and the cost of a missing letter](https://vanipy.com/kaji/edit-distance/) - illustrated reading of arXiv2211.12496v1, theorem assumptions and synthetic name-ranking examples; separate design proposal, no implementation claim. [Source note](docs/hamming-levenshtein-reading.md).


- [Fork or keep: repos versus existing open source](https://vanipy.com/kaji/reuse/) - illustrated comparison tables and [source note](docs/fork-or-keep-open-source-comparison.md), with named candidates, four code-inspected followups and unexamined legacy scope labeled; no adoption, fork, license change or integration proof.

- [Secrets: three jobs, three tools (review)](https://vanipy.com/kaji/secrets/review/) - a design review comparing a phone password vault, OpenBao for app and bot secrets, and SOPS-encrypted repo config, with OpenBao claims linked to its own docs and cost/hosting left unverified; a decision checklist, not an implementation. Nothing is built, installed, moved or paid for; Saku stays parked.

- [Secrets: OpenBao hosting options and a leak recovery plan](https://vanipy.com/kaji/secrets/hosting-recovery/) - first-pass follow-up research: vendor-advertised price floors explicitly not qualified as recommendations, seal-method-dependent unseal tradeoffs, and a generic leaked-secret recovery checklist grounded in GitHub's remediation guidance; no setup, signup, spend or real inventory.

- [Untuk Internal: Bangun Tool Sendiri, Langganan, atau On-premise Opensource? : an IDSW lightning talk, checked](https://vanipy.com/kaji/internal-tools/) - the build-vs-subscribe-vs-self-hosted lightning talk's search destinations and example projects verified (awesome-selfhosted, OpenObserve, Parseable, rustrak, the speaker's central-logs repo), with decision criteria kept as the speaker's heuristics and partly legible slide text marked approximate. [Source note](docs/idsw-internal-tools-talk.md).

- [What Good Mentorship Felt Like to Me as a Junior Engineer: an IDSW lightning talk, checked](https://vanipy.com/kaji/skill-confidence/) - Luthfiyyah Hanifah Amari's four-quadrant skill x confidence framework, its per-quadrant kondisi/solusi detail slides (quadrants 1-3 photographed; quadrant-4 detail not received), the per-skill "not a finish line" close and the lead-role slide, grounded against the Gordon Training four-learning-stages and situational-leadership sources the deck's footer credits; attribution from the closing slide's printed name plus the official agenda, and the slide's "micromanage" wording kept as the speaker's own. [Source note](docs/idsw-skill-confidence-slide.md).
- [Tokenomics of Testing: an IDSW 2026 talk, checked](https://vanipy.com/kaji/test-tokenomics/) - Ivo's evidence-first test review (four questions before writing or deleting a test, per-read token budgeting), with each big number carrying its source-strength label: the 4,000-tests post read as satire (marked as interpretation), the 1.3M figure self-reported, Koc's 417,906 net lines measured with caveats, units kept distinct. [Source note](docs/idsw-test-tokenomics-talk.md).
- [Everything Has an API If You're Willing to Prompt: an IDSW 2026 talk, checked](https://vanipy.com/kaji/prompt-api/) - Bagas Wastu's reported agent-built dashboard from a workout app's private API, framed as the speaker's account with the authorization boundary (own device, own account, token hygiene, fragile private APIs) and deliberately no extraction how-to. [Source note](docs/idsw-prompt-api-talk.md).
- [Mentor sign-off without accounts: what we learned building it](https://vanipy.com/kaji/mentor-signoff/) - reusable design decisions from sanggup's cross-device sign-off: link-carried requests with their readability limit stated in the UI, QR as convenience never the only path, hash-derived response codes that record a conversation rather than identity, per-device state with its no-sync cost stated, and the deploy-allowlist incident that proved a green pipeline is not a live page.
- [IDSW 2026 schedule overview and a learning plan](docs/idsw-2026.md) - the published agenda (checked 2026-11-21, subject to change), a reading of its themes, and a suggested session plan for builders of AI-assisted personal software.
- [Designing an AI chat composer](docs/designing-an-ai-chat-composer.md) - Sketch Together's video about the AI message-input box: controls, attachments, voice, states, mobile behavior and accessibility. Transcript-based reading, not a music-composition model or tested design rule.

- [One review page per decision set](docs/human-review-pages.md) - a reusable method for collecting a person's decisions: one page, limits and non-goals per option, not-proposed items listed with reasons, ticks stored only on the reviewer's device, and narrow interpretation of the reply (an everything-ticked reply is not a blank cheque; money, other people and accounts still need their own approval).

- [Legal clearance for a software mascot](docs/mascot-legal-clearance.md) - what clearance can and cannot mean, free searches, official fee tables for Indonesia, US, EU and Madrid, published US opinion prices; Indonesian opinion prices unknown, not legal advice.

- [Lottie, Rive and Android animation options](docs/lottie-rive-android-animation.md) - in-app motion, mascot tools, authoring costs and documented widget limits; vendor benchmarks attributed, launcher behavior untested. Includes an original decision map.

- [Local-first software](docs/local-first-software.md) - source ideals and unvalidated design proposals.
- [Showing an edit conflict as branches](docs/conflict-resolution-ui-idea.md) - an unbuilt, untested UI idea; sync and merge behavior remain open.
- [Crypto in Indonesia: supervision, seller tax and wallet design](docs/crypto-in-indonesia-regulation-tax-wallet-choice.md) - dated summary of official texts, not financial, legal or tax advice.
- [Bank counts and listed bank tickers in Indonesia](docs/2026-11-17-jumlah-bank-indonesia.md) - dated counts, 48 listing candidates and KBMI thresholds; listing coverage and per-bank capital figures remain unverified.
- [Valuing banks with public data](docs/menilai-valuasi-bank-dengan-data-publik.md) - a proposed method, public-source checks and open modeling limits; no valuation or field study was run.
- [Mother's maiden name in bank services](docs/nama-ibu-kandung-layanan-bank.md) - what checked OJK texts say about digital authentication and SLIK; mandatory-field status and exceptions remain unverified.
- [Measuring the economy independently](docs/mengukur-ekonomi-independen.md) - a proposed research protocol; fieldwork has not been run and example figures remain unverified.
- [BNI Sandbox Tester prototype](docs/prototipe-bni-sandbox-tester.md) - an unexecuted sandbox design and unverified SNAP shortlist; no code or API call was run.
- [WonderOS items and local-first notes](docs/wonderos-items-and-local-first-notes.md) - a project reading; sync behavior was not checked.
- [Proving a sync/merge core with Lean and related tools](docs/proving-a-sync-merge-core-with-lean-and-friends.md) - project claims are attributed, not independently verified; no proof or tool test was run.
- [Receiving payments from Indonesia](docs/receiving-payments-from-indonesia.md) - general provider information, checked 2026-11-16; not financial or tax advice.
- [Shizuku as an app-update option](docs/shizuku-app-updates.md) - a supplement to the app-update comparison; setup and fit were not tested.
- [Changing an Android application ID](docs/android-application-id-change.md) - official-docs reading and migration checks; not tested on a device.
- [The End of Software Copyright](docs/lemley-software-copyright.md) - a critical reading of Lemley's U.S.-focused argument about AI-generated software, authorship, licensing and the limits of its empirical claims.

- [PAN as a model for sharing research tasks](docs/pan-shared-tasks.md) - what Webis's PAN shared-task series and TIRA do (defined tasks, submitted software that can be re-run), and what a small project could borrow.

- [Android home-screen widgets: which views are allowed, and how taps work in lists](docs/android-home-screen-widget-view-and-tap-constraints.md) - Android documentation summary; runtime behavior was not tested.
- [Android app updates without the APK hunt](docs/android-app-updates.md) - the signing-key and prompt rules behind every update route, and five routes compared: in-app updater, Obtainium, own F-Droid repo, Google Play tracks, and manual APKs.
- [How To Make (almost) Anything 2026](docs/htmaa-2026.md) - lecture and recitation summaries, a Hacker News discussion, and explicit coverage limits.
- [How Freebuff says its ad-funded coding agent is paid for](docs/freebuff-ad-funded-ai-tools.md) - company claims on ads, usage limits and paid plans; no evidence of actual cost coverage.
- [Zero-cash break-even method](docs/zero-cash-break-even.md) - a reusable way to price small offers when the real input is time, not cash: cash break-even vs economic break-even, with imputed labor, scenario discipline and fee verification.

- [What it would take to create .jakarta](docs/jakarta-tld.md) - the ICANN path for a city TLD, current .jakarta status, costs, government support rules, and the .amsterdam precedent.
- [Jakarta Smart City feasibility sketch for .jakarta](docs/jakarta-smart-city-feasibility.md) - indicative Rupiah fee conversions and a proposal outline, with BLUD authority, procurement path, demand, and costs left for proper study and review.
- [Synthesia: a falling-notes piano practice tool](docs/synthesia-piano-practice-tool.md) - what its About page says: falling notes, standard MIDI/MusicXML songs, and a donations-to-paid history; company claims not independently verified.
- [Repo Exchange: a public catalogue of GitHub repos ranked by star growth](docs/repoexchange.md) - what repoexchange.web.id's public pages offer (24H/7D/30D star-growth leaderboard, editor's picks, reviewed submissions); no RSS or newsletter at check time, figures not cross-checked.

Project-specific research that only makes sense inside its own project stays in that project's repository instead.

- [NEO App and Excellent: app hosting and managed email](https://vanipy.com/kaji/cloud-and-email/) - a public-source service guide, category distinctions, advertised commercial terms and questions before choosing. [Source note](docs/cloud-and-email.md).

- [Midtrans agent skills and receiving customer payments](https://vanipy.com/kaji/midtrans/) - beta integration guidance, Payment Link versus app checkout, individual merchant requirements, dated fees and payout limits. [Source note](docs/midtrans.md).

- [IDSW community noticeboard](https://vanipy.com/kaji/noticeboard/) - 20 deduplicated job, tool and service leads with verification labels, price discrepancies and private contacts excluded. [Source note](docs/idsw-noticeboard.md).

- [Remote Browser](https://vanipy.com/kaji/remotebrowser/) - open-source browser fleet, API/SDK use, VM requirements, optional LLM harness, production safety and AGPL limits. [Research note](docs/remotebrowser.md).

- [PingPolls: a conversation, a choice and a timing signal](https://vanipy.com/kaji/pingpolls/)
- [Dukkung: one creator page for tips, sales and memberships](https://vanipy.com/kaji/dukkung/)
- [Kubeletto: container hosting, with beta billing questions](https://vanipy.com/kaji/kubeletto/)

- [YukYuk: AI media tools, credits and visibility choices](https://vanipy.com/kaji/yukyuk/)
- [Genesis: schema and GCP infrastructure in one workspace](https://vanipy.com/kaji/genesis/)

- [CodingTool.dev](https://vanipy.com/kaji/codingtool/) - utilities, examples and local/hybrid/server processing limits.

- [Laras Router](https://vanipy.com/kaji/larasrouter/) - model API compatibility, QRIS wallet, token rates and billing/data boundaries.

- [InfoTech Jakarta](https://vanipy.com/kaji/infotech-jakarta/) - public event feed/calendar, verify actual event with organizers.

- [Intelecto](https://vanipy.com/kaji/intelecto/) - textbook/Reader/LMS ecosystem, in-product AI and unconfirmed external access.

- [Models so far](https://vanipy.com/kaji/models/) - six model references, named download sizes, license caveats and runtime limits.

## AI product insights

[41 public product-feedback summaries](https://vanipy.com/kaji/ai-product-insights/) with [sanitized Markdown notes](docs/ai-product-insights.md). Requests and observations, not a roadmap; personal details and private tracking links excluded.

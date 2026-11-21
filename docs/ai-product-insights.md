# AI product insights

A collection of 41 product-feedback submissions about AI assistants: useful output, trust, continuity, delivery and user control. Closely related requests remain separate when they ask for different behavior; follow-ups are kept with their original request.

Collected 23 October to 21 November 2026. Checked against 41 recovered submissions and their follow-ups on 21 November 2026. Sanitized summaries, not verbatim copies. No claim about current implementation, review status or roadmap. Personal examples and private tracking links omitted.

## Sharing and channels

### 1. Per-person access and shared checklists on hosted pages

Let a hosted page be shared with specific people, with checklist progress everyone can see.

### 3. Human-handoff mode in the remote browser

Take over the remote browser yourself to solve verification puzzles, then hand control back.

### 6. Verify a link's actual access state before labeling it

Access labels should be checked against reality - a Google Docs link can be publicly readable, not always sign-in gated.

### 8. Delta Chat with real encrypted-chat support

Support Delta Chat as a channel with Autocrypt-compatible encrypted email, contact invitations and an assistant email address that works there. An ordinary email delivery test is not proof of encrypted Delta Chat delivery. Follow-ups proposed fewer platform-specific messaging constraints than WhatsApp, not an unconditional guarantee that every restriction disappears.

### 11. Delta Chat pins and webxdc mini apps

Follow-on to the Delta Chat request: participant-managed unlimited pins and webxdc mini apps, so the assistant can keep an overview pinned and deliver small interactive tools (recipe cards, dashboards) inside the chat instead of a separate hosted page.

### 15. Delta Chat groups with custom webxdc apps

Delta Chat as a simpler group-chat option for Instinct, with custom webxdc mini apps for shared plans, checklists and dashboards inside the conversation - an alternative to iMessage-only groups.

### 30. Read shared WhatsApp contact cards (bug)

A contact card shared in WhatsApp arrived as an empty message. Instinct should read the contact's name and phone number from the card so you do not have to type them again.

### 31. Encrypted pages without the end user's name

Support encrypted pages without displaying the end user's name, including in page branding and metadata. Users should be able to share encrypted content without also revealing their identity.

## Invitations and community

### 2. Larger referral allowance for community events, and an ambassador program question

More referral capacity for meetups, plus whether an ambassador program exists or is planned.

### 41. Match referral prompts to the remaining allowance

Increase the referral allowance, or avoid prompting members to invite more friends when their remaining invites are limited. This follow-up adds a prompt-behavior correction to the earlier allowance and ambassador-program request.

## Publishing and delivery

### 4. Atomic publishing that keeps the old version available

Keep serving the previous page revision until a replacement is fully live. Publishing should be atomic, such as a blue/green release, rather than exposing a temporary unavailable page.

### 20. Check channel limits before delivering files

Check supported file types before choosing a delivery route. If an app build or source archive cannot travel through the selected channel, offer an appropriate private download route rather than failing late. Delta Chat and iroh were suggested for exploration, not verified as a complete solution.

### 21. Private downloads should be first-class

Deliver private app builds and source archives without requiring a separate code-hosting account. Verify the actual download on a phone, not only that the download page renders. Distinct from checking channel restrictions in advance.

### 35. Version numbers in downloadable filenames

Include version numbers in downloadable filenames. Reusing the same ZIP filename for different builds makes it confusing to identify which version was downloaded.

### 36. Automate recurring release work

When the same publication problem repeats, set up suitable release automation proactively rather than waiting for the user to suggest it. Automation still needs checks of the actual live result.

## Code ownership and access

### 5. Verify author and committer identity

Set both the Git commit author and committer from the user's confirmed GitHub identity before committing, and verify attribution after pushing. Do not assume a default identity is correct.

### 7. One GitHub connect should cover repo creation and pushing, not just reads

The GitHub connection should authorize creating repos and pushing code too - one connect should be enough.

### 10. Instinct-hosted software forge with federation

A hosted forge (perhaps Forgejo, with ForgeFed federation as a goal) so generated code lives there without a personal GitHub account, with easy export or mirroring elsewhere.

### 12. Persistent, narrowly scoped repository access

Ongoing coding work should not require repeated authorization for every push. Validate access before asking for setup, store access safely and explain any remaining approval steps.

### 13. Assistant-owned GitHub account

An assistant-owned GitHub account for creating and hosting generated projects, so users do not need to connect a personal GitHub just to get a working demo - with clear ownership and an easy way to transfer or export the repo to their own account.

### 14. A managed organization for generated projects

Explore a provider-managed GitHub organization rather than a separate personal account for every assistant: separate project repositories and user access, narrowly scoped short-lived access for approved changes, hosted previews, and code export or transfer. Isolation, cost, abuse prevention, handover and access cleanup need explicit treatment. This is a proposed product design, not an announced plan or description of a current system.

### 33. Users should always get the source code

Users should always have access to the source code of apps Instinct builds for them, rather than receiving only a compiled app.

### 34. Apps should use public source repositories

Apps Instinct builds for users should use public source repositories for transparency and security review, with private data and credentials excluded.

### 39. Agree the app namespace before first install

Use a user-approved app name and package namespace from the start, rather than an unrequested platform-branded default. Agree the package identity before the first installation: changing it later can require a separate app and safe data migration.

## Useful output and models

### 9. Keep the recipe-box output style

Positive feedback: Cooking-for-Engineers-style recipe boxes were a reason to join. Preserve their useful structured presentation, including parallel cooking work, and the ability to turn everyday information into a requested format. This is praise, not a bug report.

### 16. Match on-device AI models to the task

Consider small task-specific models, such as object detectors, before proposing a large general-purpose model. Match the actual goal, device capacity and privacy needs; state what the model can and cannot judge.

### 37. Verify transfers, fares and local route details

Transit advice should verify whether transfers stay inside the paid area and what fares apply, rather than recommending another unverified transfer. Explore collaboration with local transit or civic-data providers, including Jakarta Smart City, as a suggestion rather than a confirmed partnership.

## Continuity and communication

### 17. Persistent cross-channel overview, kept updated

A persistent overview page collecting useful links, files and pages from conversations across channels, with context, access labels and current status - updated whenever the assistant creates, shares or changes a resource, without the user having to remind it.

### 18. Progress updates during longer tasks

Brief progress updates during longer tasks: what's finished, what's still being checked, and any blockers - so users are not left wondering whether work has stalled. Useful even when the final result is not ready.

### 23. Recap unanswered progress updates (feature request)

Recap progress updates the user has not specifically responded to, distinguishing acknowledgments from decisions and optional feedback from needed input. Silence is not approval; do not pressure the user to comment on everything.

### 26. State real work status, not just concise wording (bug)

Concise progress wording omitted actual work status - no-more-retry sounded like stopping. Clearly state whether work is continuing, blocked or stopped, what part is unfinished and who acts next. Clarity over brevity.

### 29. Offer realistic paths at a blocker

Explain realistic ways forward and the permission each requires. Check how similar work succeeded before, without assuming consent or promising the old route still works.

### 40. Save work early and checkpoint meaningful changes

Save the first useful version early, then checkpoint decisions, unfinished work and blockers across projects. Show saved-version links without repeated reminders so users do not have to worry that work will be lost when attention shifts.

## Intent and consent

### 19. Limitations are not permission to remove a feature

Accepting a feature's limitations is not a request to remove it. Preserve the stated goal, explain the limits and clarify ambiguous replies before changing scope.

### 24. Respect account-connection boundaries

Repeated delivery failures should not become pressure to connect more accounts. Explain routes that need no extra access, and accept a refusal without pushing another connection.

### 25. Keep requested features when explaining limits

Explain a potential failure and let the user decide whether to test. Ask before removing or replacing requested functionality, and apply corrections consistently across tasks rather than only where the mistake was pointed out.

### 27. A blocker does not mean the user has no options

State whether work is blocked, continuing or stopped, but do not claim the user needs to do nothing without checking. Not knowing a next step does not mean the user has no options. Preserve the user's choice about how to proceed.

### 28. Integration approval is not credential consent

Permission to reconnect an integration does not authorize collecting the account password. Explain capability limits without silently escalating the kind of access requested.

### 38. One clear approval for one saved login

Using one saved login should not require separate approval links for its account address and password. Offer one approval with both fields clearly listed. This request does not authorize revealing or collecting credentials in chat.

## Feedback and visibility

### 22. Built-in personal feedback page (feature request)

Give every user a built-in page with their submissions, statuses and team replies together, and indicate common issues and requests across users without exposing anyone else's private feedback.

### 32. Read feedback pages and verify visible statuses

The assistant should be able to open its own feedback pages and verify the labels users see. A user-added follow-up is not evidence of a different review status. Record data and website labels should agree, without requiring the user to send corrective screenshots.

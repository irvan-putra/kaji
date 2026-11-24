# How always-on bots work: a talk on agents, channels, memory and proactivity

Checked 2026-11-24. Source: a 7-minute video posted by Sarah ([@sarahfim](https://x.com/sarahfim)) in [this X post](https://x.com/sarahfim/status/2124910095133745643), 2026-11-23. The post says she "reverse engineered Grok Bot, Muse, Instinct and more". She says she leads product engineering at Composio, which sells the tool-connection layer she recommends, so read the tool advice with that in mind (the post itself says it is not sponsored).

This note is based on a speech-to-text transcript of the video's audio (the video has no published captions that we found). The transcript is automatic and unreviewed against the video. It is summarized here, not republished. The video's slides and images were not reviewed.

## The post

> i reverse engineered Grok Bot, Muse, Instinct and more, here is everything i learned
>
> in this video: how memory and dreaming works; setup iMessage for your agent; make bots proactive; give your agent its own computer, browser and access to 1700+ apps
>
> btw this is not sponsored, i mention a few tools you can use: @PhotonHQ @thelinqapp (iMessage channels), @browserbase @browser_use (agent browser), @CopilotKit (chat interface), @e2b @exedev (cloud terminal), @try_glen (memory), @NousResearch @openclaw @0penBot (open source bots)

Mentioned accounts, as listed in the post: PhotonHQ and thelinqapp (iMessage channels), browserbase and browser_use (agent browser), CopilotKit (chat interface), e2b and exedev (cloud terminal), try_glen (memory), NousResearch, openclaw and 0penBot (open-source bots). We did not check what any of these products do; the list is the author's.

Metrics seen on the post's page when fetched (2026-11-24): about 112,000 views, 1,856 likes, 97 replies.

## What the talk says (the speaker's account)

1. **Chat to agent.** A model plus its previous output is chat. Feeding the output back in so it can decide whether to continue, with a stop signal, makes a loop. The model asks for a function call, the program runs it and returns the result. Context plus tools is what she calls the harness, so comparing harnesses means comparing how they manage context and give tools to the model.
2. **Tools: terminal, browser, direct API.** A terminal (on the user's machine or a sandbox) lets an agent do almost anything. A browser has to load, process and click, so it is slower than calling an API directly; she recommends an API or command-line route wherever one exists. Most popular bots combine all three. Authentication is the hard part: API keys, or OAuth, which needs a developer app that sometimes costs money or approval. She recommends Composio for this (claims: over 1,700 apps, a free tier of over 100,000 tool calls a month; not checked here). Because tens of thousands of tools do not fit in a context window, her described pattern is a search step to find a tool, then an execute step to run it.
3. **Channels.** Different channels (text message, email, phone app) talk to the same agent. She says setting up iMessage was easier than she expected and names Photon Spectrum and Link as the SDKs; for a chat interface she suggests CopilotKit rather than building from scratch. She notes some popular agents have no web interface at all and names Instinct among them (the transcript also says "Po", probably another assistant; unverified). Her point: text, email or a phone app makes the agent feel like its own entity.
4. **Memory.** Closed-source memory is hard to see, but she says it is usually (a) context loaded automatically each turn and (b) tools the agent uses to look further. Three layers: where it is stored (files or a database), how it is searched (keywords or vectors), and extras on top (dreaming, graphs). As an example she describes an open-source bot (the transcript says "OpenClaude", most likely OpenClaw from the post's mentions; unverified): four files loaded at every session start (a personality file, an identity file, a user-preferences file, and a long-term memory file the agent writes itself), plus daily note logs that are not loaded and must be searched with the terminal. Every night at 3:00 a.m. it "dreams": it reads the daily notes and decides what to add to the long-term file. She also mentions a managed memory service, Glen, that gives her agent context from coworkers' agent sessions.
5. **Proactivity.** What makes a bot "always on" is reacting without a prompt. The first approach: a scheduled job that wakes the agent about every 30 minutes. The second: wake on an event, such as a new support ticket, using triggers. Most popular bots let users schedule things and react to events, and almost all also wake on a regular cadence by default.
6. **Permissions.** An agent with your terminal or logged-in browser can do what you can, including deleting an account. Options she gives: a separate computer or browser logged into accounts you do not care about; scoped API connections (read email but not delete it); and a layer in between that blocks specific tools even when the connection allows them (she names Composio for that).

## Replies seen on the post

Fetched 2026-11-24 from a public mirror of the thread ([x.latent.space/sarahfim](https://x.latent.space/sarahfim)); only the author's own replies are quoted. Other repliers are not named here: most were short praise (for example that it was a clear explanation or a good talk). One reply asked whether Composio can onboard users to connect all 1,700 apps; the author answered that if you pass Composio tools to your agent, you can ask it to connect you to anything and it gives you a link to connect in the chat ([author's reply](https://x.com/sarahfim/status/2124910095133745643), 2026-11-23). That is her claim about her own product, not tested. Two replies that appear to come from product accounts (one of them in the post's mention list) are marketing-style praise and are not treated as evidence.

## A reusable reading

Our interpretation, not tested:

- The loop, the memory layers and the wake-up styles are generic and match what several open assistants describe; they are a useful checklist, not a spec.
- Memory has a cheap, inspectable core: a few plain files loaded every turn, plus a searchable log. Dreaming is the only layer that needs a model.
- Permissions advice (scopes, blocking tools, separate accounts) fits any assistant that acts for a person. A confirmation step before consequential actions is a simple version.
- Several recommendations are paid or vendor-hosted services. Whether a free, local alternative exists for each has not been checked.

## Scope and limits

Not verified: any claim about how Grok Bot, Muse, Instinct or the open-source bot works inside; the Composio numbers; the nightly time; product descriptions of the tools mentioned. The author's claims are the author's. The video was not republished. A full verbatim transcript exists but is not published here, because reproducing the whole talk is copying it; ask if you want it.

## Sources

- [X post and video by @sarahfim](https://x.com/sarahfim/status/2124910095133745643), 2026-11-23.
- [Thread mirror with replies](https://x.latent.space/sarahfim), fetched 2026-11-24.
- Post text and media metadata via the public fxtwitter API (`api.fxtwitter.com/sarahfim/status/2124910095133745643`).

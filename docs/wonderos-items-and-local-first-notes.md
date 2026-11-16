# WonderOS: an "itemized" personal computing research project

Status: the project's own pages, read 2026-11-16. This is a short reading note about what the project says it explores, not an assessment of whether the ideas work. It complements the local-first software note.

## What the project says
- WonderOS is described as "an ongoing research project by Alexander Obenauer" exploring an itemized user environment for personal computing; it also has hardware and society strands. https://wonderos.org/
- The core idea: "The item is an alternative boundary for our digital things". Items are separate from the interfaces that render them and the services that supply them, and the whole system is composed of items. https://wonderos.org/
- It calls its users "operators", who can rearrange the system.
- The core implementation is described as a virtual machine written in C with its own language, using an "Item Store" for storage, "a chronological database of facts". https://wonderos.org/
- The operator's handbook shows items that can be in more than one place at once, for example a todo that is in both a project list and on a date. https://wonderos.org/hello/
- The author's own page frames the project as explorative, not prescriptive, and as aiming to show that better answers to its questions exist. https://alexanderobenauer.com/weekly/20230114/

## Why it is related to local-first software
Both treat the user's own data as the centre, kept apart from any one service. WonderOS is a design experiment about the data model (items and where they appear); the local-first essay is about ownership and sync (offline use, multiple devices, collaboration). Whether WonderOS addresses sync was not checked here.

# Local-first software: exploration notes

Status: exploration. Source checked 2026-11-16: https://www.inkandswitch.com/essay/local-first/
Provenance: the seven ideals below are from the essay. Everything under "Design proposals" is the author's own proposal, not something the essay proves.

## The essay's seven ideals
No spinners; work not trapped on one device; the network is optional; collaboration; the Long Now; security and privacy by default; user ownership and control. The essay compares files, web apps, cloud sync and Git against them.

## Design proposals (unvalidated)
- Keep data on the device and treat servers as optional.
- Archive instead of delete. This keeps data longer but does not by itself guarantee history or recovery after a bad merge; that needs versioning or backups too.
- Show a conflict as two versions to choose between, not as an error.
- A possible distribution architecture: a static host for files plus a bot for update announcements. Current free-tier limits and pricing of any host were not verified here; see the [tindak research notes](https://github.com/irvan-putra/tindak/tree/main/docs/research) for storage and bridge options and re-check limits before relying on them.

## Backlog (unresolved)
Android version file naming, version icons and automatic updates, and free-host coverage and limits. These need their own note and fresh checks. The existing kaji Android-updates note is not equivalent coverage.

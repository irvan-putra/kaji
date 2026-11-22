---
id: human-review-pages
type: research-note
---
# One review page per decision set (method note)

Written 22 Nov 2026. A reusable method for asking a person to review options without a meeting, a form tool, or an account. Developed while building the Sanggup and Kaji sites; no conversation content is reproduced here.

## The method

1. **One page per decision set.** Everything the person needs is on a single public page: what exists today, what is proposed, and what each option would mean. No accounts, no app to install; the page works on a phone.
2. **Separate what is done from what is proposed.** Each card says plainly whether it describes something that already exists or something that would only happen if chosen.
3. **Every option states its limits and non-goals.** Each option carries a "what it deliberately does not do" alongside what it does, so a choice is made with its tradeoffs visible, not discovered later.
4. **List what is not proposed, with reasons.** Deliberately excluded directions (and why) are on the page, tickable as "revisit" rather than silently absent.
5. **Ticks stay on the reviewer's device.** Selections are stored in the browser only; the page sends nothing anywhere. A "copy my review as text" button turns the ticks into plain text the reviewer pastes back into whatever chat they already use.
6. **Interpret the reply narrowly.** A ticked decision card selects that decision. A ticked open question is not an answer to it; it still needs one. A "revisit" tick is interest in a future design discussion, not permission. Scopes that touch money, other people's data, accounts or outreach are never implied by any tick; they need their own explicit approval when they come up.
7. **Follow through exactly, then report.** Build only what was selected, keep excluded items excluded, and report what is done versus still pending, with the page updated if the decision set changes.

## Why it works

- The reviewer answers in one pass, at their own time, with the full picture in front of them instead of a chat drip.
- Limits travel with the options, so approval covers the tradeoffs too, not just the headline.
- The text reply is a durable, quotable record of exactly what was chosen, which later work can be checked against.

## Failure mode this guards against

An everything-ticked reply is not a blank cheque. When every card comes back selected, including revisit items and open questions, the correct reading is: build the buildable options, schedule the revisits as design discussions, and still ask before anything that costs money, touches other people, or creates accounts. The method's value is precisely that it makes those classes of item visually distinct, so the narrow reading is defensible.

## Live examples (22 Nov 2026)

- https://vanipy.com/sanggup/review/tools/ - placement review for optional tools in Sanggup
- https://vanipy.com/sanggup/review/ecosystem/ - feature options review (mentor, study group, community)
- https://vanipy.com/kaji/secrets/review/ - secrets architecture decision review
- https://vanipy.com/kaji/secrets/hosting-recovery/ - research follow-up with its own decision cards

# Designing an AI chat composer

Checked 2026-11-20. Video: [Designing a composer](https://youtu.be/8q0pwh98qmU), published by Sketch Together. This note is based on the video's available transcript and YouTube metadata, not a frame-by-frame visual review.

Here, "composer" means the message input where someone writes to an AI. It does **not** mean a music-composition model. The video follows the many linked decisions hidden inside what looks like a simple text box.

## What the video covers

- **The first controls:** send-button wording, icons, placeholder text, typography, width, background, border and corner shape. A small choice changes nearby choices, rather than standing alone.
- **Adding capabilities:** images, files, web search, tools and a model picker compete for space. Moving controls into a plus menu reduces visible clutter but raises questions about discovery and menu behavior.
- **Voice and attachments:** voice conversation and dictation need distinct meaning. Attachments need placement, removal and upload states. A button that changes from voice to send saves space but must still be understandable.
- **Writing behavior:** Enter versus a new line, growing input height, pasted text, file drops, slash commands and mentions all affect the same writing flow.
- **Work in progress:** sending, thinking, failure, stopping, queuing and interruption need clear behavior. Some status belongs in the conversation instead of being repeated in the input.
- **The empty and active chat:** greetings, suggestions and the move from a centered input to a bottom input introduce more choices. The narration questions personalization that feels intrusive.
- **Competing demands:** legal, marketing, sales, support and other teams can turn the composer into a crowded display area. The designer has to choose what stays out.
- **Accessibility:** visible focus, names for icon-only controls and usable touch targets are part of the design, even when they challenge an earlier visual choice.

## A reusable reading

This is our interpretation, not a tested product recommendation:

1. Define the core writing and sending behavior before adding secondary tools.
2. Review states and transitions as carefully as the resting layout. A clean screenshot does not establish clear upload, failure or interruption behavior.
3. Treat desktop and phone input as different interaction conditions. Hover-only controls and keyboard shortcuts do not cover touch use.
4. Keep a record of decisions and their tradeoffs. Repeatedly moving a control without a clear reason can hide the underlying problem.
5. Test discovery, labels, focus and touch targets with people. The video's playful choices are not evidence that one icon, width or Enter behavior is universally best.

## Scope and limits

This is a reference note about interface design, not a specification, implemented prototype or usability study. No software was changed as part of this addition. The video was not downloaded or republished, and its transcript and images are not reproduced here. No claims are made about measured conversion, accessibility compliance or user preference.

## Sources

- [Original video: Designing a composer](https://youtu.be/8q0pwh98qmU), Sketch Together. Primary source for the topics summarized above.
- [YouTube metadata for the supplied video](https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=8q0pwh98qmU&format=json). Confirms the displayed title and publishing channel.

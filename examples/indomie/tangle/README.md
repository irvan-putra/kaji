# Indomie Mi Goreng: the customizable recipe box (Tangle edition)

A third variant of the Indomie pages in this repo: the recipe-box card rebuilt
as a reactive document with [Tangle](https://github.com/worrydream/Tangle)
(Bret Victor's library for explorable explanations, MIT licensed, vendored
under `lib/` with its original headers).

Every blue number on the page is draggable, and the blue on/off flags are
clickable. Changing them rewrites the whole card: noodle grams, total water,
chili fractions, side threads, runtime, warnings, and serving count.

Variables:

- `packs` (1-6): noodle packs; scales grams, water, seasoning sets, servings
- `waterPerPack` (250-750 ml, step 50): defaults to the card's 500 ml
- `pedas` (0-5): mapped to chili-pack fractions per the card
  (0 = no chili, 1/2 pack = level 3, full pack = level 5 / segfault)
- `withEgg` / `eggs` (1-3), `withSosis` / `sosis` (1-3): side threads
- `keepTbsp` (0-3): boil water kept for the paste

The 3:00 boil never scales with packs. Past four packs the page quotes the
reviewer-attention warning from the engineering spec.

## Sibling variants

- `../` - the interactive engineering spec (checkboxes and a spice slider)
- `../images/indomie-recipe-box-v2.jpg` - the printable recipe-box card this
  page is a live version of

## Files

- `index.html` - markup, Tangle model, and the two small custom classes
  (`TKFlag`, `TKSingularPlural`)
- `style.css` - card styling; the table flattens into a stacked list under
  560 px so nothing overflows on a phone
- `lib/` - Tangle 0.1.0, TangleKit, mootools, sprintf, BVTouchable
  (MIT, (c) 2011 Bret Victor)

No build step; it is a static page and works from `file://` too.

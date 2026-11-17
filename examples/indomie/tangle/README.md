# Indomie Mi Goreng: the customizable recipe box (Tangle edition)

This is the main interactive Indomie page, published at `/kaji/indomie/`. It keeps the card's left-to-right parallel cooking threads and merged cells, while Tangle (Bret Victor, MIT license; vendored libraries retain their headers) lets you retune portions, water, spice, eggs and sosis. The markup and page stylesheet live one directory up as `../index.html` and `../style.css`; the vendored Tangle libraries remain here under `lib/`. On narrow screens, swipe horizontally through the table to follow the threads.

A second, separate version is the engineering spec in `../instinct/` (published at `/kaji/indomie/instinct/`). The static tabular recipe card remains at `../images/indomie-recipe-box-v2.jpg`. These recipes have different water, draining, and spice defaults; keep them labeled as separate versions.

Every blue number on the page is draggable, and the blue on/off flags are clickable. Changing them rewrites the whole card: noodle grams, total water, chili fractions, side threads, runtime, warnings, and serving count.

Variables:

- `packs` (1-6): noodle packs; scales grams, water, seasoning sets, servings
- `waterPerPack` (250-750 ml, step 50): defaults to the card's 500 ml
- `pedas` (0-5): mapped to chili-pack fractions per the card
  (0 = no chili, 1/2 pack = level 3, full pack = level 5 / segfault)
- `withEgg` / `eggs` (1-3), `withSosis` / `sosis` (1-3): side threads
- `keepTbsp` (0-3): boil water kept for the paste

The 3:00 boil never scales with packs. Past four packs the page quotes the reviewer-attention warning from the engineering spec.

## Files

- `../index.html` - page markup, Tangle model, and custom classes (`TKFlag`, `TKSingularPlural`)
- `../style.css` - card styling; the table flattens into a stacked list under 560 px so nothing overflows on a phone
- `lib/` - Tangle 0.1.0, TangleKit, mootools, sprintf, BVTouchable (MIT, (c) 2011 Bret Victor)

No build step; it is a static page and works from `file://` too.

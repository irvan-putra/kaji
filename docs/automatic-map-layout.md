# Automatic layout for transit-style maps (research for Tuju and future maps)

Checked 2026-11-23. Tuju is the case that prompted this note. Nothing here was adopted, installed in a project, paid for, or used to change Tuju. Tuju's layout fix is a separate, ongoing piece of work.

## What the map needs

From the feedback on Tuju 0.2.8, the layout has to do six things at once:

1. Keep parallel lines apart (spacing), including walking links beside route lines.
2. Cross as few times as possible, and mark the crossings that remain.
3. Use few bends (no needless turns).
4. Keep every line clear of every piece of text, including multi-line notes.
5. Use the page well (less empty space, less scrolling).
6. Keep the real connections: layout may move things, never change which stop joins which.

Today the Tuju generator (`tools/build_route_map.py`) places each column by hand with fixed x/y values and label offsets, then tests check some geometry afterwards. Every fix is a manual nudge, and a nudge for one problem tends to create another. The extracted data (`data/route-stops.json`) holds stop id, name and sequence only, with no coordinates.

## Short answer

No single free tool does all six. The best fit is to split the job:

- **Shape of the network** (bends, crossings, shared spines): LOOM and octi, or a small purpose-built solver.
- **Walking links and text clearance**: obstacle-avoiding connector routing (libavoid), or the same idea in a few dozen lines of grid search.
- **Checks**: automated scoring of crossings, bends, line spacing and line-versus-text overlap, so every change is measured, not eyeballed.

The cheapest first step is the last one, because it works with the current hand-placed generator and gives any future engine a target to beat.

## Options

### 1. LOOM suite (ad-freiburg/loom): best match for crossings, shared spines, bends

- Source: https://github.com/ad-freiburg/loom , GPL-3.0, C++, 317 stars when checked.
- Pipeline of command-line tools reading and writing GeoJSON line graphs: `topo` (merge overlapping lines into one shared segment), `loom` (order the lines inside a shared segment to minimize line crossings), `octi` (turn the graph into a schematic with horizontal, vertical and 45-degree lines), `transitmap -l` (render SVG with labels).
- Papers behind it: Bast, Brosi, Storandt, "Metro Maps on Octilinear Grid Graphs" (EuroVis 2020, https://doi.org/10.1111/cgf.13986) and "Metro Maps on Flexible Base Grids" (SSTD 2021). Only the titles and the README were read, not the papers' full text.
- Why it fits: a shared spine drawn once with several lines side by side is exactly what Tuju's 4/6/7E and 10/7F stretches are, and ordering lines inside a spine to avoid crossings is what `loom` is for.
- **Tested here (small, one-off):** built from source (commit 1e47578, dated 2026-07-24) with cmake and g++, then ran two inputs through `loom | octi | transitmap -l`: the bundled Freiburg example, and a made-up 8-stop, 3-line toy graph with one shared stretch ([toy.json](../site/map-layout/toy.json)). Both finished without errors (about 0.2 s for Freiburg on a 2-core sandbox; one run, not a performance measurement). Renders below. In the toy, the three lines run side by side through the shared stretch and the drawing uses only straight vertical and horizontal segments. In the Freiburg render the shared stretches are bundled, with 45-degree diagonals.

![LOOM output for the bundled Freiburg example, octilinear, with shared stretches bundled](../site/map-layout/loom-freiburg.png)

![LOOM output for a made-up 3-line toy graph with one shared stretch](../site/map-layout/loom-toy.png)

- **Not tested:** Tuju's real network, labels (no station names appear in my two renders, so label behaviour is unknown), and walking links (the tool has no walking-link concept; modelling one as an extra dashed "line" is an untested idea). Real input needs stop coordinates, which means re-reading `stops.txt` from the GTFS feed.
- Caveat: `octi` keeps the map roughly geographic. Tuju's current design deliberately straightens each corridor into its own column. Using LOOM would change the look of the map, so that is a design choice for Irvan, not an automatic upgrade.
- License: LOOM is GPL-3.0 (per its GitHub page); Tuju's repository carries the AGPL-3.0 text. Whether and how the two combine was not checked and is unresolved here; running LOOM only as a separate build-time command is a different case from copying its code, but that distinction has not been confirmed against the licence text.

### 2. Mixed-integer programming for metro maps (Nöllenburg and Wolff)

- Paper: "Drawing and Labeling High-Quality Metro Maps by Mixed-Integer Programming", IEEE TVCG 2011, https://pubmed.ncbi.nlm.nih.gov/20498505/ . Only the abstract page was read.
- yWorks wrote up an implementation using this model with a solver (lpsolve, then CPLEX, which was quicker): https://www.yworks.com/blog/automatic-metro-map-generation . Their post says the full algorithm is not in the yFiles library and the linear-programming part depends on third-party software, and yFiles itself is commercial.
- This is the most complete formulation (bends, line length, relative position and labels together), but no ready free implementation was found. Using it would mean writing our own model with a free solver. Untested.

### 3. libavoid (Adaptagrams): for walking links and text clearance

- https://www.adaptagrams.org/documentation/libavoid.html and https://github.com/mjwybrow/adaptagrams . C++ library for "object-avoiding orthogonal and polyline connector routing"; used in Inkscape's connector tool. The page says there are no official releases yet, though the code is described as stable. Licence: LGPL 2.1 or later, per the header of `router.h` and `LICENSE.LGPL` in the repo (https://github.com/mjwybrow/adaptagrams/blob/master/cola/libavoid/router.h). The README also mentions commercial licences.
- Idea: treat every label and note as an obstacle box, route each walking link around the boxes with few bends, and let the router separate parallel segments. This targets the "lines touching text" and "walking link wanders across the map" complaints directly.
- Untested. It is C++, so using it from Tuju's Python build means a wrapper or a small compiled helper.

### 4. ELK (Eclipse Layout Kernel, elkjs)

- https://github.com/kieler/elkjs and https://eclipse.dev/elk/reference/algorithms/org-eclipse-elk-layered.html . JavaScript port of a layered layout algorithm with ports and orthogonal edge routing, built for directed node-link diagrams.
- Fits columns and arrows well, but it lays out graphs where each connection is an edge, not metro lines that share segments, so Tuju's shared spines would need workarounds. Its licence is EPL-2.0; a GitHub issue asks about EPL-2.0 and GPLv3 compatibility (https://github.com/kieler/elkjs/issues/312) and was not resolved here. Untested.

### 5. Others looked at and set aside

- **d3-tube-map** (https://github.com/johnwalley/d3-tube-map , BSD 3-Clause): draws London-style maps, but the coordinates are given by hand, so it does not solve layout.
- **metroflow** (https://github.com/bartromgens/metroflow): interactive map editor on canvas; the README calls it pre-alpha.
- **WebCola** (https://github.com/tgdwyer/WebCola): constraint-based force layout in the browser; useful for non-overlap and alignment constraints, not metro-specific. Untested.
- **OGDF** (https://www.ogdf.uni-osnabrueck.de/license/ , GPL 2 or 3): large C++ graph drawing framework with orthogonal layout; heavy for this job.
- **Graphviz** (`splines=ortho`, https://graphviz.org/docs/attrs/splines/): generic graph layout; no notion of lines sharing a corridor.
- **Transit app's generated maps** (https://blog.transitapp.com/how-we-built-the-worlds-prettiest-auto-generated-transit-maps-12d0c6fa502f/): a good description of a pipeline (shapes, OSM matching, then drawing), but proprietary, so a source of ideas only.

## Recommended path, in order

1. **Measure first (no new dependency).** Extend Tuju's existing geometry tests into one score: count of crossings, count of bends, minimum gap between lines of any colour, and any overlap between a line and a text box (using each label's real width, including wrapped notes). Print it for every build. This turns "try to decrease crossings" into a number that must go down.
2. **Route walking links by search.** Put all label boxes and route lines on a coarse grid as blocked cells with a margin, then find each walking link with A* that charges for bends and crossings. This is the same idea as libavoid in a small amount of Python and keeps the build dependency-free.
3. **Pack columns by search.** Treat each corridor column as a movable block and minimise total link length plus the score above. Pure Python local search is enough at Tuju's size.
4. **Try LOOM as an experiment.** Export the network with coordinates, run `topo | loom | octi`, and compare its crossings and bends against the hand layout on the same score. Adopt only if it wins and Irvan likes the look.

Items 1 to 3 are proposals; none has been built or run on Tuju. Item 4's tool has been run on example data only.

## Open questions

- Should Tuju stay a "column per corridor" diagram, or is a more geographic octilinear map acceptable? This decides whether LOOM is a candidate at all.
- Are stop coordinates from the public GTFS feed acceptable as build input? (They are public data; the cost is a larger extract.)

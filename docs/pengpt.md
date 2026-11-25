# PenGPT: a generative transformer for handwriting and sketches, explained

Checked 25 November 2026. Summarized from the blog post only; the companion paper was not re-read.

PenGPT is a November 2026 project by Sam Greydanus: small transformers that write and sketch from text. A 6M-parameter model writes print and cursive and picks up the handwriting of someone it has never seen from a few of their words; a 54M-parameter model draws from a typed prompt. Greydanus frames the effort as 80% data, 15% speed and 5% architecture, his first project that follows Rich Sutton's Bitter Lesson.

| Piece | What it is |
| --- | --- |
| Pen strokes as symbols | Pen points snap to a grid, so a word becomes a walk in eight directions plus pen-down and pen-up: ten symbols. The same tokenizer handles handwriting and drawings. |
| Tokens | Byte-pair encoding merges common runs of moves into tokens; the post's example word goes from 156 moves to 47 tokens, sequences 3.2x shorter. |
| Model | A plain decoder-only transformer that cross-attends to what it is told: the text for handwriting, a SigLIP 2 vector for drawings. |
| Sizes | 6M parameters (handwriting), 54M (drawing); about 8 and about 35 minutes to train on an 8xA100 node. |

## The data

- Handwriting: 495,590 words by 1,255 writers, mostly two research collections plus old letters and diaries from public archives. A vision-language model finds legible pages and transcribes them, the pages get cut into words, InkSight traces each word back into strokes, and checks throw out bad traces; a third to a half survive.
- Drawings: 477,670 sketches from ten public datasets; the best 0.5% of Quick, Draw!'s 50 million were kept.
- The datasets are not released; the paper's appendix explains how to build them.

## What the ablations say

- Cutting handwriting data to a tenth: score worsens by +0.050 nats per pen move, style rank 1.9 to 3.0.
- No augmentation (drawings): the model stops following prompts; matches-caption 43% to 6%.
- One word per sequence (handwriting): style rank 1.9 to 6.0; the model can no longer pick up a hand.
- No pen position: nothing for handwriting (+0.001), a small cost on drawings.
- No BPE merges: score slightly better (-0.010); the merges buy speed, not quality.
- 60x the vocabulary or twice the parameters: no meaningful change.
- A Graves-style LSTM on the same tokens: a bit behind on handwriting and still picks up new hands; well behind on drawings.

## Picking up a new hand

- Each training sequence holds up to four words by one writer, so at sampling time a few real words are enough to continue in that hand: no style encoder, no fine-tuning.
- From a photo: InkSight traces a few of its words and one new writer vector is fit to the traces, with the rest of the model frozen. Shown for a Sara Teasdale letter and a 1989 NIST form.

## Reading the letters

- One cross-attention head in layer 4 puts 81% of its attention on the letter being written; silencing it costs more than silencing any other head.
- The same head reads a cursive t twice: once for the stem and again for the cross, which in cursive comes only after the word is finished. No head specializes in cursive or print.

## Captions are not optional

- A model trained on picture vectors alone has the best likelihood of the three compared and draws scribbles.
- The post's reason is geometric: SigLIP's sketch vectors sit in a narrow cone, nearly at right angles to its text vectors.
- Labels are enough to draw labels (78%) but only captions get phrases (43% against 10%).

## What it cannot do

- It blends but does not bind: "facing left" and "facing right" give the same drawing (caption cosine similarity 0.999).
- Sampled handwriting is less legible than real: 54% against 66% by OCR.
- Stroke order is a model's guess, not a record, since most handwriting was traced from scans.

## Why this note exists (our take, not the author's)

The project is a clean data point for small, task-specific models: the wins came from data volume, cleaning and augmentation rather than architecture. The ablation table doubles as a checklist for stroke- or sequence-modeling work: check data scale, augmentation and context length before touching the architecture.

## Scope

The post's images are the author's and are linked, not copied. The author notes some sample figures were picked by eye from the best third of samples and includes an unpicked figure as the honest version. No code was run; the datasets are not released.

## Sources

- https://greydanus.github.io/2026/11/12/pengpt/

## In-browser demo

https://vanipy.com/kaji/pengpt/demo/ hosts the author's browser demo: the 41.7 KB app file copied unmodified (plus an attribution comment; Apache-2.0) and a byte-identical copy of pengpt.npz (81,528,834 bytes, sha256 d678fc79c86344f17cfa1419e3ec76ee151dfd7f153026188ec445d101bfd288). The npz is committed in the repo (under GitHub's 100 MB file limit) because GitHub release assets send no CORS headers, so a browser page cannot fetch them cross-origin; the kaji release pengpt-demo-2026-11-25 keeps a second mirror. The demo loads the file with HTTP range requests, so handwriting pulls only about 6 MB and drawing pulls the rest on demand. The start card states the sizes before any download. The author's README describes the weights as open; no separate weights license file ships with the project.

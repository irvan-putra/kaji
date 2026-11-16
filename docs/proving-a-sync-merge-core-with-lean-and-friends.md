# Could a sync/merge core be proved correct? Lean, Haskell, and code-review tools

Status: project pages read 2026-11-16. This is a map of what exists and what a proof could and could not cover. It does not test any of these tools, and no proof was written for any project.

## Proving that replicas converge
- Lean 4 is described by its reference as an interactive theorem prover and also "a pure functional programming language". https://lean-lang.org/doc/reference/latest/
- lean-yjs, per its own README (not independently audited): "a Lean 4 formalization of the Yjs sequence-integration algorithm" that "proves that replicas converge when they process the same operations under causal delivery." Its README also describes differential tests: it builds a Lean executable and runs JavaScript-based tests against Yjs. https://github.com/iasakura/lean-yjs
- crdtlib, per the project's own site (not independently audited): a Lean 4 library of combinators where each "preserves convergence, so whatever you assemble from them is a CRDT by construction: verified in Lean and executable." https://prg-grp.github.io/crdtlib/
- Older precedent in Isabelle: "A framework for establishing Strong Eventual Consistency for Conflict-free Replicated Datatypes" (Gomes, Kleppmann, Mulligan, Beresford, 2017), in the Archive of Formal Proofs. https://isa-afp.org/entries/CRDT.html

## What such a proof would and would not cover (a reasoning note, not a source claim)
- A proof of this kind covers the algorithm as modelled: for example that replicas applying the same operations end in the same state, under an assumed delivery model (lean-yjs states causal delivery).
- It does not by itself cover encryption, transport, UI, or whether shipped code matches the model. A separately implemented Java or JavaScript version needs additional assurance that it matches the model; differential testing (as lean-yjs does) is one approach, not a proof by itself. Whether Lean can generate Java or JavaScript was not checked.

## Haskell as an implementation language
- An LWN reader comment (1 April 2026) claims GHC's WebAssembly backend arrived in GHC 9.6 and "has matured significantly". This is an unverified reader comment, not an official GHC source, and no capability or recommendation is drawn from it. https://lwn.net/Articles/1065919/
- Eta (Haskell on the JVM): the repository page read does not state its maintenance status, so no claim is made. https://github.com/typelead/eta

## Review tools mentioned alongside
- cargo-crev describes itself as "a cryptographically verifiable code review system for the cargo (Rust) package manager": reviews by people you trust, not an automatic scan. https://github.com/crev-dev/cargo-crev
- Unison identifies each definition by a hash of its syntax tree (512-bit SHA3); names are separate metadata. Same hash means same code, not safe code. https://www.unison-lang.org/docs/the-big-idea/
- A Lean WebAssembly build: a Lean pull request "feat: release web assembly" was merged in November 2023. Its maturity was not checked. https://github.com/leanprover/lean4/pull/2855

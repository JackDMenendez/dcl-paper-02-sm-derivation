# notes/

Working theoretical notes that the paper either cites (via the audit
table's evidence column) or builds on. Notes are durable -- they
survive paper revisions -- and are the natural home for material that
is too long-form for a section but too detailed to lose.

## Conventions

- One topic per file. Filenames are short and semantic
  (`born_rule_uniqueness.md`, not `notes-2026-04-01.md`).
- Markdown, not LaTeX. Notes are read in the editor; if a note grows
  enough mathematics to warrant a render, promote it to a paper
  section instead of upgrading the note format.
- Short header at the top: title, one-line purpose, status (DRAFT /
  STABLE / SUPERSEDED). When a note is superseded, leave it in place
  with a pointer to the replacement -- the project history is part of
  the project.
- Reference paper sections by label (`see \S\ref{subsec:scope}` ->
  prose: "see section subsec:scope"), not by section number.

## Upstream flow

Findings during Paper~II work that touch **notation** (new symbols,
operators, basis conventions), **algebra** (commutation relations,
structure constants, Lie-algebra closures), **topology** (homotopy
of tick-rule paths, winding numbers, cohomology of automorphism
orbits), or **balanced $\mathcal{A}=1$ equations** (reaction-style
equations conserving $\mathcal{A}=1$ across both sides) should be
captured as a note here -- even minimally -- so they can flow
upstream to the parallel formalization effort in
`external/research/Notes/balanced_equations/` and the topical notes
alongside it (`color_and_emergent_forces.md`,
`lattice_as_inference_engine.md`, ...). A short stub with one
paragraph of "what was observed and why it matters" is fine for a
first capture; expand later if the finding grows.

See CLAUDE.md "Cross-references to physics-research" for the
junction setup. The Paper~I follow-on catalogue
(`external/dcl/notes/follow_on_implications.md`) item #13 ("Operation
Algebra of the Discrete Causal Lattice") and item #14 ("Balanced
Equations and Birefringent Channels") are the framing parents for
this rule; this paper is item #16 of the same catalogue.

## Examples

`example_note.md` shows the recommended structure -- replace it with
your own once the project has real content to capture.

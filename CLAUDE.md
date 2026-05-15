<!-- markdownlint-disable MD022 MD025 MD033 MD060 -->
# CLAUDE.md -- Working Brief for Claude Code

> Project: Paper II of the A=1 Discrete Causal Lattice series --
> SM Gauge Derivation

This file is the project memory for Claude Code. Keep it updated so a
new conversation can continue work without the full chat history.

---

## CURRENT STATUS (2026-05-08) -- v0.1-DRAFT

Paper II is freshly scaffolded from `dcl-paper-experiment-template`.
The repo carries:

- The six computational scaffolding scripts inherited from Paper~I
  (`src/utilities/automorphism_*.py`, `tick_rule_*.py`).
- A seeded `paper/sections/audit_table.tex` with the conjecture's
  established sub-claims (PASS) and open sub-claims (STUB).
- An introduction.tex that names Eq.~(137) of Paper~I as the central
  claim of this paper.

**Next concrete actions:**

1. Flesh out the "Established Factors" section -- write up what the
   four PASS audit rows mean structurally (currently their evidence
   columns reference the scripts but no prose explains the structural
   significance).
2. Open question (iii) of Paper~I §15 (SM-chirality coupling): does
   bipartite RGB/CMY parity align with the SM's left-vs-right
   chirality projector? This is the load-bearing structural question
   that decides whether Paper~II derives the SM gauge group or
   characterises the obstruction.
3. Open question (iv): explicit $1/g^2$ prefactor for the $SU(2)_W$
   and $SU(3)$ Wilson actions on the bipartite octahedral lattice
   (the existing `paper/sections/induced_gauge_action.tex` in Paper~I
   has the U(1) calculation pending; that template generalises).

---

## What This Project Is

The central thesis of Paper~II is to prove (or characterise the
obstruction to) Eq.~(137) of Paper~I:

$$
\mathrm{Aut}(\mathcal{T}_\diamond^3, \mathcal{A}=1)
\;=\; SO(3,1) \times SU(3) \times SU(2) \times U(1).
$$

Both sides are precise finite-dimensional Lie algebras with real
dimension $18 = 6 + 8 + 3 + 1$. Either the lattice's automorphism
algebra reproduces this structure factor by factor (and the Standard
Model gauge group is derived from a single conservation axiom on a
discrete substrate), or it doesn't (and Paper~II is a precise
statement of the obstruction). Both outcomes are publishable.

The conjecture decomposes into established and open parts:

**Established on the existing per-site $\mathbb{C}^2 = (\psi_R,
\psi_L)$ amplitude (dim 7, sympy-verified):**

- $SO(3,1)$ (dim 6): emergent Lorentz from $O_h$-averaged Dirac.
- $U(1)$ (dim 1): per-site phase rotation; the $\mathcal{A}=1$
  conservation law is the corresponding Noether charge.
- The proposed per-site $SU(2)$ generators on the existing
  $\mathbb{C}^2$ are *the same matrices* as the Lorentz rotation
  subgroup -- they do not contribute a separate factor.

**Open: requires a per-site internal extension to
$\mathbb{C}^{12} = \mathbb{C}^2 \otimes \mathbb{C}^2 \otimes \mathbb{C}^3$:**

- $SU(2)_W$ (dim 3): rotation of a per-site weak-isospin
  $\mathbb{C}^2$ index, distinct from the chiral $(\psi_R, \psi_L)$
  pair.
- $SU(3)$ (dim 8): rotation of a per-site colour $\mathbb{C}^3$
  index recording the amplitude that the wavefunction's most recent
  RGB tick was along $\mathbf{V}_1$, $\mathbf{V}_2$, $\mathbf{V}_3$
  respectively.

On the extended $\mathbb{C}^{12}$, the four factors commute pairwise
(direct product, dim 18 verified by
`automorphism_direct_product_extended.py`). The remaining substantive
question is whether $SU(2)_W$ couples asymmetrically to $\psi_R$ vs
$\psi_L$ as required by the SM.

---

## Paper Title and Theme

**Title:** Geometry Forces Physics: A Lie-Algebra Derivation of the
Standard Model Gauge Group from a Single Conservation Law.

**Series:** Paper~II of the A=1 Discrete Causal Lattice series.

**Anchor:** Eq.~(137) of Paper~I (\emph{Geometry First},
[doi:10.5281/zenodo.20078529](https://doi.org/10.5281/zenodo.20078529)).

**Core framing:** the claim is dimensional first and structural
second. Dim 18 either matches or it doesn't; if it matches, the
structure constants of the lattice's $\mathrm{Aut}$ algebra must
match the four-factor product factor by factor. The framework's
contribution is identifying the *minimal* per-site internal
extension ($\mathbb{C}^2 \otimes \mathbb{C}^3$ on top of the
existing chiral $\mathbb{C}^2$) the SM gauge group requires.

---

## Audit Table Status (mirrors `paper/sections/audit_table.tex`)

| Row | Status | What it claims |
|---|---|---|
| Discrete Aut order 48 = $O_h$ | PASS | `automorphism_discrete.py` enumerates 48 elements; 12 orthogonal in standard $\mathbb{R}^3$. |
| RGB symmetry $\subset \mathbb{Z}_3 \subset SU(3)$ | PASS | `automorphism_rgb_su3.py`; abelian, cannot generate non-abelian $SU(3)$. |
| $SO(3,1) \times U(1)$ on existing $\mathbb{C}^2$ (dim 7) | PASS | `automorphism_direct_product.py`; per-site $SU(2)$ overlaps with Lorentz rotations on this carrier. |
| Direct-product on extended $\mathbb{C}^{12}$ (dim 18) | PASS | `automorphism_direct_product_extended.py`; four factors commute pairwise. |
| Tick-rule consistency on $\mathbb{C}^{12}$ | PASS | `tick_rule_extended_consistency.py`; trivial tensor extension preserves $\mathcal{A}=1$, parity, and global $SU(2)_W \times SU(3)$. |
| Wilson plaquette gauge invariance | PASS | `tick_rule_gauge_invariance.py`; bipartite plaquette $V_1, -V_2, -V_1, V_2$ gauge-invariant. |
| Exact equality vs containment in $\mathrm{Aut}_\text{ext}$ | STUB | Tractable by Lie-algebra enumeration on extended generators. |
| SM-chirality coupling alignment | STUB | Whether bipartite RGB/CMY parity is the SM's chirality projector; whether $SU(2)_W$ couples asymmetrically to $(\psi_R, \psi_L)$. |
| Explicit $1/g^2$ for $SU(2)_W$, $SU(3)$ Wilson actions | STUB | Generalise the $U(1)$ calculation in Paper~I induced_gauge_action.tex. |
| **Eq.~(137) full conjecture** | STUB | Central claim. Resolves favourably iff the three open subproblems above resolve. |

The claim auditor agent (`.claude/agents/claim-auditor.md`) treats
`audit_table.tex` as the authority; this section is for quick
orientation only.

---

## Conventions

- **Status legend.** `PASS` / `PART` / `STUB` / `FAIL` (defined in
  the front-matter of `paper/main.tex`).
- **File naming.** Sections: `paper/sections/<topic>.tex`. Figures:
  `paper/figures/<name>.{tex,pdf,png}` with `.tex` fragment + binary
  pair. Notes: `notes/<topic>.md`. Experiments:
  `src/experiments/exp_NN_<name>.{py,md}`.
- **Cross-references.** Always `\label{}` + `\ref{}` / `\autoref{}`,
  never hard-coded numbers. Section labels: `sec:<name>`. Subsection:
  `subsec:<name>`. Equation: `eq:<name>`. Figure: `fig:<name>`. Table:
  `tab:<name>`. Theorem: `thm:<name>`.
- **Bibliography.** All cites flow through
  `paper/paper-bib/references.bib`. Style: `\bibliographystyle{unsrt}`
  (numeric, in citation order). Cite Paper~I as `menendez2026geometry`
  (the v1.0 Zenodo deposit) once the bibliography seed grows.
- **LaTeX layout idioms.** `\nolinkurl{}` for paths, `\url{}` for URLs
  inside `\href{}`. `longtable` for tables that may span pages.
  `\scriptsize` for long verbatim Python.
- **Symbolic verification scripts.** The `automorphism_*.py` /
  `tick_rule_*.py` scripts in `src/utilities/` are the load-bearing
  evidence base; treat their output as the operational PASS/FAIL for
  the established audit rows. Re-execute via
  `python -m src.utilities.<name>` as needed.

## Documentation convention for code

Every non-trivial line of framework code should say what it **is** in
the theory, not just what it does in the program. Name the
mathematical object, cite the paper section/equation, and use "IS"
for exact correspondences, "approximates" for continuum limits.

---

## Release flow

See `release_notes/README.md` for the full procedure. Same flow as
Paper~I: deposit on Zenodo first, commit version bump after the DOI
is in hand, build the final PDF and snapshot it to
`.stage/<DOC_TITLE>_vX.Y.pdf` (durable per-version archive,
gitignored), tag, push, GitHub Release. The Paper~I -> Paper~II
series identifier on the title page should be kept in sync.

---

## What NOT to Change

- The six `src/utilities/automorphism_*.py` and `tick_rule_*.py`
  scripts: copies of the v1.0-released versions in Paper~I. Edit
  *only* if extending the calculation; do not refactor without
  justification, since their printed output is cited in the
  audit-table evidence column.
- `paper/sections/audit_table.tex`: once Paper~II's v1.0 is deposited
  on Zenodo, the audit table is part of the released artifact and
  tooling that consumes it must work read-only against it.

---

## Cross-references to Paper~I

Paper~II treats Paper~I as the upstream of record (the v1.0 release
deposited at
[doi:10.5281/zenodo.20078529](https://doi.org/10.5281/zenodo.20078529)).
Working notes, the §15 conjecture statement, the induced-gauge-action
appendix, and the v1.0 versions of the `automorphism_*.py` /
`tick_rule_*.py` scripts all live in the dcl repo.

For local Claude/agent work, the dcl checkout is exposed inside
Paper~II as a Windows directory junction:

```text
external/dcl  ->  C:\dev\dcl
```

Anywhere a seeded file points at `external/dcl/...`, that path
resolves to the dcl repo on this machine. The `external/` directory
is gitignored, so the junction is *not* part of the committed repo.

To (re)create the junction on a fresh clone (Windows):

```bat
mkdir external
mklink /J external\dcl C:\dev\dcl
```

If the dcl repo is checked out at a different path, adjust
accordingly; the seeded paths assume `external/dcl` resolves to
*some* checkout of the dcl repo. For a reviewer who does not have
dcl checked out, the
[Zenodo DOI](https://doi.org/10.5281/zenodo.20078529) is the
authoritative reference -- the seeded prose names Paper~I sections
(§15, Appendix~B, Eq.~(137)) explicitly so the reader can navigate
the published artifact without the local dcl checkout.

**Notable Paper~I notes** (read these before starting a new line of
work that overlaps the framework's broader programme):

- `external/dcl/notes/follow_on_implications.md` -- catalogue of
  follow-on paper seeds. **Paper~II is item #16** ("Standard Model
  Gauge Derivation: Extended-Amplitude Direct-Product Construction"),
  so the catalogue's framing of this paper -- the three open
  subproblems, the per-site $\mathbb{C}^{12}$ extension, the
  dependency graph to other follow-ons -- is the authoritative
  upstream scoping document. Other items relevant to Paper~II's
  vicinity: #3 (SM masses / Farey / Veneziano), #13 (Operation
  Algebra of the Discrete Causal Lattice), #14 (Balanced Equations
  and Birefringent Channels), and items that depend on Paper~II's
  colour machinery (proton internals among them).

---

## Cross-references to physics-research (notation / formalization)

A parallel formalization effort -- standardised notation, the
algebra/topology of the framework, and the balanced $\mathcal{A}=1$
equation system -- lives in the physics-research repo, exposed as a
Windows directory junction:

```text
external/research  ->  C:\dev\physics-research
```

Highlights:

- `external/research/Notes/balanced_equations/` -- the symbol-meaning
  catalogues (`symbol-meaning-{3,4,5,6}.csv`) and
  `Diagrammatic_Map.md` for the balanced $\mathcal{A}=1$ equation
  system. Upstream parent for any reaction-style equation produced
  in Paper~II that conserves $\mathcal{A}=1$ across both sides.
- `external/research/Notes/color_and_emergent_forces.md`,
  `lattice_as_inference_engine.md`, and the rest of the topical
  notes alongside -- the formalization effort's working surface for
  notation, algebra, and topology of the framework.

**Upstream flow rule.** Findings during Paper~II work that touch
notation, algebra, topology, or balanced $\mathcal{A}=1$ equations
should be captured as notes in this repo's `notes/` directory (per
`notes/README.md`) so they can flow upstream to physics-research's
Notes/. A short stub is better than no stub; expand later if the
finding grows.

To (re)create the junction on a fresh clone (Windows):

```bat
mkdir external
mklink /J external\research C:\dev\physics-research
```

---

## Notes Index

- `notes/README.md` -- conventions for notes/
- `notes/lie_algebra_proof_sketch.md` -- starter note pointing at
  Paper~I's working proof sketch
  (`external/dcl/notes/lie_algebra_automorphism_proof_sketch.md`).
- `notes/work_plan.md` -- phased plan for closing the four open
  audit rows; identifies decision points where outcomes route the
  paper toward different framings (derivation / obstruction /
  characterisation).
- `notes/su3_branch_consistency.md` -- Phase~1 sub-task 0: only the
  $\mathbf{3} \oplus \mathbf{3}$ SU(3) interpretation admits the
  existing tick rule as a global symmetry (PASS).
- `notes/chirality_alignment.md` -- Phase~1 Route (a): the unique
  linear bipartite parity is $\sigma_x \otimes I_2 \otimes I_3$;
  bipartite $\mathbb{Z}_2$ and SM chirality $\mathbb{Z}_2$ are
  orthogonal Bloch involutions on the chirality $\mathbb{C}^2$
  (CHARACTERISATION).
- `notes/cp_modification_obstruction.md` -- Phase~1.5 Route (b): no
  natural antilinear modification of the tick rule admits Branch~B
  SU(3) or SM-style $CP$ (FAIL); reduces to anticommutation
  $\{\lambda_a, C\} = 0$ for every Gell-Mann, which has only the
  trivial solution.
- `notes/mass_chirality_coupling.md` -- structural-insight synthesis:
  mass-as-clock-density (Paper~I), vector-like $SU(2)_W$ (Phase~1a),
  and the absence of $CP$ (Phase~1.5) are three projections of one
  kinematic feature -- the bipartite tick is chirality-mixing as the
  kinetic mechanism, and every gauge structure consistent with the
  lattice preserves the clock density.
- `notes/debt_to_measurement.md` -- the substrate-first programme's
  methodological precondition: derivation is feasible only because
  measurement-based physics established accurate targets to derive.
  The surface argument (humble, symbiotic relationship between
  substrate-first and measurement-based work) is stable; the deeper
  question about the human perspective on the universe (what makes
  both routes converge?) is intentionally left open for foundations
  follow-up.
- `notes/no_spacetime_torsion.md` -- Paper~I's gravity-as-clock-density
  account replaces curved spacetime with a scalar density field on
  the flat bipartite lattice; spacetime torsion (and the entire
  Riemann-Cartan apparatus: Christoffel symbols, spin connection,
  vierbein) is therefore not needed.  The note records why,
  including the observation that Einstein-Cartan's motivation
  (coupling Dirac fermions to curved gravity through a torsionful
  spin connection) is moot because the framework provides the Dirac
  structure intrinsically through the bipartite tick rule.
- `notes/su3_generation_from_colour_memory.md` -- Phase 2: the
  natural ``rotate-toward-$|j\rangle$'' colour-memory tick rule
  (real-symmetric off-diagonal generators) closes under Lie brackets
  to the full $\mathfrak{su}(3)$ (PASS).  Diagonal-only readings
  close to the Cartan only (the continuous closure of the discrete
  RGB $\mathbb{Z}_3$); single-off-diagonal readings close to one
  $\mathfrak{su}(2)$ subalgebra.  The full $\mathfrak{su}(3)$ of
  Eq.~(137) is dynamically generated by the lattice, not merely a
  global symmetry of a trivial colour extension.
- `notes/aut_centralizer_enumeration.md` -- Phase 3: the discrete-
  Hermitian centralizer of the bipartite tick rule on $\mathbb{C}^{12}$
  is structurally $\mathfrak{su}(6)_+ \oplus \mathfrak{su}(6)_- \oplus
  \mathfrak{u}(1)$ (dim 71), with the two $\mathfrak{su}(6)$ factors
  on the $\pm 1$ chirality eigenspaces and $J_1$ as the central
  $\mathfrak{u}(1)$.  Under $SU(3) \times SU(2)$ branching, the
  59 extras decompose as $(\mathbf{8}, \mathbf{3})$ (leptoquark-
  flavoured) plus chirality-$\sigma_x$ shadow SM.  Conjecture
  $\supseteq$ confirmed (PART); equality $=$ requires factor-product
  gauge invariance.
- `notes/aut_centralizer_extras_commutators.md` -- Phase 3 extension:
  bracket structure of the 59 extras vs the 12 SM generators in the
  centralizer.  708 + 1711 brackets classified.
  $[\text{extras}, \text{SM}]$: 0/708 land in SM (extras is
  SM-invariant module).  $[\text{extras}, \text{extras}]$: 226/1711
  land in SM or mixed (extras is NOT a Lie ideal).  Algebraic shape
  of a broken-symmetry pattern $G' = SU(6) \times SU(6) \times U(1)
  \to G = \mathrm{SM}$, with 59 ``broken'' generators as coset
  module.
- `notes/induced_gauge_action_nonabelian.md` -- Phase 4: non-abelian
  generalisation of Paper~I's bipartite-plaquette induced action.
  Q-tensor (eigenvalues $\{4, 4, 16\}$) inherited from Paper~I
  unchanged; $T_F = 1/2$ trace normalisation in SU(N) fundamental.
  Per-site spectator-factor counting yields the sharp lattice-scale
  prediction $g_3^2 / g_2^2 = 3/2$ (equivalently $g_1^2 : g_2^2 :
  g_3^2 = 1 : 4 : 6$), independent of the universal one-loop
  prefactor (still open).  PART: structural form complete;
  numerical $c$ open; ratio prediction sharply derived.

(List additional notes here as they accumulate.)

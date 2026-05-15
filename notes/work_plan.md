# Paper II work plan: phased approach

**Status:** DRAFT
**Purpose:** Lay out the phased plan for closing the four open audit
rows -- in particular the central Eq.~(137) STUB -- and identify the
decision points where outcomes route the paper toward different
framings (derivation / obstruction / characterisation).
**Cited by:** none yet; will be referenced by future section drafts
as phases complete.

---

## Setup

The audit table (`paper/sections/audit_table.tex`) currently holds 6
PASS rows (the established factors) and 4 STUB rows:

1. Exact equality vs containment in $\mathrm{Aut}_\text{ext}$.
2. SM-chirality coupling alignment.
3. Explicit $1/g^2$ for the $SU(2)_W$ and $SU(3)$ Wilson actions.
4. Eq.~(137) full conjecture (resolves iff (1)-(3) resolve).

The phases below are ordered by *information value* -- earliest
phases are the ones whose answer most reshapes everything downstream,
so failure or surprise there is cheapest to absorb.

This is a working plan; phases are expected to be revised as
outcomes land. When a phase completes, mark it with the resolution
(PASS / PART / FAIL) and a pointer to the section / script that
captures the result. When the plan is superseded, leave it in place
per `notes/README.md` and add a pointer to the replacement.

---

## Argument: why this ordering

The five phases are sequenced by how much each phase's answer
reshapes the work that follows:

- Phase 1 (chirality alignment) is the single largest binary in the
  paper. If RGB/CMY parity does not coincide with the SM chirality
  projector, every downstream phase is still doable but the paper's
  headline shifts from "derivation" to "precise statement of
  obstruction." Doing this first means the framing decision is taken
  on real evidence, not in advance.
- Phase 2 (non-abelian $SU(3)$ from $\mathbb{C}^3$ memory) is the
  next-most-load-bearing structural question. It conditions Phase 3's
  enumeration scope.
- Phase 3 (containment vs equality) is mechanically tractable but
  computationally the most expensive; its scope depends on what
  Phases 1-2 returned.
- Phase 4 (Wilson $1/g^2$ prefactors) is calibration -- mechanical
  once the structure above is settled, falsifiable against measured
  couplings.
- Phase 0 (prose backbone) is parallel-able and runs alongside Phase 1
  because it is writing, not research, and gets the structural
  scaffolding in place so later results land into prose that already
  exists.

---

## Phase 0 -- Establish the prose backbone (parallel to Phase 1) -- **PASS (2026-05-15)**

**Goal.** Write the "Established Factors" section so the 6 PASS audit
rows have structural prose, not just script references.

**Output.** A `paper/sections/established_factors.tex` (or expanded
`introduction.tex`) covering:

- Why $|\mathrm{Aut}_\text{discrete}(\Gamma, V)| = 48 = O_h$ is the
  right discrete spatial symmetry, and why the orthogonal subgroup
  of order 12 is the physically interpreted part.
- Why the RGB sublattice gives only $\mathbb{Z}_3 \subset SU(3)$ --
  and why this *forces* the per-site $\mathbb{C}^3$ extension rather
  than refuting it.
- Why $SO(3,1) \times U(1)$ on the existing $\mathbb{C}^2$ is dim 7,
  and why the proposed per-site $SU(2)$ on this carrier *overlaps*
  with Lorentz rotations rather than contributing a new factor (this
  is subtle and Paper~I does not fully spell it out).
- Why the four-factor commutativity on extended $\mathbb{C}^{12}$
  (dim 18 verified) is necessary but not sufficient for equality.

**Exit criteria.** A reader can follow this section without needing
Paper~I §15 open. Each PASS row has a paragraph of structural
meaning, not a script trace.

**Risk.** Low. This is writing, not research.

**Resolution (2026-05-15).** Closed as a new section
`paper/sections/established_factors.tex`, wired into `paper/main.tex`
between Introduction and Conclusion (replacing the
`section_template.tex` placeholder). The section has six
PASS-row subsections (one per audit row: discrete spatial $O_h$, RGB
$\mathbb{Z}_3$ obstruction, $SO(3,1) \times U(1)$ on existing
$\mathbb{C}^2$, direct product on extended $\mathbb{C}^{12}$,
tick-rule consistency, Wilson plaquette gauge invariance) plus a
closing subsection that combines them into the established
containment $\mathrm{Aut} \supseteq SO(3,1) \times SU(3) \times
SU(2) \times U(1)$ and names the gap to equality. Reviewed by the
claim-auditor agent against `paper/sections/audit_table.tex`; three
mismatches found (1 high, 1 medium, 1 low) and corrected before
commit. Build verified: `make paper` produces a 13-page PDF with all
cross-references resolved (the bibtex step in the makefile fails on
the empty seed bibliography under TeXLive 2026's `openout_any = p`,
but the PDF itself builds cleanly via direct pdflatex; orthogonal to
Phase 0).

---

## Phase 1 -- Chirality alignment (load-bearing decision) -- **CHARACTERISATION (2026-05-15)**

**Goal.** Resolve audit-table STUB row "SM-chirality coupling
alignment." Question: does the bipartite RGB/CMY parity coincide with
the left/right chirality projector $P_L = (1 - \gamma_5) / 2$ on the
existing $(\psi_R, \psi_L)$ amplitude?

### Phase 1 sub-task 0 -- SU(3) representation branch -- **PASS (2026-05-15)**

Upstream of the alignment test itself: the bipartite tick rule
forces the colour interpretation to be Branch~A (3 $\oplus$ 3) rather
than Branch~B (3 $\oplus$ $\bar{3}$). Established by
`src/utilities/su3_branch_consistency.py` (PASS); captured as
`notes/su3_branch_consistency.md` for upstream flow; audit-table
row added. The structural consequence is that any bipartite parity
operator $P$ acting as a symmetry of the existing tick rule must be
*linear* (not antilinear / $CP$-like). Linear candidates are
$P = \sigma_x \otimes I_2 \otimes M$ with $M$ a symmetric element of
SU(3).

This sub-task splits Phase 1 into two routes (see `route_a` and
`route_b` below), only one of which is required for paper
publication; both are possible.

### Route (a) -- Linear bipartite parity on the existing tick rule -- **PART (2026-05-15)**

**Output.**

- A new symbolic verification script
  `src/utilities/chirality_parity_alignment.py` that enumerates the
  linear bipartite parity candidates $P = \sigma_x \otimes I_2 \otimes M$
  ($M$ ranges over $I_3$ and the symmetric Gell-Manns
  $\{I_3, \lambda_1, \lambda_3, \lambda_4, \lambda_6, \lambda_8\}$),
  constructs $\gamma_5 = \sigma_z \otimes I_2 \otimes I_3$ and the
  SU(2)\_W generators, and runs the four tests below.
- A `notes/chirality_alignment.md` working note logging the cases
  tried.
- An audit-table row update STUB $\to$ PASS / PART / FAIL.

**Predicted outcome.** Vector-like at the operator level
($\{\sigma_x, \sigma_z\} = 0$ on the chirality factor), so the
lattice's bipartite $\mathbb{Z}_2$ does *not* coincide with the SM's
chirality $\mathbb{Z}_2$. This is itself a sharp structural finding:
the lattice predicts that the SM's chirality is built on a different
$\mathbb{Z}_2$ than the lattice's bipartition. Routes the paper
toward "precise obstruction" or "characterisation" rather than
"derivation."

**Resolution (2026-05-15).** Closed as CHARACTERISATION.
`chirality_parity_alignment.py` tests 5 candidates; only $M = \pm I_3$
survive global SU(3) commutativity (by Schur on the irreducible
$\mathbf{3}$), and they are projectively equivalent. The unique
viable bipartite parity is $P = \sigma_x \otimes I_2 \otimes I_3$,
satisfying: (i) $P^2 = I$ (involution), (ii) $P \gamma_5 P^{-1} =
-\gamma_5$ (anticommutes with SM chirality), (iii) $P P_L^{SM}
P^{-1} = P_R^{SM}$ (swaps L $\leftrightarrow$ R --- spatial parity,
not chirality projection), (iv) $P\, T_a^W\, P^{-1} = T_a^W$
(vector-like SU(2)\_W coupling). Captured in
`notes/chirality_alignment.md`. Audit row "SM-chirality coupling
alignment" updated STUB $\to$ PART.

### Route (b) -- Modified tick rule with built-in discrete $CP$ (Phase 1.5) -- **FAIL (2026-05-15)**

**Goal.** Construct a modified bipartite tick rule that includes an
explicit colour conjugation on chirality-flipping steps, making
Branch~B (3 $\oplus$ $\bar{3}$) consistent. If successful, the
framework has a built-in discrete $CP$ symmetry and the
chirality-alignment test becomes meaningful in the SM-$CP$ sense
(test whether $P_L$ is extractable from $P_{CP}$ under the
$\mathcal{A}=1$ constraint).

**Resolution (2026-05-15).** Closed as a definitive NEGATIVE.
`src/utilities/tick_rule_cp_modified.py` (FAIL) tests the natural
ansatz $T_\text{ext}^B = is \cdot I_{12} + c \cdot (\sigma_x \otimes
I_2 \otimes C) \circ K$ with $K$ global complex conjugation, and
finds no non-zero $C$ admits Branch~B SU(3) as a global symmetry.
The condition reduces to anticommutation $\{\lambda_a, C\} = 0$ for
every Gell-Mann; the surviving entries after $\lambda_3$ ($C_{12},
C_{21}, C_{33}$) get killed by $\lambda_8$. Robustness checked
against isospin entanglement (decoupled from the colour constraint)
and unitarity (preserved automatically by antilinear operators).
Representation-theoretic origin: $\mathbf{3}$ and $\bar{\mathbf{3}}$
are inequivalent SU(3) irreps; the unique antilinear intertwiner
(global $K$) does not satisfy Branch~B's chirality-dependent
commutativity. Captured in `notes/cp_modification_obstruction.md`;
audit-table row "Modified tick rule for Branch~B SU(3)
compatibility" added with status FAIL.

**Structural consequence.** The framework's bipartite parity is
intrinsically LINEAR (spatial parity, no charge-conjugation
component); the lattice cannot incorporate SM-style $CP$ as a
discrete symmetry of any natural tick modification. Combined with
Route~(a)'s characterisation result, Phase~1's terminal state is:
the framework realises a parity-conserving Lie group structure
$SO(3,1) \times SU(3) \times SU(2) \times U(1)$; the SM's chirality
and $CP$ violation are external choices, not geometric consequences
of the discrete causal lattice.

**Sequencing.** Route~(a) lands first (smaller load, no audit-row
reopen). Route~(b) is taken up only after Route~(a)'s result is
recorded; the paper may present both, depending on Phase~1
outcomes.

### Phase 1 overall exit criteria

One of three terminal states for the alignment test (under either
route), each with a different downstream consequence:

| Outcome | Downstream |
|---|---|
| Aligned | Routes to "derivation" framing. $SU(2)_W$ couples chirally. Continue Phase 2 with confidence. |
| Anti-aligned / vector-like | Routes to "precise obstruction" framing. The lattice predicts a vector-like $SU(2)$, not the SM's chiral one. Phases 2-4 still run, but the paper's headline changes. |
| Partial / basis-dependent | Routes to "characterisation" framing. Identify the basis change (or lack thereof) and quote it as the framework's nontrivial prediction. |

**Risk.** This is the single most likely place for a *useful*
surprise. It is also where the framework's predictive content is
sharpest. Sub-task 0's PASS already constrains the candidate space
(linear under Route~(a), antilinear under Route~(b)); the outcome
class is no longer "anything goes."

---

## Phase 2 -- Non-abelian $SU(3)$ generation from $\mathbb{C}^3$ memory -- **PASS (2026-05-15)**

**Goal.** Resolve the question implicit in audit row "RGB symmetry
$\subset \mathbb{Z}_3 \subset SU(3)$" -- *given* the per-site
$\mathbb{C}^3$ colour-memory amplitude (where component $j$ records
"most recent RGB tick was $\mathbf{V}_j$"), does the tick rule on
this amplitude generate all eight Gell-Mann generators, or only a
subalgebra?

**Output.**

- Extension of `src/utilities/automorphism_rgb_su3.py` (or new
  `automorphism_su3_extended.py`) that enumerates the Lie algebra
  generated by the tick-rule action on $\mathbb{C}^3$.
- New audit row "Non-abelian $SU(3)$ from $\mathbb{C}^3$ memory" with
  PASS / PART / STUB resolution.

**Exit criteria.** Either the algebra closes to $\mathfrak{su}(3)$
(8 generators), to the Cartan subalgebra (2 generators, abelian --
same as RGB sublattice), or to a proper subalgebra of intermediate
rank. Each routes differently.

**Risk.** Medium. This is the place where "the conjecture might be
wrong because the lattice cannot produce non-abelian colour" lives.
Tractable to settle in either direction.

**Resolution (2026-05-15).** Closed as PASS.
`src/utilities/su3_generation_from_colour_memory.py` surveys 8
candidate $X_1 = -i \log U_1$ for the colour-memory tick rule.  Each
candidate's $S_3$ orbit $\{X_1, X_2, X_3\}$ is closed under Lie
brackets and the resulting subalgebra identified.  Three structural
cases:

- *Diagonal-only* (e.g.\ $X_1 = \lambda_8$): closure dim 2 = Cartan
  subalgebra of $\mathfrak{su}(3)$, the continuous closure of the
  discrete RGB $\mathbb{Z}_3$ of `automorphism_rgb_su3.py`.
- *Single off-diagonal* (real or imaginary, e.g.\ $X_1 = \lambda_1$
  or $\lambda_2$): closure dim 3 = one $\mathfrak{su}(2)$
  subalgebra of $\mathfrak{su}(3)$.
- *Real-symmetric two-plane (`rotate-toward-$|j\rangle$' coherent
  mixing, $X_1 = \lambda_1 + \lambda_4$)*, or *any* mixed candidate
  containing real-symmetric off-diagonal content (e.g.\
  $\lambda_8 + \lambda_1$): closure dim 8 = full $\mathfrak{su}(3)$.

The natural physical reading of "colour memory" --- a coherent
rotation of amplitude from the other components toward
$|j\rangle$ via real-symmetric generators --- produces the full
$\mathfrak{su}(3)$ as a dynamically-generated algebra of the
lattice, not merely as a global symmetry of a trivial colour
extension.  The framework's robustness result: any natural
real-symmetric off-diagonal candidate closes to full
$\mathfrak{su}(3)$; only highly restricted (purely diagonal or
purely imaginary antisymmetric) readings yield strict subalgebras.

Captured in `notes/su3_generation_from_colour_memory.md`;
audit-table row "Non-abelian $SU(3)$ from $\mathbb{C}^3$ memory"
added with status PASS.

---

## Phase 3 -- Containment vs equality on $\mathrm{Aut}_\text{ext}$ -- **PART (2026-05-15)**

**Goal.** Resolve audit STUB row "Exact equality vs containment in
$\mathrm{Aut}_\text{ext}$." Enumerate the full Lie algebra of
automorphisms of $(\mathcal{T}_\diamond^3, \mathcal{A} = 1)$ on
extended $\mathbb{C}^{12}$ and compare to $\mathfrak{so}(3,1) \oplus
\mathfrak{su}(3) \oplus \mathfrak{su}(2) \oplus \mathfrak{u}(1)$.

**Output.**

- A symbolic enumeration script. This is the **most expensive
  computation** in the project -- dim-18 generator algebra on a
  $\mathbb{C}^{12}$ carrier. May need numerical sampling fallbacks
  and / or basis-adapted shortcuts (representation-theoretic
  decomposition first, then verification).
- Audit row update: equality (the conjecture as written), proper
  containment (an obstruction, *which* one), or extended algebra (a
  prediction of extra generators).

**Exit criteria.** A definitive answer about whether the central
Eq.~(137) holds as equality or containment, conditioned on Phase 1
and Phase 2 outcomes.

**Risk.** Highest practical-engineering risk (compute scale). Lowest
framing risk (any answer is informative).

**Resolution (2026-05-15).** Closed as PART.
`src/utilities/automorphism_centralizer_extended.py` enumerates the
143 tensor-product generators of $\mathfrak{su}(12)$ and verifies
that **71** of them commute with the bipartite tick rule (equivalently,
$\dim(\mathfrak{u}(6) \oplus \mathfrak{u}(6)) - 1 = 71$ from a direct
eigenspace calculation).  Of the 14 Hermitian generators of Eq.~(137),
12 lie in this centralizer ($J_1$, 3 $SU(2)_W$, 8 $SU(3)_c$); the
remaining 2 ($J_2, J_3$ from $\mathfrak{so}(3,1)$'s rotation
subgroup) are continuum-emergent (do not commute with the discrete
$\sigma_x \otimes I_2 \otimes I_3$).

The 71 - 12 = 59 "extra" generators in the centralizer split as:

- 24 isospin-colour mixings ($I_2 \otimes \sigma_a \otimes \lambda_b$);
- 3 chirality-$\sigma_x$ + isospin ($\sigma_x \otimes \sigma_a \otimes I_3$);
- 8 chirality-$\sigma_x$ + colour ($\sigma_x \otimes I_2 \otimes \lambda_a$);
- 24 chirality-$\sigma_x$ + isospin-colour ($\sigma_x \otimes \sigma_a \otimes \lambda_b$).

All 59 are *factor-mixing* operators -- they couple tensor factors
that Eq.~(137)'s direct-product structure treats as independent.
None are SM-gauge-invariant: each one couples factors that the
SM's gauge structure forbids by construction.

Structural reading: the lattice's discrete tick rule admits a
71-dim algebra of per-site automorphisms; the SM's 18-dim
gauge + Lorentz structure is the factor-product-irreducible
sub-algebra.  **Eq.~(137) holds as equality $=$ if and only if
the factor-product gauge invariance of the SM is imposed as an
additional constraint** beyond tick-rule commutativity.  The
lattice does not single this out by itself.

Captured in `notes/aut_centralizer_enumeration.md`; audit-table row
updated STUB $\to$ PART.

**Open follow-up.** Identifying which natural continuum-emergent
constraints (basis-permutation $S_3$ on the colour $\mathbb{C}^3$,
Lorentz emergence from $O_h$-averaging, others) reduce the 71-dim
centralizer to the conjecture's 18 is the open follow-up.  This
could become a Phase 3.5 if pursued.

### Phase 3 extension (2026-05-15) -- SU(6)$\oplus$SU(6)$\oplus$U(1) identification and bracket structure

Sharpened the Phase 3 result by identifying the 71-dim centralizer
explicitly as $\mathfrak{su}(6)_+ \oplus \mathfrak{su}(6)_- \oplus
\mathfrak{u}(1)$, with the two $\mathfrak{su}(6)$ factors acting on
the $\pm 1$ chirality eigenspaces and the $\mathfrak{u}(1)$ central
(= $J_1$).  Under the $\mathbf{6} = (\mathbf{3}, \mathbf{2})$ branching,
$\mathfrak{su}(6)$ decomposes under $SU(3) \times SU(2)$ as
$\mathbf{35} = (\mathbf{8}, \mathbf{1}) \oplus (\mathbf{1}, \mathbf{3})
\oplus (\mathbf{8}, \mathbf{3})$; the 11-dim SM gauge subset and
the 24 "leptoquark-flavoured" extras correspond to these irreps.

`src/utilities/aut_centralizer_extras_commutators.py` computes the
708 brackets $[E, T]$ (extras × SM) and 1711 brackets
$[E_i, E_j]$ (extras × extras) and classifies each as zero / in SM /
in extras / mixed.  Results:

- $[\text{extras}, \text{SM}]$ counts: 256 zero, 0 in SM, 452 in
  extras, 0 mixed.  The 59-dim extras subspace is INVARIANT under
  the SM adjoint action -- SM never bracket-produces SM from extras.
- $[\text{extras}, \text{extras}]$ counts: 339 zero, 178 in SM, 1146
  in extras, 48 mixed.  Extras is NOT a Lie ideal; brackets within
  extras hit both the SM subalgebra and back to extras, exactly
  matching the $SU(3) \times SU(2)$ branching of the
  $\mathfrak{su}(6)$ adjoint.

Structural reading: the 71-dim centralizer is a simple semisimple
Lie algebra ($\mathfrak{su}(6) \oplus \mathfrak{su}(6) \oplus
\mathfrak{u}(1)$) with the SM 12-dim subalgebra embedded as a
non-normal subalgebra and the 59-dim extras as an SM-module
complement that hits both SM and extras under self-bracketing.
This is the algebraic shape of a *broken-symmetry pattern* with
$G' \to G$ where $G' = SU(6) \times SU(6) \times U(1)$ and $G$ = SM.

Captured in `notes/aut_centralizer_enumeration.md` (sharpened) and
`notes/aut_centralizer_extras_commutators.md` (the bracket
analysis).  Two narrative framings queued for Paper~II's
conclusion: (a) high-energy unification (extras as massive
GUT-style gauge bosons that decouple at low energy); (b)
decoherence on the discrete walk (extras as dephasing operators
that lose coherence over macroscopic distances).

---

## Phase 4 -- Wilson $1/g^2$ prefactors for $SU(2)_W$, $SU(3)$ -- **PART (2026-05-15)**

**Goal.** Resolve audit STUB row. Generalise Paper~I's
`induced_gauge_action.tex` (where the $U(1)$ calculation was the
worked example) to extract the explicit $1/g^2$ prefactor for the
$SU(2)_W$ and $SU(3)$ Wilson actions on the bipartite octahedral
lattice.

**Output.**

- New section `paper/sections/induced_gauge_action.tex` (or
  extension of Paper~I's appendix) with the calculation.
- A symbolic verification script if applicable.
- Audit row update.

**Exit criteria.** Closed-form $1/g^2(a)$ at lattice spacing $a$ for
both factors. Optional: a one-loop RG flow check against measured
couplings at, say, 100 GeV -- useful as a sanity check, not a proof.

**Risk.** Mechanical once Phases 1-3 settle. The calculation is
well-defined; the question is whether the numbers are sensible.
Mismatch with measured couplings is itself a publishable
falsification or constraint.

**Resolution (2026-05-15).** Closed as PART.
`src/utilities/induced_gauge_action_nonabelian.py` extends Paper~I's
bipartite-plaquette induced-action calculation to non-abelian gauge
groups.  Key results:

- The bipartite Q-tensor (eigenvalues $\{4, 4, 16\}$, trace 24)
  is inherited from Paper~I unchanged.  Verified in sympy by
  reproducing the Q-matrix from $\sum_{a<b}(V_a^i V_b^j F_{ij})^2$.
- For SU(N) link variables, the trace identity
  $\operatorname{Tr}(T^a T^b) = T_F \delta^{ab}$ (with
  $T_F = 1/2$ in the fundamental) pulls a global factor $T_F / N$
  outside; the Q-tensor structure is unchanged.
- The framework's per-site amplitude
  $\mathbb{C}^2_{\text{chir}} \otimes \mathbb{C}^2_{\text{iso}}
   \otimes \mathbb{C}^3_{\text{col}}$ has spectator-factor
  multiplicities $N_f^{SU(2)} = 2 \cdot 3 = 6$ and $N_f^{SU(3)}
  = 2 \cdot 2 = 4$.

The framework's first quantitative gauge-coupling prediction is

$$g_3^2 / g_2^2 = 3/2 \quad \text{at the lattice scale } 1/a,$$

independent of the universal one-loop prefactor $c$ (still open).
Equivalent ratios: $g_1^2 : g_2^2 : g_3^2 = 1 : 4 : 6$ at the
lattice scale.

SM measured ratios at $M_Z$: $g_3^2/g_2^2 \approx 3.3$,
$g_2^2/g_1^2 \approx 3.2$.  The discrepancy with the framework's
lattice-scale prediction is consistent with the kind of RG flow
expected over many energy decades, but the framework does not yet
fix the lattice scale $1/a$ from first principles to make this a
tight quantitative test.

Captured in `notes/induced_gauge_action_nonabelian.md`; audit-table
row updated STUB $\to$ PART.  Closing it to PASS requires the
explicit one-loop $-\operatorname{Tr}\ln D_{\text{lat}}[U]$
calculation that Paper~I and Paper~II both leave for follow-up.

---

## Phase 5 -- Synthesis and write-up

**Goal.** Settle the central Eq.~(137) audit row to PASS / PART /
FAIL, and write the conclusion section accordingly.

**Output.** Final `paper/sections/conclusion.tex`, abstract revision,
audit table v1.0-frozen, release-notes draft.

**Exit criteria.** Audit table v1.0-frozen for the Zenodo deposit per
the release flow in `release_notes/README.md`.

---

## Decision points

1. **End of Phase 1.** Chirality outcome reshapes the paper's
   headline. Stop and discuss before committing prose direction.
2. **End of Phase 2.** Non-abelian $SU(3)$ outcome reshapes Phase 3's
   enumeration scope.
3. **Mid-Phase 3.** If the full enumeration is computationally
   intractable, decide whether to switch to a representation-theoretic
   / basis-adapted approach or settle for a partial result with a
   clear statement of what is verified and what is conjectured.

---

## What is deliberately out of scope

- **No new figures** until Phase 4 results are concrete. The current
  figure scaffolding is template-only; figures should illustrate
  real results, not placeholders.
- **No bibliography expansion** beyond cite-as-needed -- the current
  `paper/paper-bib/references.bib` is empty seed and should grow with
  each section, not in a batched pass.
- **No refactor of the six load-bearing scripts.** CLAUDE.md is
  explicit: their printed output is cited, edits only when extending
  the calculation.

---

## Open questions

1. Does Phase 0 prose belong in `introduction.tex` (expansion) or in
   a new `established_factors.tex` (separate section)? Defer to the
   shape of the prose once written.
2. For Phase 1, what is the precise definition of "bipartite RGB/CMY
   parity" on the extended $\mathbb{C}^{12}$? The notion is intuitive
   on the lattice but needs a concrete operator before the alignment
   test makes sense. First sub-task of Phase 1.
3. For Phase 3, is there a representation-theoretic shortcut (e.g.,
   decomposing $\mathbb{C}^{12}$ under the proposed factors and
   counting irreducible components) that bounds the answer before the
   full enumeration is run?

## Pointers

- Audit table: `paper/sections/audit_table.tex` (canonical PASS /
  STUB record for each sub-claim).
- Working sketch: `notes/lie_algebra_proof_sketch.md` (parent note;
  open questions there mirror Phases 1-3 here).
- Paper~I anchor: `external/dcl/paper/sections/conclusion.tex`
  (Eq.~(137) statement) and
  `external/dcl/paper/sections/induced_gauge_action.tex` ($U(1)$
  Wilson template that Phase 4 generalises).
- Release flow: `release_notes/README.md`.

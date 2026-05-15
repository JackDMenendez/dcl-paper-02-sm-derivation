# SU(3) representation branch consistency

**Status:** STABLE (verified by `src/utilities/su3_branch_consistency.py`,
2026-05-15).
**Purpose:** Captures the structural finding that the bipartite tick
rule of Paper~I, extended trivially to $\mathbb{C}^{12}$, forces a
specific choice between two natural SU(3) interpretations of the
per-site colour amplitude.
**Cited by:** the audit-table row "SU(3) representation branch
consistency" in `paper/sections/audit_table.tex`. Phase 1 of
`notes/work_plan.md` routes off this finding.

---

## The two branches

The proposed colour-memory amplitude $(c_1, c_2, c_3) \in \mathbb{C}^3$
at each lattice site can carry SU(3) in two distinct ways:

- **Branch A (3 ⊕ 3).** SU(3) acts as $\lambda_a/2$ on every site,
  RGB and CMY alike. Both sublattices carry the fundamental
  representation $\mathbf{3}$. This is the action used in
  `src/utilities/automorphism_direct_product_extended.py` and
  `src/utilities/tick_rule_extended_consistency.py`. The bipartite
  RGB/CMY distinction is implemented at the level of basis labels,
  not SU(3) representations.

- **Branch B (3 ⊕ 3̄).** SU(3) acts as $\lambda_a/2$ on RGB sites and
  as $-\overline{\lambda_a}/2$ on CMY sites:
  $$T_a^B \;=\; P_R \otimes I_2 \otimes \tfrac{\lambda_a}{2} \;+\; P_L \otimes I_2 \otimes \left(-\tfrac{\overline{\lambda_a}}{2}\right),$$
  where $P_R, P_L = \mathrm{diag}(1,0), \mathrm{diag}(0,1)$ project
  the chirality factor onto the two sublattices. RGB carries
  $\mathbf{3}$, CMY carries $\bar{\mathbf{3}}$. This is QCD's
  identification of colour vs anti-colour.

Both branches close to $\mathfrak{su}(3)$ as Lie algebras (Branch~B
because the conjugate-representation generators $-\overline{\lambda_a}/2$
inherit the *same* real structure constants $f_{abc}$). The
discriminating test is consistency with the bipartite tick rule, not
internal closure.

## What was observed

Under the existing tick rule $T_\text{ext} = T_\text{chir} \otimes I_2
\otimes I_3$, the commutator factors as

$$[T_\text{ext},\, T_a^B] \;=\; [T_\text{chir}, P_R] \otimes I_2 \otimes \tfrac{1}{2}(\lambda_a + \overline{\lambda_a}) \;=\; [T_\text{chir}, P_R] \otimes I_2 \otimes \mathrm{Re}(\lambda_a).$$

This uses $[X\otimes I\otimes I,\, Y\otimes I\otimes Z] = [X,Y]\otimes I
\otimes Z$ and $[T_\text{chir}, P_L] = -[T_\text{chir}, P_R]$ (since
$P_R + P_L = I$ commutes with $T_\text{chir}$). The residual vanishes
*iff* $\mathrm{Re}(\lambda_a) = 0$.

Among the eight Gell-Mann generators, only $\lambda_2, \lambda_5,
\lambda_7$ are purely imaginary; the other five
($\lambda_1, \lambda_3, \lambda_4, \lambda_6, \lambda_8$) have real
entries and obstruct the commutation. The factor $[T_\text{chir}, P_R]$
is non-zero whenever $\cos(\delta\phi/2) \neq 0$ — i.e., for any
non-trivial chirality-mixing tick.

## Why it matters

The bipartite tick rule, as PASS'd in
`src/utilities/tick_rule_extended_consistency.py`, mixes the chirality
components $(\psi_R, \psi_L)$ but does **not** complex-conjugate the
colour amplitude when it does so. Under Branch~B that omission is a
structural inconsistency: a chirality-flip moves amplitude from a
site where SU(3) acts on $\mathbf{3}$ to one where it acts on
$\bar{\mathbf{3}}$, and the standard linear SU(3) action cannot
absorb that change of representation.

The two routes for resolving this:

1. **Accept Branch A.** The existing tick rule forces the
   3 ⊕ 3 interpretation. The bipartite parity operator, *if*
   defined as a symmetry of this tick rule, must be linear: $P =
   \sigma_x \otimes I_2 \otimes M$ with $M$ in the symmetric
   elements of SU(3). The bipartite RGB/CMY distinction has no
   SU(3)-representation content — it is a labelling on the lattice
   sites, not a particle-vs-antiparticle distinction at the gauge
   level.

2. **Modify the tick rule for Branch~B.** Include an explicit
   $\mathbf{3} \leftrightarrow \bar{\mathbf{3}}$ conjugation on
   chirality-flipping steps, making the tick rule partially
   antilinear. This re-opens the PASS row "Tick-rule consistency
   on $\mathbb{C}^{12}$" and requires re-establishing $\mathcal{A}=1$
   preservation on the modified rule. If successful, the framework
   has a built-in discrete CP symmetry; the bipartite parity
   becomes an antilinear $(\sigma_x \otimes I_2 \otimes C) \circ K$
   with $C^T = C$ (the symmetric-unitary condition for
   $P_{CP}^2 = I$).

## Upstream-flow tags

- **Algebra:** the conjugate-representation construction $-\overline{\lambda_a}/2$
  and its commutator with the bipartite tick operator. Relevant to
  the formalization of $\mathfrak{su}(3)$ on the discrete causal
  lattice.
- **Topology / structure of the bipartition:** the RGB/CMY exchange
  as a $\mathbb{Z}_2$ that may or may not be a $C$-like operation
  depending on the SU(3) action. The lattice's bipartite parity is
  *linear* iff the colour action is sublattice-independent.
- **Balanced equations** (indirect): a reaction-style $\mathcal{A}=1$
  equation that conserves charge across sublattices must commit to
  one of the two branches; the upstream catalogues
  (`symbol-meaning-{3,4,5,6}.csv`) may need an explicit branch tag.

## Pointers

- Script: `src/utilities/su3_branch_consistency.py` (sympy
  verification; run via the project venv to reproduce the table of
  obstructions per Gell-Mann generator).
- Audit table: `paper/sections/audit_table.tex`, row "SU(3)
  representation branch consistency".
- Work plan: `notes/work_plan.md`, Phase 1 sub-task 0.
- Paper~I anchor: `external/dcl/notes/lie_algebra_automorphism_proof_sketch.md`
  Step~5 update, where the per-site $\mathbb{C}^3$ colour-memory
  amplitude is introduced.

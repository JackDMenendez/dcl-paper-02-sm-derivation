# CP modification obstruction (Phase 1.5 / Route b)

**Status:** STABLE (verified by `src/utilities/tick_rule_cp_modified.py`,
2026-05-15).
**Purpose:** Captures the structural reason the bipartite octahedral
lattice cannot incorporate SM-style CP / colour-anti-colour
distinction as a discrete symmetry of the tick rule.  This closes
Phase 1.5 / Route (b) of `notes/work_plan.md` with a definitive
negative result.
**Cited by:** the audit-table row "Modified tick rule for Branch~B
SU(3) compatibility" in `paper/sections/audit_table.tex`.

---

## The modified-tick ansatz tested

To make Branch~B SU(3) (RGB in $\mathbf{3}$, CMY in $\bar{\mathbf{3}}$)
a global symmetry, the natural modification of the bipartite tick
rule is

$$T_\text{ext}^B \;=\; is \cdot I_{12} \;+\; c \cdot (\sigma_x \otimes I_2 \otimes C) \circ K,$$

with $K$ global complex conjugation on $\mathbb{C}^{12}$ and $C$ a
$3\times 3$ matrix on the colour factor.  The first term is the
chirality-preserving piece $is \cdot I_2$ on chirality (linear); the
second is the chirality-flipping piece, made antilinear by composing
with $K$ to allow $\mathbf{3} \to \bar{\mathbf{3}}$ during chirality
flips.

## The commutator condition reduces to anticommutation with every Gell-Mann

For the antilinear part $(Y \circ K)$ with $Y = \sigma_x \otimes I_2
\otimes C$ to commute with the Branch~B SU(3) generator

$$T_a^B = P_R \otimes I_2 \otimes \tfrac{\lambda_a}{2} + P_L \otimes I_2 \otimes \left(-\tfrac{\overline{\lambda_a}}{2}\right),$$

the condition $T_a^B Y = Y \bar{T}_a^B$ in chirality-block form
collapses to

$$\lambda_a\, C \;=\; -C\, \lambda_a \qquad \text{for all } a = 1, \ldots, 8.$$

$C$ must anticommute with *every* Gell-Mann generator.

## No non-zero $C$ exists

For a diagonal generator $\lambda$, anticommutation forces
$C_{ij}(\lambda_{ii} + \lambda_{jj}) = 0$ for all $i, j$.

Apply $\lambda_3 = \mathrm{diag}(1, -1, 0)$: only $C_{12}, C_{21},
C_{33}$ are unconstrained; every other entry is zero.

Apply $\lambda_8 = \mathrm{diag}(1, 1, -2)/\sqrt{3}$ on the surviving
entries:

| Entry | $\lambda_8^{ii} + \lambda_8^{jj}$ | Constraint |
|---|---|---|
| $C_{12}$ | $+2/\sqrt{3}$ | $C_{12} = 0$ |
| $C_{21}$ | $+2/\sqrt{3}$ | $C_{21} = 0$ |
| $C_{33}$ | $-4/\sqrt{3}$ | $C_{33} = 0$ |

Conclusion: $C = 0$.  No non-zero matrix anticommutes with every
Gell-Mann generator.

## Robustness to generalisations

- **Isospin entanglement** ($Y = \sigma_x \otimes Z \otimes C$, $Z$
  any $2\times 2$ on isospin): the isospin and colour factors decouple
  in the tensor product, so the colour constraint $\lambda_a C =
  -C\lambda_a$ is unchanged.  $Z$ is a free parameter that doesn't
  rescue Branch~B.
- **More general chirality structure** ($\sigma_y$ instead of $\sigma_x$,
  or general $\alpha\sigma_x + \beta\sigma_y$): chirality-block-
  off-diagonal entries still yield the same colour anticommutation
  condition; only an overall phase changes.
- **$\mathcal{A}=1$ preservation**: not the obstruction.  Antilinear
  operators with unitary linear part automatically preserve $|\psi|^2$.
  The block is representation-theoretic, not unitarity-based.

## Representation-theoretic origin

The SU(3) fundamental $\mathbf{3}$ and conjugate $\bar{\mathbf{3}}$ are
**inequivalent** irreducible representations.  By Schur:

- *Linear* intertwiner $f: \mathbf{3} \to \bar{\mathbf{3}}$ satisfying
  $\rho(g) f = f \bar{\rho}(g)$ for all $g \in SU(3)$ must be zero.
- *Antilinear* intertwiner $f = C \circ K$ exists; Schur on
  $\overline{\bar{\rho}} = \rho$ gives $C = \alpha \cdot I$, i.e., the
  unique (up to scalar) antilinear intertwiner is global colour
  conjugation $K$ itself.

The tick rule's chirality-flipping piece $(Y \circ K)$ does contain
$K$, but Branch~B's chirality-dependent $T_a^B$ demands the
*stronger* condition

$$C \lambda_a = -\lambda_a C$$

(an anticommutation) on top of the intertwiner relation.  This
stronger condition has no non-zero solution in SU(3), because $\mathbf{3}$
has no faithful representation as a sub-representation of an
antisymmetric tensor product of itself.

## Implication for the framework

Combined with the Phase 1 Route (a) result
(`notes/chirality_alignment.md`):

- The lattice's bipartite parity is intrinsically **linear** — a
  *spatial parity* $\sigma_x \otimes I_2 \otimes I_3$ with no
  charge-conjugation component.  This is structural; it cannot be
  upgraded to a charge-parity by any natural modification of the
  tick rule.
- The proposed $SU(2)_W$ on the existing per-site amplitude couples
  **vector-like** to matter, not chirally as in the SM.
- The lattice's discrete $\mathbb{Z}_2$ (bipartite parity) is
  *orthogonal* to the SM's chirality $\mathbb{Z}_2$ ($\gamma_5$
  projector) on the chirality $\mathbb{C}^2$ — two distinct
  involutions on the same carrier.

The framework realises the **Lie algebra structure** of Eq.~(137)
of Paper~I:

$$\mathfrak{aut}(\mathcal{T}_\diamond^3, \mathcal{A}=1) \;\supseteq\; \mathfrak{so}(3,1) \oplus \mathfrak{su}(3) \oplus \mathfrak{su}(2) \oplus \mathfrak{u}(1) \quad (\dim 18)$$

— but as a *parity-conserving* gauge theory, not the SM's chiral,
CP-violating version.  The framework precisely identifies which
features of the SM are geometric consequences of the discrete causal
lattice (the Lie algebra structure) and which are not (chirality, CP
— external choices in the SM, not derivable from the lattice's
$\mathcal{A}=1$ constraint).

## Upstream-flow tags

- **Algebra:** anticommutation $\{\lambda_a, C\} = 0$ for all $a$ has
  no non-zero solution in $\mathrm{Mat}(3, \mathbb{C})$.  Verified via
  the $\lambda_3 \to \lambda_8$ argument; representation-theoretically
  the statement that $\mathbf{3}$ does not appear in
  $\Lambda^2 \mathbf{3} = \bar{\mathbf{3}}$.
- **Topology / discrete symmetries:** the bipartite octahedral
  lattice's natural $\mathbb{Z}_2$ is spatial parity $P$, not $CP$.
  $C$ and $P$ are *distinct* lattice-level operations, and only $P$
  has a natural geometric realisation.
- **Balanced equations** (direct): a reaction-style $\mathcal{A}=1$
  equation cannot have a $CP$ symmetry term derived from the
  lattice's tick rule; this constrains the kinds of conserved
  quantities the formalism can produce.

## Pointers

- Script: `src/utilities/tick_rule_cp_modified.py` (sympy; 9
  candidates tested, structural proof of impossibility, sample
  isospin-entanglement check).
- Audit table: `paper/sections/audit_table.tex`, row "Modified
  tick rule for Branch~B SU(3) compatibility" (FAIL).
- Work plan: `notes/work_plan.md`, Phase 1.5 / Route (b).
- Upstream: `notes/su3_branch_consistency.md` (the original branch
  finding that motivated Route b).
- Adjacent: `notes/chirality_alignment.md` (Route a's
  characterisation result).

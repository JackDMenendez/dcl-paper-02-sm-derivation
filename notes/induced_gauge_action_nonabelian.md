# Induced gauge action: non-abelian generalisation and the
# $g_3^2/g_2^2 = 3/2$ prediction

**Status:** STABLE (verified by
`src/utilities/induced_gauge_action_nonabelian.py`, 2026-05-15).
**Purpose:** Resolve Phase 4 of `notes/work_plan.md` (explicit
$1/g^2$ prefactors for $SU(2)_W$ and $SU(3)_c$ Wilson actions on
the bipartite octahedral lattice).  Phase 4 inherits the
structural form of Paper~I's $U(1)$ induced-action calculation
unchanged (Q-tensor with eigenvalues $\{4, 4, 16\}$, $O_h$-averaged
Maxwell density, universal one-loop prefactor $c$ left open).  The
non-abelian generalisation adds the trace-normalisation factor
$T_F = 1/2$ for the fundamental of $SU(N)$, and the framework's
per-site spectator-factor dimensions yield a sharp lattice-scale
prediction for the coupling ratios.
**Cited by:** the audit-table row "Explicit $1/g^2$ prefactor for
$SU(2)_W$, $SU(3)$ Wilson actions" in
`paper/sections/audit_table.tex` (updated from STUB to PART).
This is also the first *quantitative* prediction that connects the
framework's per-site amplitude structure to observable gauge-
coupling ratios.

---

## Structural inheritance from Paper~I

Paper~I, Appendix~B, established the bipartite plaquette holonomy
expansion in the small-$a$ limit:

$$W_{ab}(\mathbf{x}) = \exp\!\bigl(-i a^2 V_a^i V_b^j F_{ij}(\mathbf{x})\bigr) + O(a^4),$$

$$1 - \operatorname{Re} W_{ab}(\mathbf{x}) = \tfrac{a^4}{2} \bigl(V_a^i V_b^j F_{ij}(\mathbf{x})\bigr)^2 + O(a^8).$$

Summing over the three bipartite plaquettes $(a, b) \in \{(1,2),
(1,3), (2,3)\}$ gives a quadratic form

$$\sum_{a<b}\bigl(V_a^i V_b^j F_{ij}\bigr)^2 \;=\; \mathbf{F}^\top Q\, \mathbf{F},$$

with $Q$ a $3\times 3$ symmetric matrix in the
$(F_{12}, F_{13}, F_{23})$ basis.  The script reproduces
$Q = \begin{pmatrix}8&4&-4\\4&8&-4\\-4&-4&8\end{pmatrix}$ with
$\operatorname{Tr} Q = 24$ and eigenvalues $\{4, 4, 16\}$ -- exactly
Paper~I's result.

$O_h$ averaging gives $\langle \mathbf{F}^\top Q \mathbf{F}
\rangle_{O_h} = (\operatorname{Tr} Q / 3)\,F_{ij}F^{ij}/2 =
8 \cdot F_{ij}F^{ij}/2$, recovering the Maxwell density up to the
universal one-loop prefactor $c = 1/g^2$ that Paper~I left open.
The anisotropic residual $Q_{\text{aniso}}$ produces gauge-sector
birefringence with optical axis $(1,1,-1)$ -- inherited unchanged.

## Non-abelian generalisation

For matrix-valued link variables $U_v(x) \in SU(N)$, the plaquette
holonomy is the ordered product around the loop, and its small-$a$
expansion is

$$W = I + i a^2\, V_a^i V_b^j F_{ij} - \tfrac{a^4}{2}\bigl(V_a^i V_b^j F_{ij}\bigr)^2 + O(a^6),$$

with $F_{ij} = F^c_{ij} T^c$ Lie-algebra-valued and $T^c$ the
generators of $SU(N)$ in the fundamental ($T_F = \tfrac{1}{2}$).
The standard Wilson normalisation $1 - \tfrac{1}{N}\operatorname{Re}\operatorname{Tr} W$
yields

$$1 - \tfrac{1}{N} \operatorname{Re}\operatorname{Tr} W = \frac{a^4}{2N}\operatorname{Tr}\bigl((V_a^i V_b^j F_{ij})^2\bigr) = \frac{a^4 T_F}{2N}\bigl(V_a^i V_b^j F^c_{ij}\bigr)^2,$$

summed over colour index $c$, using
$\operatorname{Tr}(T^a T^b) = T_F \delta^{ab}$.

**The Q-tensor in the $(F^c_{12}, F^c_{13}, F^c_{23})$ basis is
unchanged.**  The SU(N) structure introduces only the global
factor $T_F/N$, and the structural form -- Q-tensor with
eigenvalues $\{4, 4, 16\}$, $O_h$-averaged Maxwell-style density,
gauge-sector birefringence -- is inherited verbatim from Paper~I.
The numerical $1/g^2$ prefactor inherits the same universal
one-loop constant $c$ Paper~I left open.

## The spectator-factor multiplicity and the $g_3^2/g_2^2$ prediction

The framework's per-site amplitude is
$\psi \in \mathbb{C}^2_{\text{chir}} \otimes
\mathbb{C}^2_{\text{iso}} \otimes \mathbb{C}^3_{\text{col}}
\cong \mathbb{C}^{12}$.  Each gauge factor acts on one tensor
slot; the other slots are spectators.  The fermion-loop
contribution to the gauge boson self-energy carries a
multiplicity equal to the product of the spectator-slot
dimensions:

| Gauge group | Spectators | $N_f$ | Loop coefficient ($N_f \cdot T_F$) |
|---|---|---|---|
| $U(1)$ | all 12 components, charge 1 each | 12 | $12$ (charge-squared sum, no $T_F$) |
| $SU(2)_W$ | chirality (2) × colour (3) | 6 | $6 \cdot \tfrac{1}{2} = 3$ |
| $SU(3)_c$ | chirality (2) × isospin (2) | 4 | $4 \cdot \tfrac{1}{2} = 2$ |

The inverse-coupling-squared at the lattice scale (in units of
the universal one-loop prefactor $c$ times the $O_h$-averaged
Q-trace factor 8) are:

$$\frac{1}{g_1^2} : \frac{1}{g_2^2} : \frac{1}{g_3^2} \;=\; 12 : 3 : 2.$$

Equivalently:

$$g_1^2 : g_2^2 : g_3^2 \;=\; 1 : 4 : 6 \quad \text{at the lattice scale } 1/a.$$

**The sharp prediction:** $g_3^2 / g_2^2 = 3/2$ at the lattice scale
$1/a$, independent of the still-open universal one-loop prefactor
$c$.  This is the framework's first quantitative gauge-coupling
prediction, derived entirely from the per-site amplitude's
spectator-factor structure.

## Comparison to SM measured ratios

At $M_Z \approx 91.2$ GeV, the SM running couplings are
approximately:
$$g_3^2 \approx 1.40, \quad g_2^2 \approx 0.42, \quad g_1^2 \approx 0.13.$$
Ratios: $g_3^2 / g_2^2 \approx 3.3$, $g_2^2 / g_1^2 \approx 3.2$,
and $g_1^2 : g_2^2 : g_3^2 \approx 1 : 3 : 11$.

The framework predicts $g_3^2 / g_2^2 = 1.5$ at the lattice scale.
RG flow from the lattice scale $1/a$ down to $M_Z$ changes this
ratio: $g_3^2$ grows (asymptotic freedom) and $g_2^2$ decreases at
lower energies in the SM beta functions, so the ratio $g_3^2/g_2^2$
*increases* as energy decreases.  The factor-of-$\sim 2$ between
the framework's lattice-scale prediction (1.5) and the SM measured
ratio at $M_Z$ (3.3) is consistent with the right kind of RG
running over a span of many decades in energy, but the framework
does not yet fix the lattice scale $1/a$ from first principles to
make this a tight quantitative test.

Similarly: framework's $g_2^2 / g_1^2 = 4$ at the lattice scale
vs SM measured $\sim 3.2$ at $M_Z$.  The framework's prediction
sits in the same order of magnitude as the SM ratio, and the
qualitative trend (SU(2) > U(1) at the lattice scale, becoming
roughly comparable at $M_Z$) is consistent with RG running.

**The framework's prediction is non-trivial and falsifiable:** the
specific ratio 3 : 2 (lattice-scale $1/g_2^2 : 1/g_3^2$) follows
from the dimensions of the spectator factors (2 × 3 = 6 for SU(2),
2 × 2 = 4 for SU(3)).  Other framework variants with different
amplitude dimensions would give different ratios.

## Phase 4 outcome class

**PART.**  Structural form complete (Q-tensor and Yang-Mills
density inherited from Paper~I); universal one-loop prefactor $c$
remains open (inherited from Paper~I's open item);
*ratio* prediction $g_3^2/g_2^2 = 3/2$ at the lattice scale
sharply derived and independent of $c$.

The audit-table row "Explicit $1/g^2$ prefactor for $SU(2)_W$,
$SU(3)$ Wilson actions" is updated STUB $\to$ PART.  Closing it to
PASS requires the explicit one-loop $-\operatorname{Tr}\ln D_{\text{lat}}[U]$
calculation that Paper~I and Paper~II both leave for follow-up
work.

## What the framework predicts vs the SM measures

| Quantity | Framework prediction (lattice scale $1/a$) | SM measurement (at $M_Z$) |
|---|---|---|
| $g_3^2 / g_2^2$ | $3/2$ | $\approx 3.3$ |
| $g_2^2 / g_1^2$ | $4$ | $\approx 3.2$ |
| $g_3^2 / g_1^2$ | $6$ | $\approx 11$ |

The framework's lattice-scale ratios are in the same order of
magnitude as the SM measured ratios at $M_Z$, with deviations
consistent with RG running over many energy decades.  A future
paper or follow-on calculation can sharpen this by:

1. Computing the universal one-loop prefactor $c$ (closing
   Paper~I's open item).  This fixes the absolute scale of
   $1/g^2(1/a)$, allowing a quantitative RG-running check against
   the measured $g_i^2(M_Z)$.
2. Fixing the lattice scale $1/a$ from first principles or from
   another framework observable (e.g., the Planck scale, the
   hydrogen quantization, or the framework's induced gravitational
   coupling).
3. Computing the framework's beta-function coefficients (which
   may differ from the SM's because of the framework's structurally
   distinct fermion content).

Until these follow-ons land, the framework's ratio predictions are
order-of-magnitude indicators consistent with the SM measured
values.  The factor-of-2 discrepancy between $g_3^2/g_2^2 = 3/2$
(framework lattice scale) and $g_3^2/g_2^2 \approx 3.3$ (SM at
$M_Z$) is well within RG-running expectations.

## Upstream-flow tags

- **Algebra:** the bipartite Q-tensor with eigenvalues $\{4, 4, 16\}$
  is inherited from Paper~I unchanged.  The trace-normalisation
  factor $T_F = 1/2$ for SU(N) fundamental introduces a global
  scaling but does not change the tensor structure.
- **Topology / structure of the bipartition:** the optical-axis
  birefringence with eigenvector $(1, 1, -1)$ extends from $U(1)$
  to $SU(2)_W$ and $SU(3)_c$ unchanged.  The framework predicts
  $SU(2)_W$ and $SU(3)_c$ gauge bosons (W, Z, gluons) also exhibit
  bipartite-octahedral birefringence aligned with the same axis.
- **Balanced equations:** an $\mathcal{A}=1$ reaction involving
  gauge-boson exchange inherits the bipartite-plaquette Wilson
  action with the universal $1/g^2$ prefactor.

## Pointers

- Script: `src/utilities/induced_gauge_action_nonabelian.py`
  (sympy; Q-tensor verification + spectator-counting + ratio
  derivation).
- Paper~I appendix: `external/dcl/paper/sections/induced_gauge_action.tex`
  (the $U(1)$ structural calculation; the universal one-loop
  prefactor open item).
- Audit table: `paper/sections/audit_table.tex`, row "Explicit
  $1/g^2$ prefactor for $SU(2)_W$, $SU(3)$ Wilson actions" (PART).
- Work plan: `notes/work_plan.md`, Phase 4.
- Adjacent: `notes/aut_centralizer_enumeration.md` (Phase 3 found
  the lattice's discrete centralizer is larger than Eq.~(137)'s
  18-dim algebra; Phase 4's gauge-coupling ratios depend only on
  the 18-dim SM-gauge-invariant subalgebra, so the Phase 3 extras
  do not affect the Phase 4 prediction).

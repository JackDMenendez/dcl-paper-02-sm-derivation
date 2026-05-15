# Mass, chirality, and the impossibility of chiral gauge coupling

**Status:** STABLE (synthesises three established results, no new
script — the constituent verifications already exist; this note
ties them into a single structural statement).
**Purpose:** Capture the structural coherence between Paper~I's
"mass = clock density" identification and Paper~II's Phase~1
results.  The three findings are three faces of one kinematic
feature: the bipartite tick rule mixes chirality as its kinetic
mechanism, which simultaneously generates mass AND precludes
chiral gauge coupling.  Equivalently: Paper~II establishes that
**every gauge structure consistent with the lattice preserves the
clock density** — a key Paper~II $\to$ Paper~I support relation.
**Cited by:** Will be folded into the paper as a subsection of the
characterisation discussion once Phase~2-4 close.  Captured here
as a structural-insight note for upstream flow and so the synthesis
isn't lost.

---

## The tick rule's chirality structure

The bipartite chirality tick on the per-site $(\psi_R, \psi_L)$
amplitude is, from
`src/utilities/tick_rule_extended_consistency.py`:

$$T_\text{chir} \;=\; i\sin(\delta\phi/2)\, I_2 \;+\; \cos(\delta\phi/2)\, \sigma_x.$$

Two pieces, geometrically distinct:

- The diagonal $i\sin(\delta\phi/2)\, I_2$ is a chirality-preserving
  phase advance — it is the **kinetic** part of the local tick.
- The off-diagonal $\cos(\delta\phi/2)\, \sigma_x$ is a chirality-
  *mixing* amplitude — it shuttles amplitude between $\psi_R$ and
  $\psi_L$ on every tick.

These map onto the standard Dirac decomposition in the chiral basis,
where the Hamiltonian splits as $H = (\text{kinetic, } \propto \gamma_5\text{-commuting})
+ (\text{mass, } \propto \gamma_5\text{-anticommuting})$.  The
$\sigma_x$ in the tick is precisely the lattice realisation of the
Dirac mass operator $m(\bar\psi_L\psi_R + \bar\psi_R\psi_L)$ — it
anticommutes with $\gamma_5 = \sigma_z$.

## The "mass = clock density" identification

Paper~I identifies the rate of bipartite alternation — the clock
density at a site — with what becomes the fermion mass in the
continuum limit.  Mechanically, this is the statement that the
chirality-mixing amplitude $\cos(\delta\phi/2)$ is the spectral
parameter that becomes $m$.  The Zitterbewegung frequency
$\omega_Z = 2mc^2/\hbar$ of a massive Dirac particle is exactly the
frequency at which the wavefunction oscillates between chirality
components — i.e., the rate of bipartite alternation.  A high
clock density (frequent ticks) yields strong chirality oscillation,
hence large mass.

In limits:

| $\delta\phi$ | $\sin(\delta\phi/2)$ | $\cos(\delta\phi/2)$ | Interpretation |
|---|---|---|---|
| $\to 0$ | small | $\approx 1$ | maximal chirality mixing per tick — heavy mass / strong Zitterbewegung |
| $= \pi/2$ | $\sqrt 2/2$ | $\sqrt 2/2$ | balanced |
| $\to \pi$ | $\approx 1$ | $\to 0$ | no chirality mixing — degenerate "Weyl" limit (trivializes the dynamics) |

The framework's natural regime has $\cos(\delta\phi/2) > 0$, which
means every tick mixes chirality — every lattice fermion is
intrinsically massive.

## Why this rules out chiral gauge coupling

A chiral gauge coupling — the SM's $SU(2)_W$ acting on $\psi_L$ as
a doublet and treating $\psi_R$ as a singlet — requires the $L$ and
$R$ sectors to be *separable* under time evolution.  Gauge
invariance demands that a state in the doublet representation stay
in the doublet representation as it evolves.  If the kinetic
operator constantly mixes $\psi_L$ and $\psi_R$, a doublet state
shuttles into the singlet sector on every tick, and the gauge
representation is broken.

The lattice's bipartite tick rule *does* constantly mix chirality —
that's the mass mechanism.  So a chiral $SU(2)_W$ on the existing
carrier is structurally incompatible with the kinetic dynamics.
The only gauge couplings consistent with the tick rule are
**vector-like**: the same gauge action on $\psi_R$ and $\psi_L$
(treating chirality components symmetrically, so the kinetic
mixing doesn't violate gauge invariance).  This is exactly what
`src/utilities/chirality_parity_alignment.py` verifies:
$P\, T_a^W\, P^{-1} = T_a^W$ — the proposed $SU(2)_W$ commutes with
bipartite parity, i.e., couples vector-like.

## How the SM evades this constraint

The SM separates kinetic and mass terms by introducing a Higgs
field that generates mass via Yukawa coupling rather than building
it into the kinetic operator.  This gives a **two-phase structure**:

- *Above EWSB* (high energy): fermions are massless; $\psi_L$ and
  $\psi_R$ live in different gauge representations of $SU(2)_W$;
  chirality is a manifest gauge label; the kinetic operator
  preserves chirality.
- *Below EWSB* (low energy): the Higgs VEV induces a Yukawa-type
  mass term that mixes $\psi_L$ and $\psi_R$, but this term is
  itself gauge-covariant because the Higgs carries the appropriate
  $SU(2)_W$ charge.  Gauge invariance is maintained through the
  Higgs's gauge transformation properties.

The lattice has no analogue of this two-phase structure.  There is
no "massless regime" where the tick rule turns off chirality
mixing — turning it off means $\cos(\delta\phi/2) = 0$, which
trivializes the dynamics.  Mass is unconditionally built into the
kinetic mechanism.

## The structural coherence

Three independently verified results combine:

1. **Paper~I:** mass = clock density.  The chirality-mixing
   amplitude $\cos(\delta\phi/2)$ IS the lattice realisation of the
   Dirac mass.
2. **Phase~1 Route (a)** (`chirality_parity_alignment.py`): the
   proposed $SU(2)_W$ on the existing per-site amplitude commutes
   with bipartite parity (vector-like coupling, not chiral).
3. **Phase~1.5 Route (b)** (`tick_rule_cp_modified.py`): no natural
   antilinear modification of the tick rule admits Branch~B SU(3)
   or SM-style $CP$.

These are not three independent findings — they are three
projections of one kinematic feature:

> *The lattice's clock is a chirality-mixing operator at every step.*

Mass, chirality mixing, vector-like gauge coupling, and the
impossibility of $CP$ are all consequences of this single
kinematic fact.  The framework predicts a parity-conserving Lie
group structure ($SO(3,1) \times SU(3) \times SU(2) \times U(1)$,
the Lie algebra of Eq.~(137)) with mass *built into* the kinetic
term — geometrically distinct from the SM's "kinetic + Higgs +
Yukawa" three-piece structure.

## What this predicts about the SM

The framework recasts the SM's chiral structure as an *artifact of
the Lagrangian formalism's separation of kinetic and mass terms* —
a separation that doesn't survive when mass *is* the kinetic
mechanism.  Two interpretations of this prediction:

1. **Effective-theory reading:** the SM's chiral phase above EWSB
   is an effective description that emerges at scales where the
   lattice tick rule is averaged over.  At the lattice scale, the
   tick rule's chirality mixing is operative; the SM's chiral
   structure is recovered only in a coarse-grained limit.  This
   would be a strong prediction: deviations from chiral SM
   predictions at extreme energies / short distances.

2. **Disagreement reading:** the SM's chiral structure is a
   genuine feature of nature that the discrete causal lattice
   does not capture.  In this case, the framework as currently
   formulated is incomplete and needs additional structure (e.g.,
   an explicit Higgs-analogue, additional discrete symmetries, or
   a richer per-site amplitude) to recover chirality.

Either reading is publishable.  The framework's contribution is
identifying *precisely which* features of the SM are geometric
(the Lie algebra structure of Eq.~(137)) and *which are not*
(chirality, $CP$, the Higgs mechanism).

## Clock-density preservation as Paper~I support

The relationship between Paper~II and Paper~I is asymmetric.
Paper~I established the mass-as-clock-density identification on the
existing per-site $\mathbb{C}^2 = (\psi_R, \psi_L)$ amplitude.
Paper~II asks what gauge structures are *consistent* with that
identification, and finds that the answer is narrow: only
parity-conserving, vector-like couplings.  Chiral $SU(2)_W$ and
SM-style $CP$ both fail because they would require turning off the
chirality mixing that *is* the clock — and the lattice has no
mechanism to do so.

Put another way: **every gauge structure that Paper~II verifies as
a global symmetry of the bipartite tick rule automatically
preserves the clock density**.  Branch~A SU(3), the vector-like
$SU(2)_W$, the U(1) phase, the Lorentz factor, and the linear
bipartite parity all commute with the chirality-mixing tick.  The
candidates that Phase~1 rules out (Branch~B SU(3), chiral
$SU(2)_W$, antilinear $P_{CP}$) are precisely the ones that would
*not* preserve the clock density: they would either treat $\psi_R$
and $\psi_L$ asymmetrically (chiral coupling) or require
sublattice-dependent SU(3) representations that break the
chirality-mixing symmetry the clock depends on.

This is a non-trivial Paper~II $\to$ Paper~I support finding:
the framework's gauge structure is *forced* to respect the clock
density that Paper~I identified.  The clock-density identification
was a Paper~I postulate; Phase~1 of Paper~II shows it is also a
*selection principle* — the criterion that distinguishes the
admissible gauge structures from the inadmissible ones.  If
clock-density preservation were merely a soft choice, the framework
could in principle support chiral gauge couplings (with a Higgs-
analogue softening the clock at high energies); the rigid
incompatibility shown by Phases~1 and 1.5 means clock density is a
*structural* feature of the lattice, not an emergent or soft one.

The complement is also informative.  The fact that the SM
*violates* this selection principle (chiral gauge coupling exists
empirically; $CP$ violation is observed) is the framework's
sharpest empirical interface: either the lattice is the
fundamental substrate and the SM's chiral structure is an emergent
artifact above a tick-coarse-graining scale, or the lattice is
incomplete and needs additional structure to accommodate the SM's
two-phase chirality / mass split.  Both readings preserve
Paper~I's clock-density claim; what they disagree on is whether
the SM's chirality is a derivable consequence or an external
input.

## Upstream-flow tags

- **Algebra:** the lattice tick on chirality is in the
  $\{I, \sigma_x\}$ algebra — purely the $\gamma_5$-anticommuting
  (mass) part of the Dirac decomposition, with no $\sigma_z$
  (chirality-preserving kinetic) component on chirality alone.
  Spatial $\sigma_z$ enters via spatial hops $\mathbf{V}_i$,
  decoupled from the chirality tick.
- **Topology of the bipartition:** the chirality mixing is
  *structurally* the bipartite alternation — same kinematic event
  viewed two ways.  The bipartite parity ($\sigma_x$) and the mass
  operator ($\sigma_x$ in the chiral basis) are the same operator
  on the per-site $\mathbb{C}^2$.
- **Balanced equations:** any $\mathcal{A}=1$-conserving reaction
  in the framework's algebra inherits this structure — the mass
  term is the bipartite hop, and there is no $CP$ symmetry to
  conserve.

## Pointers

- Paper~I (clock-density / mass identification): the per-site
  oscillator dispersion relation; relevant section is
  Paper~I~§7--§8 in the
  [Zenodo v1.0 deposit](https://doi.org/10.5281/zenodo.20078529).
- Phase~1 Route (a): `notes/chirality_alignment.md`,
  `src/utilities/chirality_parity_alignment.py`.
- Phase~1.5 Route (b): `notes/cp_modification_obstruction.md`,
  `src/utilities/tick_rule_cp_modified.py`.
- SU(3) branch consistency: `notes/su3_branch_consistency.md`,
  `src/utilities/su3_branch_consistency.py`.
- Paper~II prose hook: `paper/sections/established_factors.tex`
  closing subsection
  `subsec:established_necessity_vs_sufficiency` item (ii) — the
  framework-level synthesis will eventually live there or in a
  new subsection of its own.

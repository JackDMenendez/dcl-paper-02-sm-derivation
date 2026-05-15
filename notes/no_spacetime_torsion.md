# Why the lattice does not need spacetime torsion (or curvature)

**Status:** STABLE (direct reading of Paper~I's
gravity-as-clock-density account; this note makes the implication
for torsion explicit, since Paper~I does not name torsion
directly).
**Purpose:** Record that the framework's substrate-first geometry
makes both spacetime curvature *and* torsion superfluous in their
conventional roles --- not as objections to general relativity or
Einstein-Cartan theory, but as a consequence of the framework
re-routing gravity through clock-density refraction and fermion
spin through bipartite chirality oscillation.  The corresponding
apparatus (affine connections, spin connections $\omega_\mu^{ab}$,
Christoffel symbols $\Gamma^\mu_{\nu\rho}$, the metric $g_{\mu\nu}$
as a dynamical field) does not enter the framework.
**Cited by:** Future Paper~II prose (a single-sentence
acknowledgement in the conclusion or
`paper/sections/established_factors.tex`, once a natural hook is
identified).  Will also flow upstream to
`external/research/Notes/` as a structural observation about the
framework's geometric primitives.

---

## What Paper~I says, and what it does not say

Paper~I~§7 ("Gravity as Clock Density",
`external/dcl/paper/sections/gravity_as_clock_density.tex`) opens:

> *General relativity describes gravity as the curvature of a
> four-dimensional spacetime manifold.  The $\mathcal{T}_\diamond^3$
> framework offers a different account, which we argue is more
> fundamental: gravity is a refraction of causal paths through
> regions of higher session density.  No curved geometry is
> required or assumed.*

That last sentence rules out *all* of Riemann-Cartan geometry, not
just curvature.  A search of the Paper~I source for "torsion,"
"Levi-Civita," "Christoffel," "spin connection," "vierbein,"
"tetrad," "frame field," and "covariant derivative" returns zero
matches across the entire repository.  The omission is structural,
not an oversight --- the framework replaces the entire connection
apparatus with something simpler.

## What the lattice *does* carry, geometrically

The bipartite octahedral lattice $\mathcal{T}_\diamond^3$ has:

- **Fixed basis vectors** $\mathbf{V}_1, \mathbf{V}_2, \mathbf{V}_3$
  at every site in $\mathbb{R}^3$ (and their CMY negatives
  $-\mathbf{V}_i$).  No parallel transport that could generate
  non-trivial curvature or torsion --- the basis is globally rigid.
- **A scalar clock-density field**
  $\rho_\text{clock}(\mathbf{x}, t)$ whose gradient sources what
  conventional physics interprets as a gravitational potential.
  The framework's gravitational "geometry" is a scalar field on a
  flat substrate, not a tensor on a manifold.
- **A bipartite tick rule** that mixes the chirality components
  $\psi_R$ and $\psi_L$ on a per-site $\mathbb{C}^2$.  The chirality
  structure is intrinsic to the tick rule, *not* introduced via a
  spin connection $\omega_\mu^{ab}$ on a curved manifold.

The framework's "geometry" therefore consists of three primitives:
(i) a flat discrete substrate with fixed basis, (ii) a scalar
density field on it, and (iii) a discrete time-step operator that
acts on a per-site $\mathbb{C}^{12}$.  None of the three carries
information that would be encoded as Christoffel or
spin-connection coefficients in a conventional formulation.

## Why $\mathcal{A}=1$ propagates the conclusion

The unity constraint $\mathcal{A}=1$ is a global conservation law
on amplitudes, $\sum_{\mathbf{x}} (|\psi_R|^2 + |\psi_L|^2) = 1$.
This is probability conservation across the lattice; it does not
invoke a covariant derivative, a parallel-transport rule, or any
connection-based notion of how amplitudes at different sites
relate.  The dynamical statement is the discrete tick rule's
unitarity, not a continuum field equation involving
$D_\mu = \partial_\mu + \Gamma_\mu + \omega_\mu$.

So $\mathcal{A}=1$ derivations inherit the connection-free
geometry by default: every theorem proved on the basis of
$\mathcal{A}=1$ + the tick rule + the lattice basis is a theorem
about a flat, connectionless substrate.  Torsion never appears in
the statements because it is not in the language of the
statements.

## Einstein-Cartan's motivation is moot in this framework

Einstein-Cartan theory was developed because conventional GR
couples to fermions through a spin connection, and the spin
connection becomes torsionful when fermion spin is present (the
spin tensor sources torsion via Cartan's equation).  The framework
does not introduce a spin connection at all: the Dirac equation
emerges from the bipartite tick rule's chirality-mixing structure
(see `src/utilities/tick_rule_extended_consistency.py` for the
extended C^12 verification and Paper~I~§5--§6 for the original
derivation), and the spinor components $\psi_R, \psi_L$ are the
framework's primitive amplitudes, not sections of a spinor bundle
requiring a connection.

The question Einstein-Cartan answers --- "how do Dirac fermions
couple to a curved spacetime?" --- never arises in the framework,
because the framework has *neither* curved spacetime *nor* fermions
as bundle sections on it.  Both halves of the conventional
fermion-on-spacetime setup are replaced by substrate-intrinsic
structure.

## Connection to Paper~II

Paper~II inherits the geometric stance unchanged.  The automorphism
factors of Eq.~(137) act on:

- the chirality $\mathbb{C}^2 = (\psi_R, \psi_L)$ for $SO(3,1)$
  (in the emergent Weyl-spinor sense of Paper~I~§6 via
  $O_h$-averaging, *not* as a tangent-space action on a curved
  manifold);
- the extended per-site $\mathbb{C}^{12}$ for $SU(3) \times SU(2)
  \times U(1)$ (acting on internal tensor factors of the per-site
  amplitude, not on a frame bundle).

Nowhere does $SO(3,1)$ require a spin connection in the
conventional sense, because the lattice's $SO(3,1)$ is a global
symmetry of the flat substrate's $O_h$-averaged dynamics, not the
gauge group of a local Lorentz frame.

The framework's terminal prediction is therefore even more
stripped-down than "parity-conserving Standard Model gauge group":
it is parity-conserving SM gauge group *on a flat substrate, with
gravity as a scalar density field, with no Christoffel and no
torsion*.  Conventional GR and Einstein-Cartan are not the
framework's continuum limits in the sense of being recovered as
Riemann/Cartan geometries; they are *alternative descriptions*
whose curvature and torsion encode (in the framework's reading)
the same observable information that the clock-density field
encodes directly.

## A draft for Paper~II's eventual prose

A single-sentence acknowledgement somewhere in the conclusion or
in `paper/sections/established_factors.tex`:

> The framework's gravitational account (Paper~I~§7) is a scalar
> clock-density field on the flat bipartite lattice, not a curved
> spacetime metric.  Spacetime torsion --- the antisymmetric part
> of the affine connection in Einstein-Cartan theory --- is
> therefore not a separate ingredient the framework requires; its
> conventional motivation (coupling Dirac spin to curved gravity)
> is moot because the lattice provides the Dirac structure
> intrinsically through the bipartite tick rule's chirality
> oscillation, without ever invoking a spin connection.

This sits naturally as a methodological aside, or as a short note
of its own in `established_factors.tex` for the readers who would
otherwise ask "what about Einstein-Cartan?".

## Upstream-flow tags

- **Notation:** the framework's geometric primitives are basis
  vectors + scalar density + tick operator, not metric +
  connection.  The notation catalogues in
  `external/research/Notes/balanced_equations/` should record this
  explicitly; reaction-style $\mathcal{A}=1$ equations live on the
  flat substrate, not on a curved manifold.
- **Topology / structure of the bipartition:** the lattice's
  rigidity (fixed $\mathbf{V}_i$ at every site, no parallel
  transport) is what rules out curvature and torsion from the
  ground up.  This is a structural feature, not an assumption that
  could be relaxed.
- **Balanced equations:** $\mathcal{A}=1$ reactions involving
  fermion sessions do not pick up a torsion contribution because
  the fermion's spin structure is in the per-site $\mathbb{C}^2$,
  not in a spacetime spin connection.

## Pointers

- Paper~I~§7 (gravity_as_clock_density.tex), the canonical
  statement: "No curved geometry is required or assumed."
- Paper~I~§5--§6 (emergent_kinematics.tex and adjacent), where
  the Dirac structure emerges from the bipartite tick rule with
  no spin connection introduced.
- `src/utilities/automorphism_direct_product.py` --- the Lorentz
  generators $J_a, K_a$ act on the chirality $\mathbb{C}^2$
  intrinsically, with no role for a spacetime spin connection.
- `notes/mass_chirality_coupling.md` --- the related observation
  that the lattice's "kinetic" mechanism is intrinsic, not
  parallel-transport-based.
- `notes/debt_to_measurement.md` --- the framework's stripped-down
  geometry agrees with GR's observable predictions because both
  are calibrated against the same measurements, not because the
  framework reproduces GR's Christoffel structure.

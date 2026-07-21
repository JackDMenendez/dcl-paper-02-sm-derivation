# dcl-paper-02-sm-derivation

**Paper II of the A=1 Discrete Causal Lattice series.**

The central thesis is to prove (or characterise the obstruction to)
Eq.~(137) of Paper I -- the conjecture that the automorphism group
of the bipartite octahedral causal lattice under the unity
constraint is the Standard Model gauge group times Lorentz:

$$
\mathrm{Aut}(\mathcal{T}_\diamond^3, \mathcal{A}=1)
\;=\; SO(3,1) \times SU(3) \times SU(2) \times U(1).
$$

Both sides are precise finite-dimensional Lie algebras:
$\dim = 6 + 8 + 3 + 1 = 18$. Paper I (*Geometry First*,
[doi:10.5281/zenodo.20078529](https://doi.org/10.5281/zenodo.20078529))
established the framework and stated the conjecture as its central
open question. Paper II takes up the calculation.

## Paper

*Geometry Forces Physics: A Lie-Algebra Derivation of the Standard
Model Gauge Group from a Single Conservation Law* — Paper II of the
A=1 Discrete Causal Lattice series.

- Landing page: [geometryinducedphysics.org/papers/paper-02-geometry-forces-physics](https://geometryinducedphysics.org/papers/paper-02-geometry-forces-physics.html)
- Citation (canonical, Zenodo): [doi.org/10.5281/zenodo.20292158](https://doi.org/10.5281/zenodo.20292158)

## Status

Published at **v1.01** (Zenodo
[doi.org/10.5281/zenodo.20292158](https://doi.org/10.5281/zenodo.20292158);
prior v1.0
[doi.org/10.5281/zenodo.20240736](https://doi.org/10.5281/zenodo.20240736)).

What is established (sympy-verified, inherited from Paper I's
v1.0 release):

- The discrete spatial automorphism $\mathrm{Aut}(\Gamma, V)$ has
  order 48 and is isomorphic to the cubic point group $O_h \cong
  B_3$.
- The existing per-site $\mathbb{C}^2 = (\psi_R, \psi_L)$ amplitude
  carries $SO(3,1) \times U(1)$ (dim 7); the proposed per-site
  $SU(2)$ generators on this carrier are the same matrices as the
  Lorentz rotation subgroup.
- The RGB sublattice symmetry contributes only $\mathbb{Z}_3
  \subset SU(3)$, which is abelian and cannot generate non-abelian
  $SU(3)$.
- On the extended per-site amplitude $\mathbb{C}^{12} =
  \mathbb{C}^2 \otimes \mathbb{C}^2 \otimes \mathbb{C}^3$ (chirality
  $\otimes$ weak-isospin $\otimes$ colour), the four conjecture
  factors commute pairwise (direct product, dim 18 verified).
- A trivial tensor-product extension of the bipartite tick rule to
  $\mathbb{C}^{12}$ preserves $\mathcal{A}=1$, parity, and the global
  $SU(2)_W \times SU(3)$ symmetries.
- The bipartite Wilson plaquette $V_1, -V_2, -V_1, V_2$ is the
  smallest non-trivial closed loop on the bipartite octahedral
  lattice and its trace is gauge-invariant by the cyclic property.

What Paper II resolves (the substance of the paper):

1. **Exact equality vs containment** in $\mathrm{Aut}_\text{ext}$.
   Containment $\supseteq$ holds; exact equality $=$ does **not**. The
   dim-71 discrete-Hermitian centralizer $\mathfrak{su}(6) \oplus
   \mathfrak{su}(6) \oplus \mathfrak{u}(1)$ is enumerated, and the SM
   gauge algebra is recovered as its *factor-product projection*.
2. **SM-chirality coupling.** Bipartite parity is spatial parity
   (orthogonal Bloch involution to $\gamma_5$); chirality and $CP$
   violation are shown **not** derivable from the discrete substrate.
3. **Explicit $1/g^2$ prefactor** for the $SU(2)_W$ and $SU(3)$ Wilson
   actions. The dimensionless ratio $g_3^2/g_2^2 = 3/2$ at the lattice
   scale is derived from spectator-factor counting; the universal
   prefactor remains open, deferred to the planned discrete-probability
   paper.

The result is therefore a precise characterisation rather than a clean
identity: the Standard Model gauge structure is the
factor-product-effective shadow of a larger, left--right-symmetric
lattice symmetry. All claims are symbolically verified by the sympy
scripts in `src/utilities/` and tagged in the audit table.

## Structure

Same layout as `dcl-paper-experiment-template`:

```
paper/main.tex + sections/ + macros/ + figures/ + paper-bib/
src/{core,experiments,utilities}/
tests/
data/
notes/
release_notes/
audit_universe.py + audit_universe.md
```

## The evidence base

`src/utilities/` carries the six computational scaffolding scripts
inherited from Paper I's v1.0 release:

| Script | What it establishes |
|---|---|
| `automorphism_discrete.py` | Discrete $\mathrm{Aut}(\Gamma, V)$ order 48; 12 elements orthogonal in $\mathbb{R}^3$. |
| `automorphism_rgb_su3.py` | RGB symmetry contributes only $\mathbb{Z}_3 \subset SU(3)$. |
| `automorphism_direct_product.py` | $SO(3,1) \times U(1)$ on existing $\mathbb{C}^2$; per-site $SU(2)$ overlaps with Lorentz rotations. |
| `automorphism_direct_product_extended.py` | Direct-product (dim 18) on extended $\mathbb{C}^{12}$. |
| `tick_rule_extended_consistency.py` | Trivial tensor extension preserves $\mathcal{A}=1$, parity, $SU(2)_W \times SU(3)$. |
| `tick_rule_gauge_invariance.py` | Wilson plaquette gauge invariance. |

`paper/sections/audit_table.tex` is the canonical PASS / STUB
mapping; `audit_universe.py` parses it and the cached
`data/*.log` for status reporting.

## Build

Same as Paper I:

```sh
./setup.sh                  # POSIX / MSYS2 UCRT64 on Windows
./build.sh paper            # PDF -> .build/dcl-paper-02-sm-derivation.pdf
python audit_universe.py    # PASS/STUB roll-up against the seeded table
```

## License

Paper text and figures: CC BY 4.0.
Source: MIT (see `LICENSE`).

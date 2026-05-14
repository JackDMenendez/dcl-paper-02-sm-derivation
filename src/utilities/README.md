# src/utilities/

Symbolic verification scripts that establish the load-bearing
sub-claims of Eq.~(137) of Paper~I (the central conjecture this
paper takes up). All six scripts originate in Paper~I's v1.0
release; they are reproduced here as the evidence base for
Paper~II's audit table (`paper/sections/audit_table.tex`).

| Script | Audit row it backs | What it establishes |
|---|---|---|
| `automorphism_discrete.py` | Discrete spatial $\mathrm{Aut}(\Gamma, V)$ has order 48 | Enumerates the 48 basis-preserving linear maps on $\{\pm V_1, \pm V_2, \pm V_3\}$; identifies the 12 elements orthogonal in $\mathbb{R}^3$; isomorphic to $B_3 \cong O_h$. |
| `automorphism_rgb_su3.py` | RGB symmetry $\subset \mathbb{Z}_3 \subset SU(3)$ | The cyclic shift of the three RGB basis vectors generates a $\mathbb{Z}_3$ subgroup. Abelian -- cannot generate non-abelian $SU(3)$. |
| `automorphism_direct_product.py` | $SO(3,1) \times U(1)$ on existing $\mathbb{C}^2$ | Verifies $[\mathfrak{so}(3,1), \mathfrak{u}(1)] = 0$ on the existing per-site $\mathbb{C}^2 = (\psi_R, \psi_L)$ amplitude (dim 7); shows that the proposed per-site $SU(2)$ generators on this carrier are the same matrices as the Lorentz rotation subgroup -- so $SU(2)_W$ requires a structural extension. |
| `automorphism_direct_product_extended.py` | Direct-product on extended $\mathbb{C}^{12}$ | On $\mathbb{C}^{12} = \mathbb{C}^2 \otimes \mathbb{C}^2 \otimes \mathbb{C}^3$ (chirality $\otimes$ weak-isospin $\otimes$ colour), all four conjecture factors $SO(3,1) \times SU(3) \times SU(2) \times U(1)$ commute pairwise. Total dim 18. |
| `tick_rule_extended_consistency.py` | Tick-rule consistency on $\mathbb{C}^{12}$ | The trivial tensor extension $T_\text{ext} = T_\text{chirality} \otimes I_2 \otimes I_3$ of the bipartite tick rule preserves $\mathcal{A}=1$, the bipartite parity action, and the global $SU(2)_W \times SU(3)$ symmetries. |
| `tick_rule_gauge_invariance.py` | Wilson plaquette gauge invariance | The matter bilinear $\psi^\dagger(x)\, U_i(x)\, \psi(x+V_i)$ is gauge-invariant under local $U(1)$ and $SU(2)$ (sample); the smallest non-trivial bipartite plaquette is the 4-link square $V_1, -V_2, -V_1, V_2$ (no triangles since $V_1+V_2+V_3 \neq 0$); $\mathrm{Tr}(W) = 2\cos(a_1+a_2+a_3+a_4)$ gauge-invariant by cyclic property. |

## Running

Each script is self-contained sympy. Run by name:

```sh
python src/utilities/automorphism_discrete.py
python src/utilities/tick_rule_gauge_invariance.py
# etc.
```

A successful run prints the verification result and exits 0; failure
raises and exits non-zero. The output of each run is the operational
PASS for the corresponding audit-table row.

## Provenance

Verbatim copies of the v1.0 versions in Paper~I
(`external/dcl/src/utilities/` -- the Windows directory junction
that points at the local dcl checkout; see CLAUDE.md for the
convention -- archived at
[doi:10.5281/zenodo.20078529](https://doi.org/10.5281/zenodo.20078529)).
Edits should be additive (e.g.\ extending a verification to a new
generator) rather than refactoring -- the printed output is cited in
the audit table and any rephrasing risks invalidating that citation.

## Beyond the inherited six

New scripts that establish the open subproblems
(Section subsec:open_subproblems of the paper) belong here:

- An exact-equality check on $\mathrm{Aut}_\text{ext}$ generators
  (constrained Lie-algebra enumeration).
- An SM-chirality coupling test: whether the bipartite RGB/CMY
  parity is the SM's chirality projector, and whether the proposed
  $SU(2)_W$ couples asymmetrically to $\psi_R$ vs $\psi_L$.
- A non-abelian $1/g^2$ calculation on the bipartite octahedral
  lattice (analogue of Paper~I's induced-gauge-action $U(1)$
  calculation).

Each new script should drop a row into `audit_table.tex`'s evidence
column at the same time it lands.

# Lie-algebra automorphism conjecture: working sketch (Paper II)

**Status:** STARTER -- pointer to the parent proof sketch in Paper~I.

**Purpose:** anchor the working notes for Paper~II's main calculation
(closing Eq.~(137) of Paper~I) and link to the parent sketch from
which this paper inherits its structure.

**Cited by:** introduction.tex (currently); section bodies once the
paper grows beyond the introduction.

---

## What this note will become

The home for Paper~II's working derivation of the three open
subproblems identified in the introduction:

1. Exact equality vs containment in $\mathrm{Aut}_\text{ext}$.
2. SM-chirality coupling alignment.
3. Explicit $1/g^2$ prefactor for the $SU(2)_W$ and $SU(3)$ Wilson
   actions.

Each subproblem gets its own subsection here as the calculations
develop, then promotes to a paper section once the argument is
complete enough to typeset.

## What is already in place

The parent proof sketch in Paper~I lays out the dimension count, the
required commutation relations, and the structural decomposition of
the conjecture into established factors and structural extensions:

- `external/dcl/notes/lie_algebra_automorphism_proof_sketch.md`

This is the v1.0 working note; reading it cold is the best
starting point for picking up Paper~II's calculation.

`external/dcl/` is a Windows directory junction pointing at the dcl
repo (Paper~I); see CLAUDE.md ("Cross-references to Paper~I") for
the convention and how to recreate the junction on a fresh clone.

The six computational scaffolding scripts in `src/utilities/`
verify the established sub-claims:

- `automorphism_discrete.py`
- `automorphism_rgb_su3.py`
- `automorphism_direct_product.py`
- `automorphism_direct_product_extended.py`
- `tick_rule_extended_consistency.py`
- `tick_rule_gauge_invariance.py`

Their outputs are cited in `paper/sections/audit_table.tex`.

## Open questions (mirrors `paper/sections/audit_table.tex`)

1. **Exact equality vs containment.** The verified statement is
   $\mathrm{Aut}_\text{ext} \supseteq SO(3,1) \times SU(3) \times
   SU(2) \times U(1)$. The conjecture asserts $=$. Tractable by
   Lie-algebra enumeration on the extended generators, constrained
   by commutation with the established factors.

2. **SM-chirality coupling alignment.**
   - (a) Is the bipartite RGB/CMY parity the same $\mathbb{Z}_2$ as
     the SM's chirality projector?
   - (b) Does the proposed $SU(2)_W$ on the per-site weak-isospin
     $\mathbb{C}^2$ couple asymmetrically to $\psi_R$ vs $\psi_L$,
     as required by the SM, or symmetrically (which would predict
     no chiral fermions)?

3. **Explicit $1/g^2$ prefactor.** The Sakharov-style induced-action
   calculation in Paper~I's `paper/sections/induced_gauge_action.tex`
   (the $U(1)$ case) generalises to non-abelian link variables; the
   coefficient calculation has not yet been done.

## Pointers

- Paper~I §15: `external/dcl/paper/sections/conclusion.tex` (the
  conjecture statement that anchors this paper, Eq.~(137) of the v1.0
  PDF).
- Paper~I Appendix~B: `external/dcl/paper/sections/induced_gauge_action.tex`
  (the $U(1)$ Wilson-action template that subproblem 3 generalises).
- Paper~II audit table: `paper/sections/audit_table.tex` (canonical
  PASS / STUB record for each sub-claim).

"""
tick_rule_cp_modified.py

Phase 1.5 / Route (b): test whether the bipartite tick rule can be
modified to admit Branch B SU(3) (3 (+) 3-bar -- the QCD colour vs
anti-colour identification) as a global symmetry, by adding an
explicit antilinear (CP-style) chirality-flipping component.

Structural setting.

The existing tick rule
    T_ext = T_chir (x) I_2 (x) I_3,    T_chir = is * I_2 + c * sigma_x
        (s = sin(d/2), c = cos(d/2))
is consistent with Branch A SU(3) (3 (+) 3, both sublattices in the
fundamental), as verified by tick_rule_extended_consistency.py and
su3_branch_consistency.py.  Phase 1.5 asks whether a modification
with an antilinear chirality-flipping component can make Branch B
SU(3) (RGB in 3, CMY in 3-bar) a global symmetry.

Modified-tick ansatz (natural form):

    T_ext^B = is * I_12  +  c * (sigma_x (x) I_2 (x) C) o K

  where K is global complex conjugation on C^12 and C is a 3x3 matrix
  on the colour factor.  Setting C = I_3 gives the simplest CP
  candidate -- chirality swap with colour conjugation; non-trivial C
  allows an additional unitary rotation on colour during the
  chirality flip.

Branch B SU(3) generators (chirality-dependent):

    T_a^B = P_R (x) I_2 (x) lambda_a/2  +  P_L (x) I_2 (x) (-conj(lambda_a)/2)

Commutator condition for the antilinear part:

  For a state psi, define Y = sigma_x (x) I_2 (x) C.  Then
    (Y o K)(T_a^B psi) = Y * conj(T_a^B psi) = Y * conj(T_a^B) * conj(psi)
    T_a^B * (Y o K)(psi) = T_a^B * Y * conj(psi)
  Equality for all psi ->  T_a^B * Y = Y * conj(T_a^B).

In chirality-block form (T_a^B block-diagonal, Y block-off-diagonal),
the (R, L) block of this equation reduces to

    lambda_a * C = -C * lambda_a    (anticommutation for every a)

What this script verifies.

  Step 1: Confirm the simplest candidate C = I_3 fails -- it requires
          lambda_a = -lambda_a, which holds for no Gell-Mann.

  Step 2: Enumerate a small set of plausible C's (diagonal involutions,
          transpositions, sign flips) and confirm each fails.

  Step 3: Show analytically -- and verify symbolically -- that no
          non-zero C satisfies anticommutation with every lambda_a.
          The argument: anticommutation with lambda_3 = diag(1, -1, 0)
          forces C_{ij} = 0 wherever lambda_3^{ii} + lambda_3^{jj} != 0,
          leaving only C_{12}, C_{21}, C_{33} possibly non-zero;
          subsequent anticommutation with lambda_8 = diag(1, 1, -2)/sqrt(3)
          forces those remaining entries to zero as well.

  Step 4: Confirm the result is robust to generalisations -- letting Y
          entangle the isospin factor (Y = sigma_x (x) Z (x) C for any
          Z on isospin) does not relax the colour constraint, because
          the isospin and colour factors are decoupled in the tensor
          product.

  Step 5: Connect to the Schur-level statement: the antilinear
          intertwiner from the fundamental 3 to the conjugate 3-bar of
          SU(3) is unique up to scalar -- it is global colour
          conjugation K_col itself.  Any natural tick-rule modification
          that uses an antilinear factor reduces to the colour
          anticommutation condition above, whose only solution is C = 0.

  Step 6: A=1 (unitarity in the antilinear sense): if a modification
          DID exist, would it preserve A=1?  Quick check on the
          candidate C = I_3.  Yes -- antilinear maps automatically
          preserve |psi|^2 when the linear part is unitary.  The
          obstruction is not unitarity; it is representation-theoretic.

Phase 1.5 outcome (predicted, confirmed by this script).

  NEGATIVE.  No modification of the natural form admits Branch B SU(3)
  as a global symmetry of the tick rule.  The structural reason: the
  SU(3) fundamental and conjugate representations are inequivalent,
  and the bipartite tick rule's natural extension does not contain
  the anticommutation structure required to bridge them.

  Implication for the framework.  The lattice cannot incorporate
  SM-style CP / colour-anti-colour distinction as a discrete symmetry
  of the existing structure.  The bipartite RGB/CMY parity is
  intrinsically a SPATIAL parity (linear, sigma_x on chirality) and
  CANNOT be promoted to a charge-parity by any natural tick
  modification.  Combined with the Route (a) result
  (chirality_parity_alignment.py): the framework predicts a
  vector-like, parity-conserving structure with the SM gauge group's
  Lie algebra -- it does NOT predict the SM's chiral coupling or CP
  violation.

  Either reading is publishable.  The framework's contribution: it
  identifies precisely which features of the SM are geometric
  (the Lie group structure of Eq.(137) holds) and which are NOT
  (chirality, CP -- external choices, not derivable from the lattice).
"""

import itertools
import sympy as sp
from sympy import (I, Matrix, eye, sqrt, simplify, conjugate, Rational, cos,
                   sin, symbols)


def gell_mann_matrices():
    L1 = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    L2 = Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]])
    L3 = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    L4 = Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
    L5 = Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]])
    L6 = Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    L7 = Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]])
    L8 = (1 / sqrt(3)) * Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])
    return [L1, L2, L3, L4, L5, L6, L7, L8]


def kron(*mats):
    r = mats[0]
    for M in mats[1:]:
        r = sp.kronecker_product(r, M)
    return r


def conj_matrix(M):
    return M.applyfunc(conjugate)


def is_zero(M):
    return all(simplify(e) == 0 for e in M)


def anticommutes_with_all(C, generators):
    """Test whether the linear matrix C satisfies C * G + G * C = 0
    for every G in `generators`.  Returns (verdict, failures) where
    failures lists the indices of generators where the condition fails."""
    failures = []
    for k, G in enumerate(generators):
        ac = simplify(C @ G + G @ C)
        if not is_zero(ac):
            failures.append(k + 1)
    return (not failures), failures


def candidate_colour_intertwiners():
    """Plausible 3x3 colour matrices C to test against the anticommutation
    condition.  None of these are predicted to pass -- the script confirms
    the structural impossibility."""
    return [
        ("C = I_3", eye(3)),
        ("C = -I_3", -eye(3)),
        ("C = diag(1, 1, -1)",
         Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])),
        ("C = diag(1, -1, -1)",
         Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])),
        ("C = diag(1, -1, 1)",
         Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 1]])),
        ("C = T_{12} (basis swap)",
         Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])),
        ("C = T_{13} (basis swap)",
         Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])),
        ("C = T_{23} (basis swap)",
         Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])),
        ("C = i*sigma_y-like (antisymmetric)",
         Matrix([[0, I, 0], [-I, 0, 0], [0, 0, 0]])),
    ]


def step1_simplest_candidate():
    """Test C = I_3 directly.  Expected to fail because lambda_a != -lambda_a."""
    print("-" * 70)
    print("Step 1: simplest candidate C = I_3")
    print("-" * 70)
    print()
    C = eye(3)
    L = gell_mann_matrices()
    ok, failures = anticommutes_with_all(C, L)
    print(f"  Does C = I_3 anticommute with every Gell-Mann?  {ok}")
    if not ok:
        print(f"  Failures: lambda_{{{', '.join(str(f) for f in failures)}}}")
        print("  Reason: {{lambda_a, I}} = 2 * lambda_a, which is non-zero for")
        print("  every Gell-Mann generator.  C = I_3 trivially fails.")
    print()


def step2_enumerate_candidates():
    """Loop through the candidate list and confirm each fails."""
    print("-" * 70)
    print("Step 2: enumerate plausible colour intertwiners C")
    print("-" * 70)
    print()
    L = gell_mann_matrices()
    print(f"  {'Candidate':<35s} | {'Anticommutes w/ all 8?':<25s} | Failures")
    print("-" * 70)
    survivors = []
    for name, C in candidate_colour_intertwiners():
        ok, failures = anticommutes_with_all(C, L)
        verdict = "yes" if ok else "NO"
        fail_str = "" if ok else f"lambda_{{{','.join(str(f) for f in failures)}}}"
        print(f"  {name:<35s} | {verdict:<25s} | {fail_str}")
        if ok:
            survivors.append((name, C))
    print()
    if not survivors:
        print("  No candidate satisfies the anticommutation condition.")
    print()
    return survivors


def step3_proof_no_solution():
    """Prove analytically (verified symbolically) that no non-zero C
    satisfies anticommutation with every Gell-Mann generator."""
    print("-" * 70)
    print("Step 3: structural proof that no non-zero C works")
    print("-" * 70)
    print()
    print("  For diagonal lambda, anticommutation {lambda, C} = 0 forces")
    print("    C_{ij} * (lambda_{ii} + lambda_{jj}) = 0  for all i, j.")
    print()
    print("  Apply to lambda_3 = diag(1, -1, 0):")
    print("    (i, j) | lambda_{ii} + lambda_{jj} | constraint")
    print("    (1,1)  |  +2                       | C_{11} = 0")
    print("    (1,2)  |   0                       | C_{12} unconstrained")
    print("    (1,3)  |  +1                       | C_{13} = 0")
    print("    (2,1)  |   0                       | C_{21} unconstrained")
    print("    (2,2)  |  -2                       | C_{22} = 0")
    print("    (2,3)  |  -1                       | C_{23} = 0")
    print("    (3,1)  |  +1                       | C_{31} = 0")
    print("    (3,2)  |  -1                       | C_{32} = 0")
    print("    (3,3)  |   0                       | C_{33} unconstrained")
    print()
    print("  Surviving after lambda_3:  C_{12}, C_{21}, C_{33}  possibly non-zero.")
    print()
    print("  Now apply lambda_8 = diag(1, 1, -2)/sqrt(3):")
    print("    For the surviving entries (i, j):")
    print("    (1,2)  |   2/sqrt(3)               | C_{12} = 0")
    print("    (2,1)  |   2/sqrt(3)               | C_{21} = 0")
    print("    (3,3)  |  -4/sqrt(3)               | C_{33} = 0")
    print()
    print("  Conclusion: every entry of C must be zero.  Symbolic check:")
    print()

    L = gell_mann_matrices()

    # Symbolic verification: search over diagonal C and a few off-diagonal
    # ansatzes consistent with the lambda_3 surviving entries
    c12, c21, c33 = symbols('c12 c21 c33', complex=True)
    C_general = Matrix([
        [0,    c12, 0],
        [c21,  0,   0],
        [0,    0,   c33],
    ])
    print("  General C consistent with lambda_3 anticommutation:")
    sp.pprint(C_general)
    print()

    print("  Apply lambda_8 anticommutation:")
    lam8 = L[7]
    ac8 = simplify(C_general @ lam8 + lam8 @ C_general)
    print("    {C, lambda_8} = ")
    sp.pprint(ac8)
    print()
    print("  Each non-zero entry gives an equation forcing c12 = c21 = c33 = 0.")
    print()


def step4_isospin_decoupling():
    """Show that allowing Y to entangle isospin doesn't relax the colour
    constraint."""
    print("-" * 70)
    print("Step 4: isospin entanglement does not relax the colour constraint")
    print("-" * 70)
    print()
    print("  Generalise the ansatz to Y = sigma_x (x) Z (x) C with Z any 2x2")
    print("  matrix on isospin.  In chirality-block form, (R, L) block of")
    print("  T_a^B * Y is")
    print("    (I_2 (x) lambda_a/2) * (Z (x) C) = Z (x) (lambda_a C / 2)")
    print("  and (R, L) block of Y * conj(T_a^B) is")
    print("    (Z (x) C) * (I_2 (x) -lambda_a/2) = Z (x) (-C lambda_a / 2).")
    print()
    print("  Setting equal: lambda_a C = -C lambda_a -- SAME colour constraint,")
    print("  independent of Z.  Isospin and colour decouple in the tensor")
    print("  product, so no isospin entanglement can rescue Branch B.")
    print()

    # Confirm symbolically with Z = sigma_y as a sample
    sx = Matrix([[0, 1], [1, 0]])
    sy = Matrix([[0, -I], [I, 0]])
    L = gell_mann_matrices()

    # Take Z = sigma_y, C = I_3 -- still must fail by the same algebra
    Z = sy
    C = eye(3)

    # Compute Y = sigma_x (x) Z (x) C and check the block equation
    Y = kron(sx, Z, C)

    # Construct T_a^B for a = 1 (real lambda_1, definitely problematic)
    P_R = Matrix([[1, 0], [0, 0]])
    P_L = Matrix([[0, 0], [0, 1]])
    lam1 = L[0]
    T_1_B = (kron(P_R, eye(2), Rational(1, 2) * lam1)
             + kron(P_L, eye(2), Rational(-1, 2) * conj_matrix(lam1)))

    # Test T_a^B Y - Y conj(T_a^B)
    lhs = T_1_B @ Y
    rhs = Y @ conj_matrix(T_1_B)
    residual = simplify(lhs - rhs)
    print(f"  Sample check (Z = sigma_y, C = I_3, a = 1): residual zero?  "
          f"{is_zero(residual)}")
    print()


def step5_schur_intertwiner():
    """Discuss the representation-theoretic origin of the obstruction."""
    print("-" * 70)
    print("Step 5: representation-theoretic origin of the obstruction")
    print("-" * 70)
    print()
    print("  The fundamental 3 and conjugate 3-bar of SU(3) are INEQUIVALENT")
    print("  irreducible representations.  By Schur's lemma applied to a")
    print("  candidate LINEAR intertwiner f: 3 -> 3-bar:")
    print()
    print("    rho(g) f = f * rho-bar(g)  for all g in SU(3)  =>  f = 0.")
    print()
    print("  The candidate ANTILINEAR intertwiner is f = C o K, where K is")
    print("  complex conjugation; Schur on (rho-bar)-bar = rho gives")
    print()
    print("    C must commute with every U_g in SU(3)  =>  C = alpha * I.")
    print()
    print("  So the unique (up to scalar) antilinear intertwiner is global")
    print("  colour conjugation K itself.")
    print()
    print("  The tick rule's chirality-flipping piece, when promoted to an")
    print("  antilinear operator (Y o K), DOES contain K -- but it must also")
    print("  commute with T_a^B, which (under chirality dependence) requires")
    print("  the additional anticommutation C lambda_a = -lambda_a C.  That")
    print("  is a STRONGER condition than Schur intertwining; it has only")
    print("  the trivial solution.")
    print()
    print("  The two conditions differ because Branch B's T_a^B uses")
    print("    +lambda_a/2 on R, -conj(lambda_a)/2 on L,")
    print("  not the same generator on both -- so commutativity with the")
    print("  chirality-flipping tick imposes a relation between lambda_a")
    print("  and conj(lambda_a) that goes beyond simple intertwining.  That")
    print("  relation has no solution within SU(3).")
    print()


def step6_unitarity_check():
    """Confirm that A=1 is not the obstruction -- if the modification existed,
    it would automatically preserve |psi|^2."""
    print("-" * 70)
    print("Step 6: A=1 is not the obstruction")
    print("-" * 70)
    print()
    print("  For an antilinear operator A = U o K with U unitary, |A psi|^2 =")
    print("    psi^dag conj(U^dag) U conj(psi) = |conj(psi)|^2 = |psi|^2.")
    print()
    print("  So A=1 is preserved automatically.  The obstruction is")
    print("  representation-theoretic, not unitarity-based.")
    print()


def report():
    print("=" * 70)
    print("Tick-rule modification for Branch B SU(3) compatibility")
    print("=" * 70)
    print()
    print("Ansatz:")
    print("    T_ext^B = is * I_12  +  c * (sigma_x (x) I_2 (x) C) o K,")
    print()
    print("with K global complex conjugation and C an unknown 3x3 colour")
    print("matrix to be determined by Branch B SU(3) commutativity.")
    print()
    print("Commutator condition (chirality-flipping piece):")
    print("    lambda_a C = -C lambda_a  for all a = 1, ..., 8.")
    print()

    step1_simplest_candidate()
    survivors = step2_enumerate_candidates()
    step3_proof_no_solution()
    step4_isospin_decoupling()
    step5_schur_intertwiner()
    step6_unitarity_check()

    # ── Final conclusion ───────────────────────────────────────────────
    print("=" * 70)
    print("Conclusion")
    print("=" * 70)
    print()
    if survivors:
        print(f"  Unexpected: {len(survivors)} candidate(s) passed the")
        print("  anticommutation test.  Inspect manually.")
        for name, _ in survivors:
            print(f"    -- {name}")
    else:
        print("  Zero candidates pass.  Branch B SU(3) cannot be made a global")
        print("  symmetry of the bipartite tick rule by any natural")
        print("  modification of the form X + (Y o K).  The obstruction is")
        print("  fundamental: the 3 and 3-bar representations of SU(3) are")
        print("  inequivalent, and the antilinear intertwiner that exists")
        print("  between them (global K on colour) is incompatible with the")
        print("  chirality-dependent SU(3) action that Branch B requires.")
    print()
    print("Phase 1.5 / Route (b) result class: NEGATIVE.")
    print()
    print("  The bipartite octahedral lattice's structure does not admit")
    print("  SM-style CP / colour-anti-colour distinction as a discrete")
    print("  symmetry of the tick rule.  Combined with Route (a):")
    print()
    print("    -- The lattice's bipartite parity is intrinsically LINEAR,")
    print("       a spatial parity sigma_x (x) I_2 (x) I_3 with no charge-")
    print("       conjugation component.")
    print("    -- The proposed SU(2)_W couples VECTOR-LIKE to matter, not")
    print("       chirally as in the SM.")
    print("    -- The framework's discrete Z_2 is orthogonal to the SM's")
    print("       chirality Z_2 on the chirality C^2.")
    print()
    print("  The framework realises a parity-conserving Lie group")
    print("  SO(3,1) x SU(3) x SU(2) x U(1) -- it identifies which parts of")
    print("  the SM are geometric (the Lie algebra structure of Eq.~(137)")
    print("  holds) and which are NOT (chirality, CP -- external choices,")
    print("  not derivable from the lattice).")


if __name__ == '__main__':
    report()

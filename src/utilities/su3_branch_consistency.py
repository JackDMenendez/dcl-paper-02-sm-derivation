"""
su3_branch_consistency.py

Phase 1 sub-task 0 (upstream of chirality_parity_alignment.py):
determine which SU(3) interpretation of the per-site colour C^3 is
consistent with the existing bipartite tick rule on C^12 verified by
tick_rule_extended_consistency.py.

Structural setting.

The audit-table PASS row "Direct-product structure on extended C^12"
(automorphism_direct_product_extended.py) uses SU(3) generators

    T_a^A = I_2 (x) I_2 (x) lambda_a / 2          (Branch A)

acting identically on the colour C^3 of every site, regardless of
which sublattice (RGB or CMY) the site is on.  This implicitly puts
BOTH sublattices in the fundamental representation 3 of SU(3).

An alternative interpretation -- forced by identifying RGB with 3 and
CMY with the conjugate 3-bar, as in QCD's distinction between colour
and anti-colour -- is

    T_a^B = P_R (x) I_2 (x)   lambda_a /2
          + P_L (x) I_2 (x) (-conj(lambda_a)/2)   (Branch B)

where P_R = diag(1, 0) and P_L = diag(0, 1) project the chirality
factor onto the RGB and CMY sublattices respectively.  Under Branch
B, the SU(3) action on the CMY sublattice IS the conjugate
representation 3-bar.

The question this script answers: do the Branch B generators commute
with the existing tick operator T_ext = T_chir (x) I_2 (x) I_3?

(Branch A trivially commutes -- already established in
tick_rule_extended_consistency.py.  Branch B is the open question.)

Analytic prediction.

Using the tensor commutator identity
    [X (x) I (x) I, Y (x) I (x) Z] = [X, Y] (x) I (x) Z,
the residual decomposes as

    [T_ext, T_a^B] = [T_chir, P_R] (x) I_2 (x) (lambda_a + conj(lambda_a))/2
                   = [T_chir, P_R] (x) I_2 (x)        Re(lambda_a),

where the first equality uses [T_chir, P_L] = -[T_chir, P_R] (since
P_R + P_L = I commutes with T_chir).  The residual vanishes iff
Re(lambda_a) = 0, i.e., iff lambda_a is purely imaginary.  Among the
eight Gell-Mann generators, only lambda_2, lambda_5, lambda_7 satisfy
this; the other five (lambda_1, lambda_3, lambda_4, lambda_6,
lambda_8) have real entries and obstruct.

What this establishes.

  Branch A (3 (+) 3, current scaffolding) IS a global symmetry of
  the existing bipartite tick rule.  Branch B (3 (+) 3-bar, the
  charge-conjugation framing) is NOT a global symmetry: 5 of 8
  generators fail to commute with T_ext.

Structural consequence for Phase 1.

  The bipartite parity, if defined as a symmetry of the existing
  tick rule, MUST be linear.  Antilinear (CP-like) candidates are
  inconsistent with the tick rule as written.

  If one wants to pursue the CP framing, the tick rule itself must
  be modified to include a 3 <-> 3-bar conjugation on chirality-
  flipping steps -- a substantive change that re-opens the
  audit-table PASS row "Tick-rule consistency on C^12".

What this does NOT establish.

  Whether the modified (partially antilinear) tick rule under Branch
  B preserves A=1 and the other audit invariants.  That is a
  separate calculation.

  Whether the lattice's deeper physics (continuum limit, gauge
  coupling, etc.) prefers Branch A or Branch B.  This script speaks
  only to internal consistency with the existing tick rule.
"""

import sympy as sp
from sympy import (I, Matrix, eye, sqrt, simplify, conjugate, Rational, cos,
                   sin, symbols)


def gell_mann_matrices():
    """The eight Gell-Mann matrices lambda_a on C^3.  Generators of
    su(3) under the normalisation T_a = lambda_a / 2.  Same conventions
    as automorphism_direct_product_extended.py."""
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
    """Tensor (Kronecker) product of matrices, left-to-right."""
    r = mats[0]
    for M in mats[1:]:
        r = sp.kronecker_product(r, M)
    return r


def conj_matrix(M):
    """Element-wise complex conjugate of a sympy matrix.  This IS the
    action of the antilinear charge-conjugation operator K on the
    matrix entries of an SU(3) generator -- mapping a generator of
    the fundamental 3 to a generator of the conjugate 3-bar (up to
    the sign convention -conj(lambda_a) used here)."""
    return M.applyfunc(conjugate)


def chirality_tick_operator(delta_phi):
    """The bipartite chirality tick operator on C^2 = (psi_R, psi_L),
    same as tick_rule_extended_consistency.py.  T_chir IS the local
    (no-spatial-hop) part of the bipartite tick rule on the existing
    framework's per-site amplitude."""
    c = cos(delta_phi / 2)
    s = sin(delta_phi / 2)
    return Matrix([[I * s, c],
                   [c, I * s]])


def commutator(A, B):
    return simplify(A @ B - B @ A)


def is_zero(M):
    return all(simplify(e) == 0 for e in M)


def branch_a_generators():
    """Branch A: SU(3) acts as lambda_a/2 on the colour C^3 of every
    site, regardless of sublattice.  Both RGB and CMY in the
    fundamental 3.  Matches the colour_generators() of
    automorphism_direct_product_extended.py."""
    L = gell_mann_matrices()
    return [kron(eye(2), eye(2), Rational(1, 2) * La) for La in L]


def branch_b_generators():
    """Branch B: SU(3) acts as lambda_a/2 on RGB sites (P_R subspace)
    and as -conj(lambda_a)/2 on CMY sites (P_L subspace).  RGB carries
    3, CMY carries 3-bar.  The sign + conjugation IS the standard
    relation between a Lie-algebra generator and its conjugate-
    representation generator (for su(N), the conjugate of T = lambda/2
    is -conj(T) = -conj(lambda)/2, satisfying the same structure
    constants because f_{abc} is real)."""
    L = gell_mann_matrices()
    P_R = Matrix([[1, 0], [0, 0]])
    P_L = Matrix([[0, 0], [0, 1]])
    return [
        kron(P_R, eye(2), Rational(1, 2) * La)
        + kron(P_L, eye(2), Rational(-1, 2) * conj_matrix(La))
        for La in L
    ]


def report():
    print("=" * 70)
    print("SU(3) branch consistency on the bipartite tick rule")
    print("=" * 70)
    print()
    print("Two candidate SU(3) actions on the extended C^12 amplitude:")
    print()
    print("  Branch A: T_a^A = I_2 (x) I_2 (x) lambda_a/2")
    print("    (both sublattices in the fundamental 3 of SU(3))")
    print()
    print("  Branch B: T_a^B = P_R (x) I_2 (x)   lambda_a/2")
    print("                  + P_L (x) I_2 (x) (-conj(lambda_a)/2)")
    print("    (RGB in 3, CMY in 3-bar; chirality-dependent SU(3))")
    print()

    dphi = symbols('delta_phi', real=True)
    T_chir = chirality_tick_operator(dphi)
    T_ext = kron(T_chir, eye(2), eye(3))

    Ta = branch_a_generators()
    Tb = branch_b_generators()

    # ── Step 1: within-factor su(3) algebra closes for both branches ────
    print("-" * 70)
    print("Step 1: within-factor su(3) closure (sample [T_1, T_2] = i T_3)")
    print("-" * 70)
    print()

    print("  Branch A:")
    c_a = commutator(Ta[0], Ta[1])
    matches_a = is_zero(simplify(c_a - I * Ta[2]))
    print(f"    [T_1^A, T_2^A] = i T_3^A?  {matches_a}")

    print("  Branch B:")
    c_b = commutator(Tb[0], Tb[1])
    matches_b = is_zero(simplify(c_b - I * Tb[2]))
    print(f"    [T_1^B, T_2^B] = i T_3^B?  {matches_b}")
    print()
    print("  Both branches close to su(3).  Branch A trivially (by the")
    print("  tensor structure); Branch B because the conjugate-rep")
    print("  generators -conj(lambda_a)/2 inherit the same real structure")
    print("  constants f_{abc} as the fundamental, and the block structure")
    print("  P_R (+) P_L is preserved by the commutator P_R P_L = 0.")
    print()

    # ── Step 2: commutativity with T_ext ────────────────────────────────
    print("-" * 70)
    print("Step 2: commutativity with the bipartite tick rule T_ext")
    print("-" * 70)
    print()

    print("  Branch A: [T_ext, T_a^A] = 0 for all a?")
    branch_a_ok = True
    for a in range(8):
        if not is_zero(commutator(T_ext, Ta[a])):
            branch_a_ok = False
            print(f"    a = {a + 1}: NOT zero")
    if branch_a_ok:
        print(f"    All 8 commutators vanish.  Branch A IS a global")
        print(f"    symmetry of the tick rule (already PASS in")
        print(f"    tick_rule_extended_consistency.py).")
    print()

    print("  Branch B: [T_ext, T_a^B] = 0 for all a?")
    branch_b_fail = []
    branch_b_pass = []
    for a in range(8):
        if is_zero(commutator(T_ext, Tb[a])):
            branch_b_pass.append(a + 1)
        else:
            branch_b_fail.append(a + 1)
    print(f"    Commute:    {branch_b_pass}")
    print(f"    Obstruct:   {branch_b_fail}")
    if branch_b_fail:
        print(f"    Branch B IS NOT a global symmetry of the tick rule.")
    print()

    # ── Step 3: structural residual decomposition ───────────────────────
    print("-" * 70)
    print("Step 3: structural residual for Branch B")
    print("-" * 70)
    print()
    print("  Using [X (x) I (x) I, Y (x) I (x) Z] = [X, Y] (x) I (x) Z and")
    print("  [T_chir, P_L] = -[T_chir, P_R] (since P_R + P_L = I commutes")
    print("  with T_chir), the residual factors as")
    print()
    print("    [T_ext, T_a^B] = [T_chir, P_R] (x) I_2 (x) (lambda_a + conj(lambda_a))/2")
    print("                   = [T_chir, P_R] (x) I_2 (x)        Re(lambda_a)")
    print()

    P_R = Matrix([[1, 0], [0, 0]])
    chir_resid = simplify(T_chir @ P_R - P_R @ T_chir)
    print("  [T_chir, P_R] =")
    sp.pprint(chir_resid)
    print()
    print("  (Off-diagonal, proportional to the kinetic hop cos(delta_phi/2);")
    print("  non-zero whenever the tick has a non-trivial chirality-mixing")
    print("  component, i.e., everywhere except the trivial limit cos = 0.)")
    print()

    print("  Per-generator real part Re(lambda_a) = (lambda_a + conj(lambda_a))/2:")
    L = gell_mann_matrices()
    for a, La in enumerate(L):
        real_part = simplify(La + conj_matrix(La)) / 2
        zero = is_zero(real_part)
        marker = "imaginary -> commutes  " if zero else "real      -> obstructs"
        print(f"    lambda_{a + 1}:  {marker}")
    print()
    print("  Five of the eight Gell-Manns have non-zero real parts.  Those")
    print("  five Branch-B generators do not commute with T_ext, so SU(3)")
    print("  is not a global symmetry on Branch B for any cos(delta_phi/2)")
    print("  != 0 (i.e., for any non-trivial chirality-mixing tick).")
    print()

    # ── Step 4: structural conclusion ───────────────────────────────────
    print("-" * 70)
    print("Step 4: structural conclusion")
    print("-" * 70)
    print()
    print("  The bipartite tick rule T_ext = T_chir (x) I_2 (x) I_3, as")
    print("  verified PASS in tick_rule_extended_consistency.py, is")
    print("  consistent with Branch A (3 (+) 3) only.  Branch B (3 (+) 3-bar)")
    print("  fails commutation for 5 of 8 SU(3) generators.")
    print()
    print("  Equivalent statement: ANY bipartite parity operator P that")
    print("  acts as a SYMMETRY of the existing tick rule must commute with")
    print("  Branch A SU(3).  In particular, the antilinear (CP-like)")
    print("  candidate P_CP = (sigma_x (x) I_2 (x) C) o K, which would")
    print("  implement the 3 <-> 3-bar exchange, is not compatible with the")
    print("  existing tick rule -- it can only be made consistent by")
    print("  modifying the tick rule itself to include the 3 <-> 3-bar")
    print("  conjugation on chirality-flipping steps.")
    print()
    print("Routing for Phase 1.")
    print()
    print("  Route (a) -- linear bipartite parity, Branch A SU(3):")
    print("    Proceed with the existing tick rule.  Candidate P operators")
    print("    are linear: P = sigma_x (x) I_2 (x) M for M in the symmetric")
    print("    elements of SU(3) (or SU(3) sign-flips).  The chirality-")
    print("    alignment test against gamma_5 has a structurally predictable")
    print("    outcome (sigma_x and sigma_z anticommute), which routes the")
    print("    paper toward 'precise obstruction' or 'characterisation'")
    print("    rather than 'derivation'.  This is the conservative path:")
    print("    no audit rows reopen, Phase 1 proceeds.")
    print()
    print("  Route (b) -- antilinear (CP) bipartite parity, modified tick rule:")
    print("    Define a Branch-B-compatible tick rule that includes an")
    print("    explicit colour-conjugation on chirality-flipping ticks.")
    print("    Verify A=1 preservation and re-establish the existing audit")
    print("    PASS rows on the modified rule before running the alignment")
    print("    test.  High-payoff path: if successful, the framework has a")
    print("    built-in discrete CP, and the chirality-alignment test")
    print("    becomes meaningful in the SM-CP sense.  Higher risk: a PASS")
    print("    row may have to move to PART or STUB temporarily.")
    print()


if __name__ == '__main__':
    report()

"""
chirality_parity_alignment.py

Phase 1 main result (Route a): test the structural relationship
between the lattice's bipartite RGB/CMY parity P and the Standard
Model's chirality structure on the extended C^12 amplitude, under
the linear-P, Branch-A SU(3) regime established by
su3_branch_consistency.py (PASS).

Carrier:  psi in C^2 (chir) (x) C^2 (iso) (x) C^3 (col) = C^12.

Reference operators:

  Tick rule:           T_ext   = T_chir (x) I_2 (x) I_3
                       T_chir  = [[i sin(d/2), cos(d/2)],
                                  [cos(d/2),   i sin(d/2)]]

  SM chirality:        gamma_5 = sigma_z (x) I_2 (x) I_3
                       P_L     = (I - gamma_5) / 2  (projects onto psi_L)
                       P_R     = (I + gamma_5) / 2  (projects onto psi_R)

  SU(2)_W generators:  T_a^W   = I_2 (x) sigma_a/2 (x) I_3  (a = 1, 2, 3)

  SU(3) generators (Branch A):
                       T_a^c   = I_2 (x) I_2 (x) lambda_a/2  (a = 1, ..., 8)

Candidate bipartite-parity operators (linear, by sub-task 0):

  P_M = sigma_x (x) I_2 (x) M

  with M a Hermitian unitary 3x3 matrix (M^2 = I_3, so P_M^2 = I_12).
  The candidates explored:

    M = I_3                                            (canonical; trivial colour)
    M = diag(1, 1, -1)                                 (singles out colour 3)
    M = diag(1, -1, -1)                                (singles out colour 1)
    M = -I_3                                           (overall colour sign flip)
    M = T_{ij}                                         (basis transposition)

  Only M in {+I_3, -I_3} commutes with all eight Gell-Mann generators
  (by Schur's lemma on the irreducible 3); these are also projectively
  equivalent.  The non-trivial M's fail Test 4 (global SU(3) symmetry)
  and so are not bipartite-parity candidates under Branch A.

Test suite, applied to each candidate:

  T1.  Involution:           P^2  = I_12 ?
  T2.  Unitarity:            P^dag P = I_12 ?
  T3.  Tick-rule symmetry:   [P, T_ext] = 0 ?
  T4.  Global SU(3):         [P, T_a^c] = 0  for all a ?
  T5.  Global SU(2)_W:       [P, T_a^W] = 0  for all a ?
  T6.  Chirality involution: P gamma_5 P^{-1} = -gamma_5 ?   (anticommutation)
  T7.  L/R swap:             P P_L P^{-1} = P_R ?
  T8.  Vector-like SU(2)_W:  P T_a^W P^{-1} = T_a^W ?         (no CP-style conjugation)

Outcome classification:

  Aligned         (T6 returns +1, eigenbases coincide).
  Anti-aligned    (T6 returns -1, T7 swaps L<->R).
  Characterisation (T6 returns -1 but T8 commutes -- bipartite parity
                   and SM chirality are *orthogonal Bloch involutions*
                   on the chirality C^2; the lattice's Z_2 and the
                   SM's Z_2 are distinct, both linear, both involutions
                   on the same carrier).

Predicted outcome (analytic, confirmed by this script):
  CHARACTERISATION.  The lattice's bipartite parity is spatial parity
  (chirality swap), but the lattice's chirality basis -- in which
  RGB/CMY are sigma_x eigenstates -- is rotated by 90 degrees on the
  Bloch sphere relative to the SM's chirality basis (in which L/R
  are sigma_z eigenstates).  The two involutions anticommute, so
  the two Z_2's are maximally orthogonal.  Bipartite parity commutes
  with the SU(2)_W generators (vector-like, NOT the SM's CP signature),
  but exchanges the SM's L and R subspaces in the chirality C^2.

  The Phase 1 finding: under Branch A and the existing tick rule, the
  lattice predicts a specific structural relationship between its
  bipartite Z_2 and the SM's chirality Z_2 -- they are orthogonal,
  not aligned and not equal.  The SM's chirality is a SEPARATE
  Z_2 from the lattice's bipartition, not derivable from it; the
  lattice's bipartition is spatial parity, not chirality projection.

  This routes the paper toward "characterisation" rather than
  "derivation" or "obstruction."  The characterisation IS the
  result.
"""

import sympy as sp
from sympy import (I, Matrix, eye, sqrt, simplify, Rational, cos, sin,
                   symbols)


def pauli_matrices():
    sx = Matrix([[0, 1], [1, 0]])
    sy = Matrix([[0, -I], [I, 0]])
    sz = Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def gell_mann_matrices():
    """Eight Gell-Mann matrices on C^3 -- same conventions as
    automorphism_direct_product_extended.py and
    su3_branch_consistency.py."""
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


def chirality_tick_operator(delta_phi):
    c = cos(delta_phi / 2)
    s = sin(delta_phi / 2)
    return Matrix([[I * s, c], [c, I * s]])


def commutator(A, B):
    return simplify(A @ B - B @ A)


def is_zero(M):
    return all(simplify(e) == 0 for e in M)


def equals(A, B):
    return is_zero(simplify(A - B))


def candidate_parities():
    """Linear bipartite parity candidates P = sigma_x (x) I_2 (x) M
    with M^2 = I_3 and M Hermitian unitary on C^3."""
    sx = Matrix([[0, 1], [1, 0]])
    candidates = []

    # M = I_3 (canonical)
    M1 = eye(3)
    candidates.append(("M = I_3", M1, kron(sx, eye(2), M1)))

    # M = diag(1, 1, -1)
    M2 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
    candidates.append(("M = diag(1, 1, -1)", M2, kron(sx, eye(2), M2)))

    # M = diag(1, -1, -1)
    M3 = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
    candidates.append(("M = diag(1, -1, -1)", M3, kron(sx, eye(2), M3)))

    # M = -I_3 (overall sign flip)
    M4 = -eye(3)
    candidates.append(("M = -I_3", M4, kron(sx, eye(2), M4)))

    # M = T_{12} (basis transposition)
    M5 = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    candidates.append(("M = T_{12}", M5, kron(sx, eye(2), M5)))

    return candidates


def run_tests(name, M, P):
    """Run the T1..T8 test suite on candidate P. Returns a dict of
    boolean results plus the action-of-P on gamma_5, P_L, T^W."""
    sx, sy, sz = pauli_matrices()
    L = gell_mann_matrices()
    dphi = symbols('delta_phi', real=True)

    T_ext = kron(chirality_tick_operator(dphi), eye(2), eye(3))
    gamma5 = kron(sz, eye(2), eye(3))
    P_L = (eye(12) - gamma5) / 2
    P_R = (eye(12) + gamma5) / 2
    T_W = [kron(eye(2), sx / 2, eye(3)),
           kron(eye(2), sy / 2, eye(3)),
           kron(eye(2), sz / 2, eye(3))]
    T_c = [kron(eye(2), eye(2), La / 2) for La in L]

    P_inv = P.H  # P is unitary, so P^{-1} = P^dagger

    results = {}

    # T1: involution
    results['T1_involution'] = equals(P @ P, eye(12))
    # T2: unitarity
    results['T2_unitary'] = equals(P_inv @ P, eye(12))
    # T3: tick-rule symmetry
    results['T3_tick'] = is_zero(commutator(P, T_ext))
    # T4: global SU(3) symmetry  (all 8 generators)
    results['T4_su3'] = all(is_zero(commutator(P, Tc)) for Tc in T_c)
    # T5: global SU(2)_W symmetry
    results['T5_su2W'] = all(is_zero(commutator(P, Tw)) for Tw in T_W)
    # T6: chirality involution -- P gamma_5 P^{-1} = -gamma_5 ?
    P_gamma5_Pinv = simplify(P @ gamma5 @ P_inv)
    results['T6_anticommutes_g5'] = equals(P_gamma5_Pinv, -gamma5)
    results['T6_commutes_g5'] = equals(P_gamma5_Pinv, gamma5)
    # T7: maps P_L to P_R ?
    P_PL_Pinv = simplify(P @ P_L @ P_inv)
    results['T7_swaps_LR'] = equals(P_PL_Pinv, P_R)
    # T8: vector-like SU(2)_W -- P T^W P^{-1} = T^W ?
    results['T8_TW_invariant'] = all(
        equals(P @ Tw @ P_inv, Tw) for Tw in T_W
    )

    return results


def classify(results):
    """Map the test results to an outcome class."""
    if not (results['T1_involution'] and results['T2_unitary']
            and results['T3_tick'] and results['T4_su3']
            and results['T5_su2W']):
        return "INELIGIBLE (fails involution / unitarity / global-symmetry)"
    if results['T6_commutes_g5']:
        return "ALIGNED (P commutes with gamma_5 -- same Z_2 as SM chirality)"
    if results['T6_anticommutes_g5'] and results['T7_swaps_LR']:
        if results['T8_TW_invariant']:
            return ("CHARACTERISATION (P anticommutes with gamma_5, swaps L<->R, "
                    "commutes with SU(2)_W -- spatial parity, orthogonal Bloch "
                    "axis to chirality; lattice's Z_2 != SM's Z_2)")
        else:
            return ("ANTI-ALIGNED (P anticommutes with gamma_5, swaps L<->R, "
                    "but acts on SU(2)_W non-trivially)")
    return "UNCLASSIFIED -- inspect results manually"


def report():
    print("=" * 70)
    print("Chirality-parity alignment (Route a: linear P, Branch A SU(3))")
    print("=" * 70)
    print()

    candidates = candidate_parities()

    summary = []
    for name, M, P in candidates:
        print("-" * 70)
        print(f"Candidate: P_M = sigma_x (x) I_2 (x) M   with   {name}")
        print("-" * 70)
        results = run_tests(name, M, P)
        for key, val in results.items():
            print(f"  {key:30s}: {val}")
        outcome = classify(results)
        print(f"  Outcome: {outcome}")
        print()
        summary.append((name, outcome, results))

    # ── Final summary ──────────────────────────────────────────────────
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print()
    print(f"{'Candidate':<28s} | {'T4 SU(3)?':<10s} | Outcome")
    print("-" * 70)
    for name, outcome, results in summary:
        t4 = "yes" if results['T4_su3'] else "NO"
        # Compress outcome to the leading word for the table
        short = outcome.split(' (')[0] if '(' in outcome else outcome
        print(f"{name:<28s} | {t4:<10s} | {short}")
    print()

    # ── Structural conclusion ──────────────────────────────────────────
    print("-" * 70)
    print("Structural conclusion")
    print("-" * 70)
    print()
    print("  By Schur's lemma on the irreducible 3 of SU(3), only M = +/- I_3")
    print("  commutes with all eight Gell-Mann generators -- so only M = +/- I_3")
    print("  yields a P that is a global symmetry of Branch A SU(3).  The two")
    print("  surviving candidates are projectively equivalent (M = -I_3 is")
    print("  M = I_3 times an overall phase e^{i*pi} on colour, which acts as")
    print("  the identity on every physical observable on the colour C^3).")
    print()
    print("  Under the unique surviving candidate P = sigma_x (x) I_2 (x) I_3:")
    print()
    print("    (i)   P is the bipartite RGB/CMY parity verified PASS in")
    print("          tick_rule_extended_consistency.py.")
    print()
    print("    (ii)  P anticommutes with gamma_5 = sigma_z (x) I_2 (x) I_3,")
    print("          so the lattice's bipartite Z_2 and the SM's chirality Z_2")
    print("          are DIFFERENT involutions on the chirality C^2 -- they")
    print("          generate orthogonal Bloch axes (sigma_x vs sigma_z).")
    print()
    print("    (iii) P swaps the SM's left and right subspaces (P P_L P^{-1}")
    print("          = P_R).  This IS spatial parity in the SM sense, not")
    print("          chirality projection.")
    print()
    print("    (iv)  P commutes with every SU(2)_W generator (P T_a^W P^{-1}")
    print("          = T_a^W).  SU(2)_W is therefore vector-like under")
    print("          bipartite parity -- the lattice does NOT have the SM's")
    print("          CP signature (which would conjugate T_a^W).")
    print()
    print("  Phase 1 outcome class: CHARACTERISATION.")
    print()
    print("  The lattice's bipartite RGB/CMY parity is precisely *spatial")
    print("  parity*, not the SM's chirality projector.  The SM's chirality")
    print("  Z_2 is a SEPARATE structure on the same chirality C^2 carrier,")
    print("  rotated by 90 degrees on the Bloch sphere relative to the")
    print("  bipartite Z_2.  Eq.~(137) of Paper I, taken with Branch A SU(3)")
    print("  and the existing tick rule, predicts this orthogonal-Z_2")
    print("  relationship as a structural feature of the framework, not as")
    print("  an obstruction or an alignment.")
    print()
    print("  Routes for the paper:")
    print("    -- Headline: 'characterisation' framing.  The framework")
    print("       predicts a specific relationship between bipartite parity")
    print("       and SM chirality.  This is the publishable Phase 1 result.")
    print("    -- Optional follow-up (Phase 1.5, Route b): modify the tick")
    print("       rule to admit antilinear CP candidates and test whether")
    print("       P_L can be extracted from a locked CP operator.  Higher")
    print("       payoff, larger structural change.")


if __name__ == '__main__':
    report()

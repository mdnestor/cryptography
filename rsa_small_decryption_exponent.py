from fractions import Fraction
from continued_fractions import compute_cf, convergents

def small_decryption_exponent_attack(n: int, e: int, verbose=False):
    A = compute_cf(Fraction(e, n))
    for c in convergents(A):
        k, d = c.numerator, c.denominator
        if k > 0 and d < 1/3 * n**0.25:
            if verbose: print(f"checking k / d = {k} / {d}")
            phi = (e*d - 1)/k
            b = phi - n - 1
            d = (b**2 - 4*n)**0.5
            p = (-b - d)/2
            q = (-b + d)/2
            if verbose: print(f"phi = {phi}\np = {p}\nq = {q}")
            if p.is_integer() and q.is_integer():
                if verbose: print("both integers, solution found!")
                return int(p), int(q)

if __name__ == "__main__":
    n = 10383648113
    e = 9061915015
    p, q = small_decryption_exponent_attack(n, e, verbose=True)
    print(p, q)

import math
from fractions import Fraction
from typing import *

# polymorphic in x
def compute_cf(x, n=math.inf) -> List[int]:
    a = math.floor(x)
    x -= a
    if x == 0 or n == 0:
        return [a]
    return [a] + compute_cf(1/x, n - 1)

def evaluate_cf(A: List[int]) -> Fraction:
    if not A:
        raise ValueError(A)
    if len(A) == 1:
        return Fraction(A[-1])
    return A[0] + 1 / evaluate_cf(A[1:])

def convergents(A: List[int]) -> List[Fraction]:
    return [evaluate_cf(A[:i]) for i in range(1, len(A))]

if __name__ == "__main__":
    A = compute_cf(math.e, 8)
    print(A)
    for c in convergents(A):
        print("{:.4f}".format(float(c)), c)

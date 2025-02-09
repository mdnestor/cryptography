from typing import *

# first attempt: given a list of integers, compute the extended fraction
def compute_continued_fraction(a: List[int]) -> float:
    x = 0
    for ai in a[::-1]:
        x = 1/(ai + x)
    return 1 / x

# this only works so well, the next step is to work with rational number data type
# aka representing as pairs of ints

Rational = Tuple[int, int]

def tofrac(x: int) -> Rational:
    return (x, 1)

def floor(x: Rational) -> Rational:
    return (x[0] // x[1], 1)

def add(x: Rational, y: Rational) -> Rational:
    return (x[0]*y[1] + y[0]*x[1], x[1]*y[1])

def neg(x: Rational) -> Rational:
    return (-x[0], x[1])

def inv(x: Rational) -> Rational:
    return (x[1], x[0])

def compute_rational_continued_fraction(a):
    x = tofrac(0)
    for ai in a[::-1]:
        x = inv(add(tofrac(ai), x))
    return inv(x)

def compute_rational_convergents(x):
    aseq = []
    while True:
        a = floor(x)
        aseq.append(a[0])
        x = add(x, neg(a))
        if x[0] == 0:
            return aseq
        x = inv(x)

# testing
print(compute_continued_fraction([3,7]))
print(compute_rational_continued_fraction([3,7]))
print(compute_rational_convergents((22, 7)))

# testing out attack
e = 9061915015
n = 10383648113
convergents = compute_rational_convergents((e, n))
print(convergents)

for i in range(len(convergents)):
    L = convergents[:i]
    k, d = compute_rational_continued_fraction(L)
    if d < 1/3 * n**0.25:
        print(f"Testing convergent k / d = {k} / {d}")
        if k > 0:
            phi = (e*d-1)/k
            b = phi - n - 1
            p = (-b - (b**2 - 4*n)**0.5)/2
            q = (-b + (b**2 - 4*n)**0.5)/2
            print(f"Calculated phi = {phi}")
            print(f"Found p, q = {p}, {q}")

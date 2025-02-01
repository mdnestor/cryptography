import random

def is_prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, n))

def generate(g, p):
    n = 0
    xs = [g % p]
    while xs[-1] != 1:
        x = xs[-1]
        x = (x * g) % p
        xs.append(x)
    return xs

def is_generator(g, p):
    return not (g % p == 0) and len(generate(g, p)) == p - 1

def mod_exp(g, a, p):
    x = 1
    for i in range(a):
        x = (x * g) % p
    return x

def discrete_log(x, g, p):
    assert(is_generator(g, p))
    for a in range(p):
        if mod_exp(g, a, p) == x:
            return a

def generate_large_prime(a, b):
    while True:
        n = random.randint(a, b)
        if is_prime(n):
            return n

def generate_generator(p):
    while True:
        g = random.randint(0, p)
        if is_generator(g, p):
            return g

if __name__ == "__main__":
    p = generate_large_prime(10**6, 10**7)
    print("Large prime:", p)
    g = generate_generator(p)
    print("Generator:", g)
    
    # Alice chooses a secret message
    a = random.randint(0, p - 1)
    print("Alice's secret:", a)
    # Alice computes
    A = mod_exp(g, a, p)
    print("Alice's public message:", A)
    
    # Bob chooses a secret
    b = random.randint(0, p - 1)
    print("Bob's secret:", b)
    B = mod_exp(g, b, p)
    print("Bob's public message:", B)
    
    print("Alice's shared secret:", mod_exp(B, a, p))
    print("Bob's shared secret:", mod_exp(A, b, p))

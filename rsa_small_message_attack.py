
n = 1697429
e = 1653175
c = 1486810

b = 6
f = 5

# need modexp

def modinv(x, n):
     for y in range(n):
          if x*y % n == 1:
               return y
          
def fast_exponentiation(k, x, q):
    # make sure all variables are non-negative
    if x < 0:
         return fast_exponentiation(modinv(k, q), -x, q)
    assert (k >= 0 and x >= 0 and q >=1)
    result = 1 # define a counter 
    while x:
        if x % 2 == 1:
                result = (result * k) % q
        k = (k ^ 2) % q
        x >>= 1 # bit shift operator, dividing x by 2 ** y thus x >> 2 ** 1 = x / 2 
    return result

L1 = [(c*fast_exponentiation(i,-e,n))%n for i in range(1, 2**f+1)]
L2 = [fast_exponentiation(i,e,n) for i in range(1, 2**f+1)]

for m in range(2**6):
     if fast_exponentiation(m, e, n) == c:
          print(m)

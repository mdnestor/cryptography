import numpy
import math
import numpy as np
from numpy import matrix
from numpy import linalg

def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=matrix(A)
  adj=numpy.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=numpy.array(A)
  minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor
  
  
# make random matrix with det gcd = 1?

import math


# LOOP until valid key matrix is found
found = False
while not found:
    A = np.random.randint(low=0, high=25, size=(5,5))
    #print(A)
    # check gcd?
    d = np.linalg.det(A)
    d = int(d)

    # assert(math.gcd(d, 26) == 1)
    if math.gcd(d, 26) == 1:
        found = True

# encrypt a message?

m = "ANERROROCCUREDSEEOUTPUTFORDETA"

print("original message:", m)

blocks = [m[(5*i):(5*(i+1))] for i in range(5)]
print("blocked message:", blocks)

# encode m into list of ints
def encode(x):
    return np.array([ord(i) - ord('A') for i in x])

encoded_blocks = [encode(b) for b in blocks]
print("encoded blocks:", encoded_blocks)

encrypted_blocks = [(block @ A) % 26 for block in encoded_blocks]

print("encrypted blocks:", encrypted_blocks)

M = np.array(encrypted_blocks)

print(M)










  
  
  
  

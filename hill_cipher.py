
"""

This file implements the Hill cipher algorithm and also implements a known-plaintext attack.

This is a block cipher based on modular arithmetic, so we will need to implement the modular inverse algorithm.

"""

import math
import numpy as np
from typing import *

# helper functions that convert strings to lists of integers and vice versa

def encode(x: str) -> List[int]:
  return np.array([ord(ch) - ord('A') for ch in x])

def decode(x: List[int]) -> str:
  return "".join([chr(i + ord('A')) for i in x])

# Linear algebra utilities

def modular_determinant(A: np.ndarray, n: int) -> int:
  return int(round(np.linalg.det(A))) % n

def modular_invertible(A: np.ndarray, n: int) -> bool:
  d = modular_determinant(A, n)
  return math.gcd(d, n) == 1

def generate_modular_invertible_matrix(l: int, n: int) -> np.ndarray:
  A = np.zeros((l, l))
  while not modular_invertible(A, n):
    A = np.random.randint(0, n, size=(l, l))
  return A

def minor(A: np.ndarray, i: int, j: int) -> np.ndarray:
    A = np.delete(A, i, axis=0)
    A = np.delete(A, j, axis=1)
    return A

def modular_inverse(a: int, n: int) -> int:
  for i in range(n):
    if (i*a) % n == 1:
      return i

# https://en.wikipedia.org/wiki/Adjugate_matrix
def modular_adjugate(A: np.ndarray, n: int) -> np.ndarray:
  C = np.zeros(shape=A.shape)
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      M = modular_determinant(minor(A, i, j), n)
      C[i][j] = (-1)**(i + j) * M
  return C.T.astype(int) % n

def modular_matrix_inverse(A: np.ndarray, n: int) -> np.ndarray:
  B = modular_adjugate(A, n)
  d = modular_determinant(A, n)
  d_inv = modular_inverse(d, n)
  return (d_inv * B) % n

class HillCipher():
  def __init__(self, block_size: int, alphabet_size: int = 26):
    n = alphabet_size
    l = block_size
    self.alphabet_size = n
    self.block_size = l
    self.__key__ = generate_modular_invertible_matrix(l, n)
    self.__keyinv__ = modular_matrix_inverse(self.__key__, n)

  def encrypt_block(self, x: str) -> str:
    assert(len(x) == self.block_size)
    x = encode(x)
    y = np.matmul(self.__key__, x) % self.alphabet_size
    return decode(y)

  def decrypt_block(self, x: str) -> str:
    assert(len(x) == self.block_size)
    x = encode(x)
    y = np.matmul(self.__keyinv__, x) % self.alphabet_size
    return decode(y)

  def encrypt(self, x: str) -> str:
    l = self.block_size
    assert(len(x) % l == 0)
    blocks = [x[(i*l):((i+1)*l)] for i in range(len(x)//l)]
    return "".join(self.encrypt_block(b) for b in blocks)

  def decrypt(self, x: str) -> str:
    l = self.block_size
    assert(len(x) % l == 0)
    blocks = [x[(i*l):((i+1)*l)] for i in range(len(x)//l)]
    return "".join(self.decrypt_block(b) for b in blocks)

def crack_hill_cipher(m: str, c: str, l: int):
  assert(len(m) == len(c))
  assert(len(m) == l**2)
  m = encode(m)
  c = encode(c)

  M = m.reshape((l, l))
  C = c.reshape((l, l))

  if not modular_invertible(M, 26):
    raise ValueError()

  Minv = modular_matrix_inverse(M, 26)
  K = (Minv @ C).T % 26
  return K

if __name__ == "__main__":

  l = 5
  cipher = HillCipher(block_size = l)
  
  x = "NEVERGONNAGIVEYOUUPNEVERGONNALETYOUDOWNNEVERGONNARUNAROUNDANDHURTYOUNEVERGONNATELLALIENEVERGONNSAYGOODBYE"
  
  m = x[0:25]
  c = cipher.encrypt(m)
  
  print("known plaintext", m)
  print("known ciphertext", c)
  K = crack_hill_cipher(m, c, l)
  
  print("recovered key")
  print(K)
  print("true key")
  print(cipher.__key__)
  print("keys equal?", np.all(K == cipher.__key__))

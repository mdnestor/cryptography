from typing import *
import math

# I will assume all plaintext messages consist of capital letters only

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# first utility "encode" will take a string and return a list of ints
def encode(x: str) -> List[int]:
    return [ord(char) - ord('A') for char in x]

def decode(x: List[int]) -> str:
    return "".join(chr(i + ord('A')) for i in x)

# the ceaser shift
def ROT(x: str, k: int) -> str:
    x = encode(x)
    x = [(i + k) % len(ALPHABET) for i in x]
    x = decode(x)
    return x

# the affine shift
def Affine(x: str, k: Tuple[int, int]) -> str:
    assert(math.gcd(k[0], len(ALPHABET)) == 1)
    x = encode(x)
    x = [(k[0] * i + k[1]) % len(ALPHABET) for i in x]
    x = decode(x)
    return x

# a general class for a permutation cipher
class PermutationCipher():
    def __init__(self, key: str):
        # assert the key is a valid permutation
        assert("".join(sorted(key)) == ALPHABET)
        
        # make the forward and inverse dictionaries
        self.dict = {ALPHABET[i]: key[i] for i in range(len(ALPHABET))}
        self.dict_inv = {key[i]: ALPHABET[i] for i in range(len(ALPHABET))}
    
    def encrypt(self, x: str) -> str:
        return "".join(self.dict[c] for c in x)
    
    def decrypt(self, x: str) -> str:
        return "".join(self.dict_inv[c] for c in x)


def Vignere(x: str, k: str) -> str:
    x = encode(x)
    k = encode(k)
    x = [(x[i] + k[i % len(k)]) % len(ALPHABET) for i in range(len(x))]
    return decode(x)

def OneTimePad(x: str, k: str) -> str:
    assert(len(x) <= len(k))
    x = encode(x)
    k = encode(k)
    x = [(x[i] + k[i]) % len(ALPHABET) for i in range(len(x))]
    return decode(x)

# frequency analysis
def get_letter_counts(x: str):
    return {c: x.count(c) for c in x}

def get_letter_frequencies(x: str):
    return {c: x.count(c)/len(x) for c in x}


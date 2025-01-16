from main import *

# checking examples from text

print(encode("HELLO"))

print(decode(encode("HELLO")))

print(ROT("HELLO", 13))

print(Affine("HELLO", (11, 5)))

print(Affine("IN", (17, 5)))

cipher = PermutationCipher("CQMELROJKPAHWZNFGYXSITBVUD")

print(cipher.encrypt("HELLO"))

print(get_letter_counts("HELLO"))

print(get_letter_frequencies("HELLO"))

print(Vignere("WEMEETATDAWN", "SANDWICH"))
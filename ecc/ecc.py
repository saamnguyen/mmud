from ecc.curve import Curve25519
from ecc.key import gen_keypair
from ecc.cipher import ElGamal


# Plaintext
plaintext = b"Sam Nguyen"
# Generate key pair
pri_key, pub_key = gen_keypair(Curve25519)

print("Private Key: " + str(pri_key))
print("Public Key: " + str(pub_key))

# Encrypt using ElGamal algorithm
cipher_elg = ElGamal(Curve25519)
C1, C2 = cipher_elg.encrypt(plaintext, pub_key)
# Decrypt
new_plaintext = cipher_elg.decrypt(pri_key, C1, C2)

print("Plain Text: " + str(new_plaintext))

print(new_plaintext == plaintext)
# >> True
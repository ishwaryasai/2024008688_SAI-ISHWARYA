#RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

#keys genration
key = RSA.generate(2048)
public_key = key.publickey()

# Encryption
message = b"Hello RSA"
cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
encrypted = cipher.encrypt(message)
print("Encrypted:", encrypted.hex())

# Decryption
cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted.decode())

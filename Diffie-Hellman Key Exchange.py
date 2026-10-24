# Diffie-Hellman Key Exchange

p = 23
g = 5

a = 6
b = 15

A = pow(g, a, p)
B = pow(g, b, p)

key_A = pow(B, a, p)
key_B= pow(A, b, p)

print("Public prime (p):", p)
print("Generator (g):", g)
print("Alice's public key:", A)
print("Bob's public key:", B)
print("Alice's shared key:", key_A)
print("Bob's shared key:", key_B)

if key_A == key_B:
    print("Key exchange successful")
else:
    print("Key exchange failed")

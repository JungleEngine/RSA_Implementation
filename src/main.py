from Crypto.Util import number as crypto
import numpy as np
from sympy import mod_inverse


def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return x0


def generate_keys(n_bits):
    while True:
        p = crypto.getPrime(n_bits)
        q = crypto.getPrime(n_bits)
        if p != q:
            break

    n = p * q
    phi = (p - 1) * (q - 1)

    # Generate e.
    while True:
        e = np.random.randint(2, phi)
        gcd = np.gcd(e, phi)
        if gcd == 1:
            break

    d = mod_inverse(e, phi)
    print(phi)
    return n, e, d


if __name__ == '__main__':
    msg = "hello"
    n, e, d = generate_keys(12)

    # Encrypt message with block size = 1 character.
    encrypted_data = [pow(ord(char), e, n) for char in msg]

    # Decrypted data.
    decrypted_data = "".join([chr(pow(char, d, n)) for char in encrypted_data])

    print(" public_key: ", n, " private_key: ", d)
    print("decrypted_msg: ", decrypted_data)

    if (decrypted_data != msg):
        print("decrypted_data not equal to original message")

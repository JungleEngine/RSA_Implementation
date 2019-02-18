from Crypto.Util import number as crypto
import numpy as np
import time
from sympy import mod_inverse
import random
from math import gcd
import matplotlib.pyplot as plt


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
        e = random.getrandbits(n_bits) + 2
        print(phi)
        g = gcd(e, phi)
        if g == 1:
            break

    d = mod_inverse(e, phi)
    return n, e, d


def test_RSA(msg, min_bits, max_bits, step=2):
    key_length = []
    enc_time = []
    n_bits = min_bits
    while n_bits <= max_bits:
        n, e, d = generate_keys(n_bits)
        # Encrypt message with block size = 1 character.
        t_start = time.time()
        encrypted_data = [pow(ord(char), e, n) for char in msg]
        t_end = time.time()

        enc_time.append(t_end - t_start)
        key_length.append(n_bits)
        # Decrypted data.
        decrypted_data = "".join([chr(pow(char, d, n)) for char in encrypted_data])

        if (decrypted_data != msg):
            print("decrypted_data not equal to original message")

        n_bits = n_bits * step
        print("current n_bits: ", n_bits)
    return key_length, enc_time

if __name__ == '__main__':
    msg = "h"
    key_length, enc_time = test_RSA(msg, min_bits=16, max_bits=1024, step=2)

    plt.plot(key_length, enc_time, linewidth=2.0)
    plt.ylabel('Encryption time')
    plt.xlabel('key_length time')
    plt.show()
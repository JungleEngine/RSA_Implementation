from sympy import mod_inverse
import math
import numpy as np

d = 8891


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    primesList = []
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True):

            primesList.append(p)

            # Update all multiples of p 
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    return prime, primesList


def find_prime_factors(n, prime_or_not, primes):
    for i in range(len(primes)):
        if n % primes[i] == 0:
            factor2 = int(n / primes[i])
            if prime_or_not[factor2]:
                # print("Prime factor of ", n , ": ",primes[i], factor2)
                return primes[i], factor2


# Extended Euclidean Algorithm 
def gcd_extended(a, b, x, y):
    # Base Case
    if a == 0:
        x = 0
        y = 1
        return b

        # To store results of recursive call
    x1 = 1
    y1 = 1
    gcd = gcd_extended(b % a, a, x1, y1)

    # Update x and y using results of recursive call 
    x = y1 - (b / a) * x1
    y = x1

    return gcd


def brute_force_attack(n, e, encrypted_data):
    prime_factors = []

    i = 2

    while (i * i <= n):
        if n % i == 0:
            prime_factors = [i, n / i]
            break
        i += 1


    p = prime_factors[0]
    q = prime_factors[1]
    phi = (p - 1) * (q - 1)

    # gcd = GCDExtended(e, phi, d, k)
    # print(d, k)

    # Private key
    d = mod_inverse(e, phi)

    # Decrypted data.
    decrypted_data = "".join([chr(pow(char, d, n)) for char in encrypted_data])
    return decrypted_data


def chosen_cipher_attack(n, e, msg, receiver):
    # Encrypt message with block size = 1 character.
    encrypted_data = [char * pow(2, e, n) for char in msg]

    decrypted_data = receiver.decrypt_msg(encrypted_data)

    ret = "".join([chr(char // 2) for char in decrypted_data])
    return ret
#
# brute_force_attack(197 * 199, 323, "hello")
# chosen_cipher_attack(199 * 197, 323, "hello")

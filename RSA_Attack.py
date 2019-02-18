import numpy as np
import math
from sympy import mod_inverse

d = 8891

def SieveOfEratosthenes(n): 
 
    prime = [True for i in range(n+1)]
    primesList = []
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
            
            primesList.append(p)

            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1

    return prime, primesList
       

def FindPrimeFactors(n, prime_or_not, primes):
	for i in range(len(primes)):
		if n % primes[i] == 0:
			factor2 = int(n / primes[i])
			if prime_or_not[factor2]:
				#print("Prime factor of ", n , ": ",primes[i], factor2)
				return primes[i], factor2


# Extended Euclidean Algorithm 
def GCDExtended(a, b, x, y):

    # Base Case
    if a == 0 :  
        x = 0
        y = 1
        return b 
       
    # To store results of recursive call    
    x1 = 1
    y1 = 1
    gcd = gcdExtended(b%a, a, x1, y1) 
  
    # Update x and y using results of recursive call 
    x = y1 - (b/a) * x1 
    y = x1 
  
    return gcd 


def BruteForceAttack(n, e, msg):

    # Encrypt message with block size = 1 character.
    encrypted_data = [pow(ord(char), e, n) for char in msg]

    # Generate prime numbers till N
    N = 1000000
    prime_or_not, primes = SieveOfEratosthenes(N)

    prime_factors = FindPrimeFactors(n, prime_or_not, primes)
    print("Prime factors: ", prime_factors)

    p = prime_factors[0]
    q = prime_factors[1]
    phi = (p-1) * (q-1)

    #gcd = GCDExtended(e, phi, d, k)
    #print(d, k)

    # Private key
    d = mod_inverse(e, phi)

    # Decrypted data.
    decrypted_data = "".join([chr(pow(char, d, n)) for char in encrypted_data])

    if decrypted_data == msg:
        print("Success: Decrypted message: ", decrypted_data)
    else:
        print("Failed: Decrypted message: ", decrypted_data)

def Decrypt(encrypted_data, n):

    # Decrypted data.
    decrypted_data = [chr(pow(char, d, n)) for char in encrypted_data]
    return decrypted_data



def ChosenCipherAttack(n, e, msg):

    # Encrypt message with block size = 1 character.
    encrypted_data = [pow(ord(char) * 2, e, n) for char in msg]

    decrypted_data = Decrypt(encrypted_data, n)

    decrypted_data = "".join([chr(ord(char) // 2) for char in decrypted_data])

    if decrypted_data == msg:
        print("Success: Decrypted message: ", decrypted_data)
    else:
        print("Failed: Decrypted message: ", decrypted_data)


BruteForceAttack(197*199, 323, "hello")
ChosenCipherAttack(199*197,323, "hello")
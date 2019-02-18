import numpy as np
import math

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

# Generate prime numbers till N
N = 1000000
prime_or_not, primes = SieveOfEratosthenes(N)


n = 2773
e = 1213
m = 1216421
d = 0
k = 0

prime_factors = FindPrimeFactors(n, prime_or_not, primes)
print(prime_factors)

phi = (prime_factors[0] - 1) * (prime_factors[1] - 1)

gcd = GCDExtended(e, phi, d, k)
print(d, k)
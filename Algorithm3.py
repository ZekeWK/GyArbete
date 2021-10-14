import GaussianInteger as GI
import Erastothenes
import math

def Algorithm3(n):
    natural_primes = set(Erastothenes.ErastothenesSieve(n)) #Add all the natural one's aswell

    gaussian_primes = []

    sqrt_n = math.isqrt(n)
    for a in range(sqrt_n):
        
        max_b = min(math.isqrt(n - a**2), a)
        for b in range(1, max_b + 1):

            possible_gaussian_prime = a**2 + b**2
            
            if possible_gaussian_prime in natural_primes:
                gaussian_primes.append(GI.GaussianInteger(a, b))
                gaussian_primes.append(GI.GaussianInteger(a, b).con())
    
    for possible_gaussian_prime in natural_primes:
        if possible_gaussian_prime**2 > n:
            break

        if possible_gaussian_prime % 4 == 3:
            gaussian_primes.append(possible_gaussian_prime)

    return gaussian_primes

result = Algorithm3(100)
for i in result:
    print(i)
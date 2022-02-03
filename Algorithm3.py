import GaussianInteger as GI
import Erastothenes
import math

def Algorithm3(n, natural_primes_list):
    natural_primes = set(natural_primes_list) 

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
            gaussian_primes.append(GI.GaussianInteger(possible_gaussian_prime, 0))

    return gaussian_primes

if __name__ == "__main__":    
    input = 100
    result = Algorithm3(input, Erastothenes.ErastothenesSieve(input))
    result.sort()
    for i in result:
        print(i)
import GaussianInteger as GI
import Erastothenes
import math

def Algorithm3(n, natural_primes_set):
    natural_primes = natural_primes_set 

    gaussian_primes = []

    sqrt_n = math.isqrt(n)
    for a in range(sqrt_n + 1):
        
        max_b = min(math.isqrt(n - a**2), a)
        for b in range(1, max_b + 1):

            norm = a**2 + b**2
            
            if norm in natural_primes:
                gaussian_primes.append(GI.GaussianInteger(a, b))
                gaussian_primes.append(GI.GaussianInteger(a, b).conjugate())

        if a % 4 == 3 and a in natural_primes:
            gaussian_primes.append(GI.GaussianInteger(a, 0))

    return gaussian_primes

if __name__ == "__main__":    
    input = 100
    result = Algorithm3(input, set(Erastothenes.ErastothenesSieve(input)))
    result.sort()
    for i in result:
        print(i)
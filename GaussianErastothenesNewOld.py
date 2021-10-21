import GaussianInteger as GI
import math

def Gaussian_Erastothenes(n):
    n_squared = n**2
    possible_gaussian_primes = [[(GI.GaussianInteger(x, y).abs2() <= n_squared) for y in range(-n, n + 1)] for x in range(-n, n + 1)]

    print(possible_gaussian_primes)

    for (a,b) in range(2).enumerate(): #Fix this to be going through all the numbers in order of norm.
        if not possible_gaussian_primes[a][b]:
            continue

        for (x, y) in range(3):
            if possible_gaussian_primes[x][y]:
                possible_gaussian_primes[x][y] = False

    gaussian_primes = []

    for a in range(n):
        for b in range(b):
            if possible_gaussian_primes[a][b]:
                gaussian_primes.append(GI.GaussianInteger(a,b))

    return gaussian_primes


    
Gaussian_Erastothenes(5)
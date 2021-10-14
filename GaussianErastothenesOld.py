import GaussianInteger as GI
import math

def Gaussian_Erastothenes(n): #Make sure this works?
    n_2 = n**2
    possible_gaussian_primes = []
    for a in range(n+1):
        possible_gaussian_primes_with_a = []
        for b in range(a + 1):
            if GI.GaussianInteger(a, b).abs2() <= n_2:
                possible_gaussian_primes_with_a.append(True)
            else:
                possible_gaussian_primes.append(possible_gaussian_primes)
                print(possible_gaussian_primes_with_a)
                break
    
    for norm in range(n):
        for a in range(norm):
            b = math.sqrt(n**2 - a**2)
            if not b.is_integer(): #Make this instead check if b is an actua integer
                continue
            
            if possible_gaussian_primes[a][b]:
                for sdsd in sds: #Make this go throug all the val

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


    
Gaussian_Erastothenes(10)
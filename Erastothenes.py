import math

def ErastothenesSieve(n):
    sqrt_n = math.floor(math.sqrt(n))

    possible_primes = [True for x in range(n + 1)] 

    for number in range(2, sqrt_n + 1):
        if not possible_primes[number]:
            continue
        
        else:
            for non_prime in range(number * 2, n + 1, number):
                possible_primes[non_prime] = False

    primes = []

    for number in range(2, n + 1):
        if possible_primes[number]:
            primes.append(number)
    
    return primes
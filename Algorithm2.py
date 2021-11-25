import Erastothenes
import GaussianInteger as GI
import math

def Algorithm2(n):
    global natural_primes
    
    natural_primes = Erastothenes.ErastothenesSieve(n)

    sqrt_n = math.sqrt(n)

    gaussian_primes = [GI.GaussianInteger(1, 1), GI.GaussianInteger(1, -1)]
    for natural_prime in natural_primes:
        if natural_prime % 4 == 1:
            gaussian_prime = find_two_squares_that_sum_to(natural_prime)
            
            gaussian_primes.append(gaussian_prime)
            gaussian_primes.append(gaussian_prime.con())
        
        elif natural_prime % 4 == 3:
            if natural_prime <= sqrt_n:
                gaussian_primes.append(natural_prime)
    
    return gaussian_primes

def eulers_criterion(prime):
    global natural_primes
    if prime % 4 != 1:
        raise Exception

    exponent = (prime - 1) // 4

    for natural_prime in natural_primes:
        possible_root = pow(natural_prime, exponent, prime)
        
        if pow(possible_root, 2, prime) == prime -1:
            return possible_root

def euclids_algorithm_stop_early(a, b, stop_size):
    if a < stop_size:
        return (a, b)
    return euclids_algorithm_stop_early(b, a%b, stop_size)

def find_two_squares_that_sum_to(prime):
    if prime % 4 == 3:
        raise Exception

    return GI.GaussianInteger.new(euclids_algorithm_stop_early(prime, eulers_criterion(prime), math.sqrt(prime))) 


if __name__ == "__main__":    
    result = Algorithm2(100)
    for i in result:
        print(i)
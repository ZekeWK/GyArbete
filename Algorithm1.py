import GaussianInteger as GI
import math

def Algorithm1(n):
    sqrt_n = math.isqrt(n)

    cashed_b = (None, None)
    def get_b(a):
        if cashed_b[0] == a:
            return cashed_b[1] 
        else:
            val = min(a, math.isqrt(n-(a**2)))+1
            cash = (a, val)
            return val

    possible_gaussian_primes = [[True for b in range(0, get_b(a))] for a in range(1, sqrt_n + 1)]
    
    def in_bounds_possible_gaussian_primes(gaussian_integer):
        (a, b) = gaussian_integer.get_tuple()

        return 0 <= a-1 < len(possible_gaussian_primes) and 0 <= b < len(possible_gaussian_primes[a-1])

    def remove_non_prime(gaussian_non_prime):
        if in_bounds_possible_gaussian_primes(gaussian_non_prime):
            possible_gaussian_primes[gaussian_non_prime.real()-1][gaussian_non_prime.imag()] = False

    
    def readd_prime(gaussian_prime):
        if in_bounds_possible_gaussian_primes(gaussian_prime):
            possible_gaussian_primes[gaussian_prime.real()-1][gaussian_prime.imag()] = True
    
    def get_gaussian_prime(possible_gaussian_prime):
        if in_bounds_possible_gaussian_primes(possible_gaussian_prime):
            return possible_gaussian_primes[possible_gaussian_prime.real() -1][possible_gaussian_prime.imag()]
        return False

    def remove_multiples(z):
        n_div_norm =  n // z.abs2()
        sqrt_n_div_norm = math.isqrt(n_div_norm)

        for x in range(1, sqrt_n_div_norm + 1):
            for y in range(sqrt_n_div_norm + 1):
                w = GI.GaussianInteger(x, y)
                if w.abs2() > n_div_norm:
                    break
                
                product1 = z       * w
                product2 = z.con() * w
                product3 = z       * w.con()
                product4 = z.con() * w.con()

                if product1.real() < product1.imag() and product2.real() < product2.imag() and 0 > product3.imag() and 0 > product4.imag():
                    break

                remove_non_prime(product1)
                remove_non_prime(product2)
                remove_non_prime(product3)
                remove_non_prime(product4)

        readd_prime(z)

    remove_non_prime(GI.GaussianInteger(1, 0))
    
    for gaussian_integer in (GI.GaussianInteger(1, 1), GI.GaussianInteger(2, 1), GI.GaussianInteger(3, 0)):
        remove_multiples(gaussian_integer)

    sqrt_2_sqrt_n = math.isqrt(sqrt_n*2)
    for manhattan_distance in range(2, sqrt_2_sqrt_n + 1):  
        manhattan_distance_div_2 = manhattan_distance//2 + 1

        for a in range(manhattan_distance_div_2, manhattan_distance + 1):
            b = manhattan_distance - a

            z = GI.GaussianInteger(a, b)

            if get_gaussian_prime(z):
                remove_multiples(z)

    gaussian_primes = []
    for (a, values) in enumerate(possible_gaussian_primes):
        for (b, value) in enumerate(values):
            if value:
                if b != 0:
                    gaussian_primes.append(GI.GaussianInteger(a + 1,b))
                    gaussian_primes.append(GI.GaussianInteger(a + 1,b).con())
                else:
                    gaussian_primes.append(GI.GaussianInteger(a+1, 0))
    return gaussian_primes

if __name__ == "__main__":    
    input = 100
    result = Algorithm1(input)
    result.sort()
    for i in result:
        print(i)
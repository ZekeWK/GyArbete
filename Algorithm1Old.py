import GaussianInteger as GI
import math

def Algorithm1(n):
    sqrt_n = math.isqrt(n) + 1
    possible_gaussian_primes = [[True for b in range(min(math.isqrt(n - a**2), a))] for a in range(sqrt_n)]
    
    possible_gaussian_primes[1][0] = False

    for norm in range(sqrt_n):
        norm_div_2 = norm // 2 + 1
        for a in range(norm_div_2, norm):
            b = norm_div_2 - a

            #print(a, b)
            #print(possible_gaussian_primes)
            if possible_gaussian_primes[a][b]: #I am gonna have to do this again...
                #print("HI")
                print(GI.GaussianInteger(a, b))

                n_div_norm = n//norm
                z = GI.GaussianInteger(a, b)

                for x in range(1, n_div_norm):
                    for y in range(n_div_norm):
                        w = GI.GaussianInteger(x, y)
                        
                        product1 = z       * w
                        product2 = z.con() * w
                        product3 = z       * w.con()
                        product4 = z.con() * w.con()

                        def remove_non_prime(product):
                            if product.real() < sqrt_n and product.real() >= 0 and product.imag() < min(math.isqrt(n**2 - product.real()**2), product.real()) and product.imag() > 0:
                                possible_gaussian_primes[product.real()][product.imag()] = False
                        
                        remove_non_prime(product1)
                        remove_non_prime(product2)
                        remove_non_prime(product3)
                        remove_non_prime(product4)
    gaussian_primes = []
    for (a, values) in enumerate(possible_gaussian_primes):
        for (b, value) in enumerate(values):
            if value:
                gaussian_primes.append(GI.GaussianInteger(a,b))
                gaussian_primes.append(GI.GaussianInteger(a,b).con())
    print(possible_gaussian_primes)
    return gaussian_primes

result = Algorithm1(100)
print("---------------------------")
for i in result:
    print(i)
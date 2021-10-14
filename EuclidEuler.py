from GaussianInteger import GaussianInteger
import math

#x^2=-1 mod p
def euler(p):
    if prime % 4 != 1:
        raise Exception

    exponent = int((p - 1) / 4) #a^(p-1)/2 = -/+ 1 mod p Eulers criterion

    for natural_prime in range(2,p):
        root = pow(x, exp, p)

        #if x % 10000 == 0:
        #print(x, root, pow(root, 2, p) - p)
        
        if pow(root, 2, p) == p-1:
            return root

def euclids_alghorithm(a, b, r):
    if a < r:
        return (a, b)
    return euclids_alghorithm(b, a%b, r)



def find_two_squares_that_sum_to(prime):
    if prime % 4 == 3:
        raise Exception
    return GaussianInteger(euclids_alghorithm(prime, euler(prime), math.sqrt(prime)))

#find_two_squares_that_sum_to(101)
find_two_squares_that_sum_to(5)

find_two_squares_that_sum_to(332804805798337) #This one gives a weird result difference

#euclid(332804805798337)

#euclid(769770656001913)

#euclid(826539253381390957)

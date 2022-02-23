from unittest import result
import Erastothenes

from Algorithm1 import Algorithm1
from Algorithm2 import Algorithm2
from Algorithm3 import Algorithm3

def run_Algorithm1(input):
    return Algorithm1(input)

def run_Algorithm2(input):
    return Algorithm2(input, Erastothenes.ErastothenesSieve(input))

def run_Algorithm3(input):
    return Algorithm3(input, set(Erastothenes.ErastothenesSieve(input)))

def main():
    inputs = range(10000, 100010)

    for n in inputs:
        result1 = sorted(run_Algorithm1(n))
        result2 = sorted(run_Algorithm2(n))
        result3 = sorted(run_Algorithm3(n))

        result1 = set(result1)
        result2 = set(result2)
        result3 = set(result3)

        differed = sorted(result1.symmetric_difference(result2).union(result1.symmetric_difference(result3)).union(result2.symmetric_difference(result3)))

        print("For n :" + str(n))

        for i in differed:

            sets = [' ', ' ', ' ']

            if i in result1:
                sets[0] = '1'

            if i in result2:
                sets[1] = '2'
                
            if i in result3:
                sets[2] = '3'
            
            print(str(i) + "      "+ "".join(sets))




    print("Done")



if __name__ == "__main__":
    main()
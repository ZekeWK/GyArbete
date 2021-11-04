import Algorithm1
import Algorithm2
import Algorithm3

import time

def time_it(algorithm, times_for_average, inputs):
        output = ""
        for input in inputs:
            start_time = time.time()
            for i in range(times_for_average):
                algorithm(input)
            stop_time = time.time()
            average_time = (stop_time - start_time) / times_for_average
            output += str(input) + ", " + str(average_time) + "\n"
        return output

def main():
    for i in [Algorithm1.Algorithm1, Algorithm2.Algorithm2, Algorithm3.Algorithm3]: 
        print(str(i) + " Input, Time")
        print(time_it(i, 10, range(100, 1001, 100)))

if __name__ == "__main__":
    main()
import Algorithm1
import Algorithm2
import Algorithm3

import tracemalloc

def measure_it(algorithm, times_for_average, inputs):
    output = ""
    for input in inputs:
        memory_peaks_sum = 0
        for i in range(times_for_average):
            tracemalloc.start()
            algorithm(input)
            memory_peaks_sum += tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
        average_peak_memory_usage = memory_peaks_sum / times_for_average
        
        output += str(input) + ", " + str(average_peak_memory_usage) + "\n"
    return output

def main():
    for i in [Algorithm1.Algorithm1, Algorithm2.Algorithm2, Algorithm3.Algorithm3]: 
        print(str(i) + " Input, Time")
        print(measure_it(i, 10, range(100, 1001, 100)))

if __name__ == "__main__":
    main()
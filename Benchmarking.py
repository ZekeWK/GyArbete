from Algorithm1 import Algorithm1
from Algorithm2 import Algorithm2
from Algorithm3 import Algorithm3

import tracemalloc
import time
from datetime import datetime
from tqdm import tqdm

def main():
    inputs = range(1000, 10001, 1000)
    iterations_time = 10
    iterations_memory = 2

    benchmarks = benchmark_the_algorithms(inputs, iterations_time, iterations_memory)

    output_string = "Benchmark run at: " + str(datetime.now()) + " , with iterations_time: " + str(iterations_time) + " , and with iterations_memory: " + str(iterations_memory) + ".\n"
    output_string += benchmarks_to_readable(benchmarks)
    
    with open("results.txt", "a") as f:
        f.write(output_string)

    with open("last_results.txt", "w+") as f:
        f.write(output_string)

def benchmarks_to_readable(benchmarks):
    output_string = str()
    for benchmark_type, string in zip(benchmarks, ["Time:\n", "Memory:\n"]):
        output_string += string
        for benchmark in benchmark_type:
            output_string += str(benchmark[0])[10:20] + "\n"
            for test in benchmark[1]:
                output_string += str(test[0]) + ", " + str(test[1]) + "\n"
            output_string += "\n"
    return output_string
    
def benchmark_the_algorithms(inputs, iterations_time, iterations_memory):
    time_benchmarks = []
    memory_benchmarks = []
    for algorithm in [Algorithm1, Algorithm2, Algorithm3]:
        time_benchmarks   .append(get_benchmark_of(get_time_used,   algorithm, tqdm(inputs), iterations_time))
        memory_benchmarks .append(get_benchmark_of(get_memory_peak, algorithm, tqdm(inputs), iterations_memory))
    return (time_benchmarks, memory_benchmarks)

def get_benchmark_of(test, algorithm, inputs, iterations_per):
    benchmarks = []
    for input in inputs:
        benchmarks.append((input, get_average_usage(test, algorithm, input, iterations_per)))
    return (algorithm, benchmarks)

def get_average_usage(test, algorithm, input, iterations):
    cur_sum = 0
    for _i in range(iterations):
        cur_sum += test(algorithm, input)
    return cur_sum/iterations

def get_memory_peak(algorithm, input):
    tracemalloc.start()
    algorithm(input)
    memory_peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return memory_peak

def get_time_used(algorithm, input):
    start_time = time.time()
    algorithm(input)
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    print("Activated")
    main()
    print("Done")
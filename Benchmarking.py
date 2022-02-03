from Algorithm1 import Algorithm1
from Algorithm2 import Algorithm2
from Algorithm3 import Algorithm3

import Erastothenes

import tracemalloc
import time
from datetime import datetime
from tqdm import tqdm
from copy import deepcopy
from bisect import bisect_right
import statistics

def main():
    inputs = range(100000, 5000001, 100000)
    iterations_time = 5
    iterations_memory = 3

    benchmarks = benchmark_the_algorithms(inputs, iterations_time, iterations_memory)
    
    output_string = "Benchmark run at: " + str(datetime.now()) + " , with iterations_time: " + str(iterations_time) + " , and with iterations_memory: " + str(iterations_memory) + ".\n"
    output_string += benchmarks_to_readable(benchmarks)
    
    with open("results.csv", "a") as f:
        f.write(output_string)

    with open("last_results.csv", "w+") as f:
        f.write(output_string)
    
    print(output_string)

def benchmarks_to_readable(benchmarks):
    output_string = str()
    for benchmark_type, string in zip(benchmarks, ["Input, Time, Standard Deviation:\n", "Input, Memory, Standard Deviation:\n"]):
        output_string += string
        for benchmark in benchmark_type:
            output_string += str(benchmark[0]) + "\n" #[14:24]
            for test in benchmark[1]:
                output_string += str(test[0]) + "; " + str(test[1]) + "; " + str(test[2]) + "\n"
            output_string += "\n"
    return output_string
    
def benchmark_the_algorithms(inputs, iterations_time, iterations_memory):
    global natural_primes
    natural_primes = Erastothenes.ErastothenesSieve(max(inputs))

    time_benchmarks = []
    memory_benchmarks = []
    for algorithm in [run_Algorithm1, run_Algorithm2, run_Algorithm3, run_Algorithm2_And_Erastothenes, run_Algorithm3_And_Erastothenes]:
        time_benchmarks   .append(get_benchmark_of(get_time_used,   algorithm, tqdm(deepcopy(inputs)), iterations_time))
        memory_benchmarks .append(get_benchmark_of(get_memory_peak, algorithm, tqdm(deepcopy(inputs)), iterations_memory))
    return (time_benchmarks, memory_benchmarks)

def get_benchmark_of(test, algorithm, inputs, iterations_per):
    benchmarks = []
    for input in inputs:
        (mean, standard_deviation) = get_mean_usage(test, algorithm, input, iterations_per)
        benchmarks.append((input, mean, standard_deviation))
    return (algorithm, benchmarks)

def get_mean_usage(test, algorithm, input, iterations):
    global natural_primes
    primes = natural_primes[0:bisect_right(natural_primes, input)]

    results = []
    for _i in range(iterations):
        results.append(test(algorithm, input, primes.copy()))
    
    mean = statistics.mean(results)
    standard_deviation = statistics.pstdev(results, mean)

    return (mean, standard_deviation)

def get_memory_peak(algorithm, input, primes):
    tracemalloc.start()
    algorithm(input, primes)
    memory_peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return memory_peak

def get_time_used(algorithm, input, primes):
    start_time = time.process_time()
    algorithm(input, primes)
    end_time = time.process_time()
    return end_time - start_time

def run_Algorithm1(input, primes):
    Algorithm1(input)

def run_Algorithm2(input, primes):
    Algorithm2(input, primes)

def run_Algorithm3(input, primes):
    Algorithm3(input, primes)

def run_Algorithm2_And_Erastothenes(input, primes):
    Algorithm2(input, Erastothenes.ErastothenesSieve(input))

def run_Algorithm3_And_Erastothenes(input, primes):
    Algorithm3(input, Erastothenes.ErastothenesSieve(input))


if __name__ == "__main__":
    input()
    print("Activated")
    main()
    print("Done")
    input()
import BenchmarkingConfig as Config

import BenchmarkingMemory
import BenchmarkingTime

import Algorithm1
import Algorithm2
import Algorithm3

from tqdm import tqdm

def main():
    output = open(Config.output_file, 'a')
    
    output.write("Test with config: \n    Times per input:" + str(Config.times_for_average) + "\n    Inputs: " + str(Config.inputs) + "\n\n")

    for algorithm in [Algorithm1.Algorithm1, Algorithm2.Algorithm2, Algorithm3.Algorithm3]: 
        output.write(str(algorithm)[10:20] + "\n\n")
        output.write("Input, Time \n" + BenchmarkingTime.time_it(algorithm, Config.times_for_average, tqdm(Config.inputs)) + "\n")
        output.write("Input, Memory \n" + BenchmarkingMemory.measure_it(algorithm, Config.times_for_average, tqdm(Config.inputs)) + "\n")

if __name__ == "__main__":
    print("Activated")
    main()
    print("Done")
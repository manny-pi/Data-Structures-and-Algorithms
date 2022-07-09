from matplotlib import pyplot as plt
import time
import sys
from random import randint as r
import sorting


def create_data_set(n):
    """Generates a randomized data set with n elements"""

    return [r(0, 100) for i in range(n)]


# Create an array of sample sizes; i.e. 1, 10, 20,
MAX_SIZE = int(1e2) * 3
STEP = 1
sample_sizes = [sample_size for sample_size in range(1, MAX_SIZE + 1, STEP)]

# {key=algorithm: value=[runtime per sample size]}
algorithms = {
    "insertionSort": [],
    "insertionSortRecursive": [],
    "selectionSort": [],
    "mergeSort": [],
}

# For each data set of size n, execute the algorithm and store their runtimes
for sample_size in sample_sizes:

    # Create a random data set of size sample_size
    sample_data = create_data_set(sample_size)

    # Execute each algorithm on the data set
    for func_name in algorithms:

        # Complete the method signature for the function that implements the algorithm
        arguments = ""
        if func_name == "insertionSort":
            arguments = f"({sample_data})"

        elif func_name == "insertionSortRecursive":
            arguments = f"({sample_data}, {sample_size - 1})"

        elif func_name == "selectionSort":
            arguments = f"({sample_data})"

        elif func_name == "mergeSort":
            arguments = f"({sample_data}, {0}, {sample_size - 1})"

        method_signature = f"sorting.{func_name}{arguments}"

        # Run the algorithm on sample_data
        start_time = time.perf_counter_ns()
        eval(method_signature)
        end_time = time.perf_counter_ns()

        # Add the amount of time taken for the sample size to the data set
        runtime = (end_time - start_time) / 1e6
        algorithms[func_name].append(runtime)


# Plot each algorithm and its runtime on the data sets
for func_name in algorithms:

    # Plot the data for the algorithm
    plt.plot(sample_sizes, algorithms[func_name], label=func_name)


plt.title("Runtime for Sorting Algorithms")
plt.legend()
plt.xlabel("Size of Data Set (n)")
plt.ylabel("Runtime (ms)")
plt.show()

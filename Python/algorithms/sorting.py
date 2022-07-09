import math
from matplotlib import pyplot as plt
import time
from random import randint


# Algorithms
def insertionSort(_in):
    j = 1
    while j < len(_in):
        key = _in[j]
        i = j - 1
        while i >= 0 and _in[i] > key:
            _in[i + 1] = _in[i]
            _in[i] = key
            i -= 1
        _in[i + 1] = key

        j += 1


def insertionSortRecursive(_in, n):
    if n > 0:
        insertionSortRecursive(_in, n - 1)
        key = _in[n]
        i = n - 1
        while i >= 0 and key <= _in[i]:
            temp = _in[i]
            _in[i] = key
            _in[i + 1] = temp

            i -= 1


def selectionSort(_in):
    j = 0
    while j < len(_in) - 1:
        smallest = _in[j]
        indexOfSmallest = j
        i = j + 1
        while i < len(_in):
            if _in[i] < smallest:
                smallest = _in[i]
                indexOfSmallest = i
                # print(_in)
            i += 1

        current = _in[j]
        _in[j] = smallest
        _in[indexOfSmallest] = current
        j += 1


def mergeSort(_in, p, r):
    if p < r:
        q = math.floor((p + r) / 2)         # Calculate midpoint q of sub-array A[p.. r]
        mergeSort(_in, p, q)                # Call mergeSort on sub-array A[p.. q]
        mergeSort(_in, q + 1, r)            # Call mergeSort on sub-array A[q + 1.. r]
        mergeSortAux(_in, p, q, r)          # Call merge on sub-array A[p.. r]


def mergeSortAux(_in, p, q, r):
    n_1 = q - p + 1     # Compute length of A[p.. q]
    n_2 = r - q         # Compute length of A[q + 1.. r]

    L = []              # New array to hold sub-array A[p.. q]
    R = []              # New array to hold sub-array A[q + 1 .. r]

    # Copy sub-array A[p.. q] to L
    for i in range(n_1):
        L.append(_in[p + i])

    # Copy sub-array A[q + 1.. r] to R 
    for j in range(n_2):
        R.append(_in[q + j + 1])

    # Add sentinel values to the arrays
    L.append(None)
    R.append(None)

    # Compare values from L and R, and sort the array
    i = 0
    j = 0
    for k in range(p, r + 1):

        # Execute if reached sentinel value on left sub-array
        if L[i] is None:
            _in[k] = R[j]
            j += 1

        # Execute if reached sentinel value on right sub-array
        elif R[j] is None:
            _in[k] = L[i]
            i += 1

        # Exe cute if not reached sentinel value
        else:
            if L[i] <= R[j]:
                _in[k] = L[i]  # Replace the element at _in[k]
                i += 1         # Move on to the next element in L

            else:
                _in[k] = R[j]
                j += 1


# Tests
def testInsertionSort(sample_data=None, sample_size=10):
    """ Runs INSERTION-SORT on an array a given sequence of numbers """

    runTest('insertionSort', sample_data, sample_size)


def testInsertionSortRecursive(sample_data=None, sample_size=10):
    """ Runs INSERTION-SORT (recursive) on an array a given sequence of numbers """

    runTest('insertionSortRecursive', sample_data, sample_size)


def testSelectionSort(sample_data=None, sample_size=10):
    """ Runs SELECTION-SORT on a given sequence of numbers """

    runTest('selectionSort', sample_data, sample_size)


def testMergeSort(sample_data=None, sample_size=10):
    """Runs MERGE SORT on an array of 10 randomly generated numbers """

    runTest('mergeSort', sample_data, sample_size)


def runTest(func_name, sample_data, sample_size):
    # Conversion: 1 nanosecond = 1e-6 milliseconds

    # Execute if the caller doesn't provide a data set, and only provides a sample_size > 0
    if sample_data is None:
        sample_data = create_sample(sample_size)        # Create data set
        sample_size = len(sample_data)                  # Store the size of the data set

    # Execute if the caller provides a data set
    else:
        sample_size = len(sample_data)                  # Store the size of the data set

    # Complete the method signature for the method we're testing
    arguments = ""
    if func_name == 'insertionSort':
        arguments = f"({sample_data})"

    elif func_name == 'insertionSortRecursive':
        arguments = f"({sample_data}, {sample_size - 1})"

    elif func_name == 'selectionSort':
        arguments = f"({sample_data})"

    elif func_name == 'mergeSort':
        arguments = f"({sample_data}, {0}, {sample_size - 1})"

    method_signature = f"{func_name}{arguments}"

    # Print the results
    print(f"- - - - {func_name} Test - - - -")
    print(f"Sample size: {sample_size}")
    # print("Before: ", sample_data)
    print("\t\t- Start Processing -")

    print("\t\t\t...")

    # Execute sorting algorithm
    start_time = time.perf_counter_ns()
    eval(method_signature)
    end_time = time.perf_counter_ns()

    print("\t\t- End Processing -")
    # print("After:  ", sample_data)
    print("Time Taken (ms): %.5f" % ((end_time - start_time) / 1e6))
    print()


def plotAlgorithms():
    # Array containing size data sets of: n 1, 50, 100, ..., 1000
    sample_sizes = [sample_size for sample_size in range(1, 1000, 10)]
    sample_runtimes = []

    # Store the names of the algorithms we want to test
    algorithms = {'insertionSort': [], 'insertionSortRecursive': [], 'selectionSort': [], 'mergeSort': []}
    for func_name in algorithms:

        for sample_size in sample_sizes:

            # Create a random data set of size sample_size
            sample_data = [randint(0, 100) for i in range(sample_size)]

            # Complete the method signature for the function that implements the algorithm
            arguments = ""
            if func_name == 'insertionSort':
                arguments = f"({sample_data})"

            elif func_name == 'insertionSortRecursive':
                arguments = f"({sample_data}, {sample_size - 1})"

            elif func_name == 'selectionSort':
                arguments = f"({sample_data})"

            elif func_name == 'mergeSort':
                arguments = f"({sample_data}, {0}, {sample_size - 1})"

            method_signature = f"{func_name}{arguments}"

            # Run the algorithm on sample_data
            start_time = time.perf_counter_ns()
            eval(method_signature)
            end_time = time.perf_counter_ns()

            # Add the amount of time taken for the sample size to the data set
            runtime = (end_time - start_time)
            algorithms[func_name].append(runtime)

        # Plot the data for the algorithm
        plt.plot(sample_sizes, algorithms[func_name], label=func_name)

    plt.title("Runtime for Sorting Algorithms")
    plt.legend()
    plt.xlabel("Size of Data Set (n)")
    plt.ylabel("Runtime (ns)")
    plt.show()


# Used to generate random data sets
def create_sample(sample_size):
    """ Returns an array of random integers """
    return [randint(1, 100) for i in range(sample_size)]


if __name__ == '__main__': 
    # Create data sets 
    s_size = int(1e2) * 3
    s_data = create_sample(s_size)

    testInsertionSort(sample_data=s_data)
    # testInsertionSortRecursive(sample_data=s_data)
    # testSelectionSort(sample_data=s_data)
    # testMergeSort(sample_data=s_data)



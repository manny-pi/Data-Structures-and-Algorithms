import math
import random
import time

# Algorithms
def linearSearch(_in, searchValue):
    for i in range(len(_in)):
        if _in[i] == searchValue:
            return i

    return -1


def binarySearch(_in, searchValue):
    lowerBound = 0
    upperBound = len(_in) - 1

    while lowerBound <= upperBound:
        mid = math.floor((lowerBound + upperBound) / 2)
        if _in[mid] == searchValue:
            return mid
        elif _in[mid] < searchValue:
            lowerBound = mid + 1
        elif _in[mid] > searchValue:
            upperBound = mid - 1

    return -1


def binarySearchRecursive(_in, searchValue, lowerBound, upperBound):
    mid = math.floor((lowerBound + upperBound) / 2)
    if _in[mid] == searchValue:
        return mid

    elif upperBound == lowerBound:
        return -1

    elif _in[mid] < searchValue:
        return binarySearchRecursive(_in, searchValue, mid + 1, upperBound)

    elif _in[mid] > searchValue:
        return binarySearchRecursive(_in, searchValue, lowerBound, mid - 1)


# Tests
def testLinearSearch(_in, searchValue):
    runTest("linearSearch", _in, searchValue)


def testBinarySearch(sample_data, searchValue):
    runTest("binarySearch", sample_data, searchValue)


def testBinarySearchRecursive(sample_data, searchValue):
    runTest("binarySearchRecursive", sample_data, searchValue)


def runTest(func_name, sample_data, searchValue):

    arguments = ""
    if func_name == "linearSearch" or func_name == "binarySearch":
        arguments = f"({sample_data}, {searchValue})"
    elif func_name == "binarySearchRecursive":
        arguments = f"({sample_data}, {searchValue}, {0}, {len(sample_data)})"

    method_signature = f"{func_name}{arguments}"

    start_time = time.perf_counter_ns()
    index = eval(method_signature)
    end_time = time.perf_counter_ns()
    runtime = (end_time - start_time) / 1e6

    print(f"- - - - {func_name} test - - - - ")
    print(f"Value found @ i={index}")
    print(f"Runtime (ms): {runtime}")
    print()


def create_data_set(n=10):
    """ Generates a random data set of size n"""
    upperBound = random.randint(0, int(1e4))
    return [i for i in range(n + 1)]


# Create data sets
data_set = create_data_set(n=int(1e6))
random_index = random.randint(0, len(data_set))
v = data_set[random_index]

testBinarySearch(data_set, v)
testBinarySearchRecursive(data_set, v)
testLinearSearch(data_set, v)


import sys
help(sys)
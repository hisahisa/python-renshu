# Function to calculate sum of all elements in matrix
# sum(arr) is a python inbuilt function which calculates
# sum of each element in a iterable ( array, list etc ).
# map(sum,arr) applies a given function to each item of
# an iterable and returns a list of the results.

import numpy as np


def FindSum(arr):
    # inner map function applies inbuilt function
    # sum on each row of matrix arr and returns
    # list of sum of elements of each row
    # return map(sum, arr)
    print(arr)
    return sum(map(sum, arr))


def custom(n):
    return n + 1
# Driver function
if __name__ == "__main__":
    arr = np.asarray([[1, 2, 3], [4, 5, 6], [5, 6, 19]])
    #arr = [[1, 2, 3], [4, 5, 6], [5, 6, 19]]
    print("Sum = ", list(map(custom, arr)))

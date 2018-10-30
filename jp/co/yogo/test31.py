# Function to calculate sum of all elements in matrix
# sum(arr) is a python inbuilt function which calculates
# sum of each element in a iterable ( array, list etc ).
# map(sum,arr) applies a given function to each item of
# an iterable and returns a list of the results.

import numpy as np
import re


def FindSum(arr):
    # inner map function applies inbuilt function
    # sum on each row of matrix arr and returns
    # list of sum of elements of each row
    # return map(sum, arr)
    print(arr)
    return sum(map(sum, arr))


def custom(n):
    return (n[0]+1, n[1])


def custom_filter(n):
    pattern = '^Beat'
    repatter = re.compile(pattern)
    return repatter.match(n[0])


# Driver function
if __name__ == "__main__":
    #l1 = [(7, 2), (3, 4), (5, 5), (10, 3)]
    l1 = [('Beal', 2), ('Beatles', 4), ('Beatis', 5), ('Beui', 3)]

    print("res = ", list(filter(custom_filter, l1)))
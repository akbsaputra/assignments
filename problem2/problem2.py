# This py file is for Problem 2 of Homework #3 MPCS 51042
#
# AKBAR SAPUTRA
#
# This file contains a functions that will count all elements of lists

from functools import reduce

def count_all(*values):
    """
    This function takes in one or more lists (*values) and count all elements
    in those lists

    Inputs:
        *values (lists): any lists unpacked with * operator

    Output:
        An integer representing the number of all elements in all lists in input
    """
    output = reduce(lambda x, y: x + reduce(lambda a, b: a + 1, y, 0), values, 0)
    return output

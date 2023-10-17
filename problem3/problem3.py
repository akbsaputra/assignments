# This py file is for Problem 3 of Homework #3 MPCS 51042
#
# AKBAR SAPUTRA
#
# This file contains a functions that duplicate elements of a list

def duplicate_value(value, times, result):
    """
    This function is a helper function that takes value (element of 'values' in
    the main function) and duplicate it as many 'times', since using len or loop
    is prohibited

    Inputs:
        value (int): an integer as element of 'values' in the main function
        num (int): an integer representing the amount 'value' will be duplicated
            to
        result (tuple): a tuple that will accumulate to the tuple we want for
            the output

    Output:
        A tuple containing value duplicated 'times' times
    """
    # If times > 0, create a tuple followed by the existing result (if any)
    # If times = 0, the function short-circuited and stopped, and result is returned
    return times and duplicate_value(value, times - 1, (value,) + result) or result

def duplicate(values, num):
    """
    This function takes in a list and an integer, and create a tuple containing
    each element in the list duplicated 'num' times.

    Inputs:
        values (list): a list of integer
        num (int): an integer representing the amount each element of 'values'
            will be duplicated to

    Output:
        A list of tuples containing each element in 'values' duplicated 'num'
        times
    """

    output = list(map(lambda x: duplicate_value(x, num, ()), values))
    return output

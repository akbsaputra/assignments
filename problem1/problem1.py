# This py file is for Problem 1 of Homework #3 MPCS 51042
#
# AKBAR SAPUTRA
#
# This file contains two functions that tests if certain values satisfy a function

def satisfy(func1, func2, values):
    """
    This function takes in two predicate functions (func1 and func2) and a list
    of integers (values), and tests whether each element of values satisfy both
    func1 and func2.

    Inputs:
        func1 (function): any predicate function
        func2 (function): any predicate function
        values (list): a list of integers

    Output:
        A list of two-element tuples. The first component of the tuple should be
        the integer from values and the second is True if both predicate functions
        return True and False otherwise.
    """
    output = list(map(lambda x: (x, func1(x) and func2(x)), values))
    return output

def satisfy_all(funcs, values):
    """
    This function takes a list of predicate functions (funcs) and a list
    of integers (values), and tests whether each element of values satisfy
    each function in funcs.

    Inputs:
        funcs (list): a list of functions
        values (list): a list of integers

    Output:
        A list of two-element tuples. The first component is an integer from
        values and the second is a list of the return values from calling each
        predicate function with the integer.
    """
    output = list(map(lambda x: (x, list(map(lambda f: f(x), funcs))), values))
    return output

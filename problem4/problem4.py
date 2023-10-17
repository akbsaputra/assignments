# This py file is for Problem 4 of Homework #3 MPCS 51042
#
# AKBAR SAPUTRA
#
# This file contains a functions that count all elements of lists

def calc(op, a, b):
    """
    This function performs a calculation of a specified operator between two
    operands

    Inputs:
        op (str): a string representing an operation of either +, -, *, / or %
        a: an operand
        b: an operand

    Output:
        A value as a result of an operation between 'a' and 'b'
    """
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "%": lambda x, y: x % y
    }

    return operations[op](a, b)
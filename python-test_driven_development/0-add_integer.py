#!/usr/bin/python3
"""Defines a function that adds two integers.

This module contains the add_integer function, which adds two
numbers together after validating and casting them appropriately.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int/float): The first number to add.
        b (int/float): The second number to add (default 98).

    Returns:
        int: The sum of a and b, both cast to integers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

#!/usr/bin/python3
"""Module that adds 2 integers.

This module defines a single function, add_integer, which adds
two numbers together after validating and casting them.
"""


def add_integer(a, b=98):
    """Add a and b.

    Return the sum of a and b as an integer."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

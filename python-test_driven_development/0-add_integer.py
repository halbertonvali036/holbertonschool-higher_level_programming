"""Module for add_integer function.

Provides a function add_integer that adds two numbers.
Numbers must be integers or floats (which are casted to int).
Returns the integer sum of a and b.
"""


def add_integer(a, b=98):
    """Adds two integers or floats after casting to int.

    Returns the integer sum of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

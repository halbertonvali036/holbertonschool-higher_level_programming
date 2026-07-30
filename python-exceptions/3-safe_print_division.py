#!/usr/bin/python3
"""Defines a function that divides two integers and prints the result."""


def safe_print_division(a, b):
    """Divide two integers and print the result inside a finally block.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        The result of the division, or None if division fails.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

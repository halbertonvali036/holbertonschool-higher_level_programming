#!/usr/bin/python3
"""Defines a function that safely prints an integer."""


def safe_print_integer(value):
    """Print an integer using '{:d}'.format().

    Args:
        value: The value to attempt to print as an integer.

    Returns:
        bool: True if value was printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

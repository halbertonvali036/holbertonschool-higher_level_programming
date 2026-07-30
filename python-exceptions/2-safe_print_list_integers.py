#!/usr/bin/python3
"""Defines a function that prints and counts integers in a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, printing only integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue

    print()
    return count

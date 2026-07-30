#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements divided by div.

    Args:
        matrix (list): list of lists of integers/floats
        div (int or float): number to divide by

    Returns:
        list: new matrix with values rounded to 2 decimals
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(all(isinstance(x, (int, float)) for x in row)
                    for row in matrix))):
        raise TypeError(error_msg)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]

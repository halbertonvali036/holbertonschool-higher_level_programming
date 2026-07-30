#!/usr/bin/python3
"""Module that divides all elements of a matrix.

This module defines a single function, matrix_divided, which
divides every element of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Return a new matrix with all elements divided by div,
    rounded to 2 decimal places."""
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_len = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix

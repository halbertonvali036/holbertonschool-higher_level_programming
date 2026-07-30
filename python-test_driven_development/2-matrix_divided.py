#!/usr/bin/python3
"""
Module matrix_divided
Contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix (list of lists): Matrix containing ints or floats.
        div (int/float): The number to divide the matrix by.

    Returns:
        list of lists: A new matrix containing the divided values.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If rows of matrix are not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(msg_type)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(msg_size)

    return [[round(val / div, 2) for val in row] for row in matrix]

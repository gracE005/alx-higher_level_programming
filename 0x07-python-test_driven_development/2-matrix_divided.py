#!/usr/bin/python3
"""
    A module that divides elements of a matrix
"""


def matrix_divided(matrix, div):
    """Denotes division of functions in a matrix"""

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(v, list) for v in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(v, (int, float)) for row in matrix for v in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for index, row in enumerate(matrix):
        if len(row) != len(matrix[index - 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda row: list(map(lambda v:
                                         round(v/div, 2), row)), matrix))

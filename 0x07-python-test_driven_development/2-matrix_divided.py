#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains method that divides all elements of a matrix and returns new matrix
Requires same size lists of ints or floats, and max two decimal places
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with dividends
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

#!/usr/bin/python3
"""
Module 1-square
Defines Square with private attribute size
"""


class Square:
    """
    class Square definition

    Args:
        size : size of a size in a square
    """
    def __init__(self, size):
        """
        Initializes aquare

        Attributes:
            size: size of a side of square
        """
        self.__size = size

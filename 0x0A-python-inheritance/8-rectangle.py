#!/usr/bin/python3
"""
Module 8-rectangle

Contains parent class BaseGeometry
with public instance method area and integer_validator

Contains subclass Rectangle
with instantioation of private attributes width and height, validated py parent
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init__self, width, height)
    """
    def __init__(self, width, height):
        """validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        super().integer_validatior("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
"""
    module contains a class with a private instance size
"""


class Square:
    """
       Square class
    """
    def __init__(self, size=0):
        """Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square"""
        return self.__size ** 2

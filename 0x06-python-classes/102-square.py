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
        self.size = size

    def area(self):
        """Area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __eq__(self, other):
        """Overload equal operator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Overload not equal operator."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Overload greater than operator."""
        return self.area() > other.area()

    def __lt__(self, other):
        """Overload less than operator."""
        return self.area() < other.area()

    def __ge__(self, other):
        """Overload greater than or equal operator."""
        return self.area() >= other.area()

    def __le__(self, other):
        """Overload less than or equal operator."""
        return self.area() <= other.area()

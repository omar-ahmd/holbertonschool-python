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

    def my_print(self):
        """Draw square"""
        if self.__size == 0:
            print()
            return
        else:
            for x in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()

#!/usr/bin/python3
"""
    module contains a class with a private instance size
"""


class Square:
    """
       Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.size = size
        self.position = position

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
        """Draw the square"""
        if self.size == 0:
            print()
            return
        for row in range(self.position[1]):
            print()
        for x in range(self.size):
            for space in range(self.position[0]):
                print(" ", end="")
            for i in range(self.size):
                print("#", end="")
            print()

    @property
    def position(self):
        """Retrieving the position of Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

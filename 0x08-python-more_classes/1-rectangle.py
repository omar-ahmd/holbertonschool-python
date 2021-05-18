#!/usr/bin/python3
"""
This module contains a rectangle class
"""


class Rectangle:
    """
       Rectangle class
    """
    def __init__(self, width=0, height=0):
        """Initialize the rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width value"""
        return self.__width

    @width.setter
    def width(self, width):
        """set the width value"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Get the height value"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the height value"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

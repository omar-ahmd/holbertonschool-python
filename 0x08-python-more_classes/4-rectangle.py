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

    def area(self):
        """"Calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Print the rectangle using #"""
        if self.__height == 0 or self.__width == 0:
            return("")
        else:
            rect = ""
            for x in range(self.__height):
                for y in range(self.__width):
                    rect += "#"
                rect += "\n"
        return(rect[:-1])

    def __repr__(self):
        """repr of rectangle"""
        if self.__height == 0 or self.__height == 0:
            return("")
        else:
            return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

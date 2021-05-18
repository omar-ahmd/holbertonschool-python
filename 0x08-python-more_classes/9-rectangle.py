#!/usr/bin/python3
"""
This module contains a rectangle class
"""


class Rectangle:
    """
       Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    rect += str(self.print_symbol)
                rect += "\n"
        return(rect[:-1])

    def __repr__(self):
        """repr of rectangle"""
        if self.__height == 0 or self.__height == 0:
            return("")
        else:
            return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Delete the rectangle instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Compare area of 2 rectrangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Return rectangle instance with equal height and width"""
        return Rectangle(size, size)

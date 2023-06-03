#!/usr/bin/python3
"""
    A module that constitutes a single class of a rectangle(5)
"""


class Rectangle:
    """Defines a reactangle"""

    def __init__(self, width=0, height=0):
        """Initializing of instance data"""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def __str__(self):
        """Prints rectangle using `#` character"""
        string = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                string.append("#")
            if i < (self.__height - 1):
                string.append("\n")
        return "".join(string)

    def __repr__(self):
        """Prints string representation of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a string when instane being deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Recovers the value of `width`"""
        return self.__width

    @property
    def height(self):
        """Recovers the value of `height`"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets new value to the value of atribute `width`"""
        if not isinstance(value, (int, float)):
            raise TypeError("width must be a definite integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value of atribute `height` to new value"""
        if not isinstance(value, (int, float)):
            raise TypeError("height must be a positive integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area value of a reactangle"""
        return (self.__width * self.__height)

    def periphery(self):
        """Computes the periphery of a reactangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

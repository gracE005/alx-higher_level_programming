#!/usr/bin/python3
"""
    A module that consisits of a single class of a rectangle
"""


class Rectangle:
    """Represents a reactangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Prints rectangle using `print_symbol` character"""
        string = []
        if self.__width == 0 or self.__height == 0:
            return ""

        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)
        for i in range(self.__height):
            for j in range(self.__width):
                string.append(self.print_symbol)
            if i < (self.__height - 1):
                string.append("\n")
        return "".join(string)

    def __repr__(self):
        """Prints string representation of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a string when instane being deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Restores the value of `width`"""
        return self.__width

    @property
    def height(self):
        """Restores the value of `height`"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the attribute `width` value to a new value"""
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the attribute `height` value to a new value"""
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of a reactangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes the perimeter of a reactangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

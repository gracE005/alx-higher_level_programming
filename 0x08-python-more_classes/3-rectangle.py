#!/usr/bin/python3
"""
    A module that constitutes a single class
"""


class Rectangle:
    """constitutes a rectangle"""

    def __init__(self, width=0, height=0):
        """Program  a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def circumference(self):
        """Return the circumference of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

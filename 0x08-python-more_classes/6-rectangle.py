#!/usr/bin/python3
"""
    A module that consists of a single class of a rectangle
"""


class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_input(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_input(value)
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ['#' * self.__width + '\n'] * self.__height
        return ''.join(rect)

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def __validate_input(value):
        if not isinstance(value, int):
            raise TypeError("width/height must be an integer")
        if value < 0:
            raise ValueError("width/height must be >= 0")

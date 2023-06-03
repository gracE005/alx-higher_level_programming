#!/usr/bin/python3
"""
A module that contains a single class
"""

class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = self._validate_dimension(width, "width")
        self._height = self._validate_dimension(height, "height")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = self._validate_dimension(value, "width")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = self._validate_dimension(value, "height")

    def _validate_dimension(self, value, dimension_name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{dimension_name} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension_name} must be >= 0")
        return value

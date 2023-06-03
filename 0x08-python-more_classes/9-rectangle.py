#!/usr/bin/python3
"""
    A module that contains a single class of a rectangle
"""


class Rectangle():
    """
    A rectangle class
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructor of the class Rectangle
          Args:
            - width (default = 0): int
            - heigth (default = 0): int
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculate the area of a Rectangle"""
        return self.__width * self.__height

    def periphery(self):
        """Get the periphery of a Rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Function to print a Square with the print_symbol
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        final = [str(self.print_symbol) * self.__width
                 for character in range(self.__height)]

        return '\n'.join(final)

    def __repr__(self):
        """Returns an “official” string representation of a Rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted"""
        print('rectangle deleted...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        The property width Getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The property value Getter
          Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        The property height Getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The property value Getter
          Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area
          Args:
            - rect_1: Rectangle
            - rect_2: Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

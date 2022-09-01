#!/usr/bin/python3
""" 1-rectangle.py - Rectangle"""


class Rectangle:
    """
    class rectangle
    """
    def __init__(self, width=0, height=0):
        """
        instance initialization
        Args:
            width: of a rectangle
            height: of a rectangle
        """
        if (isinstance(width, int)):
            if width < 0:
                raise ValueError('width must be >= 0')
            self.__width = width
        else:
            raise TypeError('width must be an integer')

        if (isinstance(height, int)):
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = height
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        """
        getter for widht attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter
        """
        return self.__height

    def height(self, value):
        """
        setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__height = value

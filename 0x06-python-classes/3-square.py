#!/usr/bin/python3
""" 1-square.py - Square """


class Square:
    """ square class private size """
    def __init__(self, size=0):
        """ private size
        Args:
        size: accept a value
        """
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Return:
            the area of a square
        """
        return self.__size ** 2

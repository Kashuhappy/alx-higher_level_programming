#!/usr/bin/python3
""" create a square with size """


class Square:
    """ Square class
        Attributes:
        size (int): size of square
    """
    def __init___(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        A = self.__size * self.__size
        return (A)

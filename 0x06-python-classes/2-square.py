#!/usr/bin/python3
"""defines a square"""


class Size:
    """Square Class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise Valueerror("Size must be >= 0")
        else:
            self.__size = size

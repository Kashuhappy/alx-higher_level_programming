#!/usr/bin/python3
""" creates class square """


class Square:
    """ Square Class """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise Valueerror("size must be >= 0")
        else:
            self.__size = size

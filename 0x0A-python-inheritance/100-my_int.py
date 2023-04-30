#!/usr/bin/python3
"""Module contains MyInt class that inherits from int class"""


class MyInt(int):
    """class inherits from int class"""
    def __eq__(self, other):
        """equal method reversed"""
        return self - other != 0

    def __ne__(self, other):
        """not equaal method reversed"""
        return self - other == 0

#!/usr/bin/python3
"""
Module contains a function to check is object inherits from a class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if `obj` is the same class or inherit from `a_class`
    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object
    Returns:
        `True` if the object is an instanc otherwise `False'
    """

    return isinstance(obj, a_class)

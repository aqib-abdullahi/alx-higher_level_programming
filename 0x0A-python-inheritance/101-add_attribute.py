#!/usr/bin/python3
"""function that adds a new attribute to an object if possible"""


def add_attribute(obj, a, v):
    """adds attribute to an object if possible"""
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")

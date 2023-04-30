#!/usr/bin/python3
"""
Module contains a function that retunrs a value 
if object is an instance of a class that inherited from
a specified class
"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False

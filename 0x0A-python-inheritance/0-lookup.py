#!/usr/bin/python3
"""
Module has a function that returns list of available methods
"""
def lookup(obj):
    """
    Returns list of available  attributes and methods of an object
    """

    return dir(obj)

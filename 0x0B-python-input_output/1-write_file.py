#!/usr/bin/python3
"""
Contains the function "wrtie_file"
"""
def write_file(filename="", text=""):
    """returns number of characters written"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)

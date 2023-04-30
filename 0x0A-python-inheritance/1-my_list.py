#!/usr/bin/python3
"""Modiuule prints a list in ascneding order
"""


class Mylist(list):
    """A class to customize the list class
       and prints the list with a method"""

    def print_sorted(self):
        """
        Prints a list in ascending order
        and sort a list and then print on the output
        """

        if issubclass(Mylist, list):
            print(sorted(self))

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Printing the result of the addition of all arguments"""
    if len(sys.argv) == 1:
        print(0)
    elif len(sys.argv) == 2:
        print("{}".format(sys.argv[1]))
    elif len(sys.argv) > 2:
        i = 1
        a = 0
        while i < len(sys.argv):
            a = a + int(sys.argv[i])
            i = i + 1
        print(a)

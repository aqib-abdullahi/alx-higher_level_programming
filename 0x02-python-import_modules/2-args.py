#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """ printing number of and the list of its arguments"""

if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]) )
elif len(sys.argv) > 2:
    print("{} arguments:".format(len(sys.argv) - 1))
    i = 1
    while i < len(sys.argv):
        print("{}: {}".format(i, sys.argv[i]))
        i = i + 1
    

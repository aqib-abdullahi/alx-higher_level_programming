#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        l = 0
        k = len(matrix) - 1
        for r in range(len(matrix[i])):
            j = len(matrix[i])
            if l ==  k:
                print("{:d}".format(matrix[i][r]), end = '')
            elif l < k:
                print("{:d}".format(matrix[i][r]), end = ' ')
            l += 1
        print()

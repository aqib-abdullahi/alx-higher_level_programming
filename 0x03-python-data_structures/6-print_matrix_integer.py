#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for r in range(len(matrix[i])):
            print("{}".format(matrix[i][r]), end = " ")
        print()

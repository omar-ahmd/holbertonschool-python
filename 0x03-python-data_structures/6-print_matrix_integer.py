#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print("{:d} ".format(element) if element != row[-1] else "{:d}".format(element), end="")
        print()

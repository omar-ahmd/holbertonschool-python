#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element != row[-1]:
                out = "{:d} ".format(element)
            else:
                out = "{:d}".format(element)
            print(out, end="")
        print()

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for value in row:
                if value == row[0]:
                    print("{:d}".format(value), end="")
                else:
                    print(" {:d}".format(value), end="")
            print()
    else:
        print()

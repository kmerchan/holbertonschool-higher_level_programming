#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[1]] * len(matrix)
    row_index = 0
    for row in matrix:
        new_matrix[row_index] = [x**2 for x in row]
        row_index += 1
    return(new_matrix)

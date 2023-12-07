#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_new_matrix = []
    for i in range(len(matrix)):
        my_new_matrix += list(map(lambda x: x ** 2, matrix[i]))
    return my_new_matrix

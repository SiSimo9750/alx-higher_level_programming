#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_elemnt = list(map(lambda x: x ** 2, matrix[i]))
        new_matrix = new_matrix + new_elemnt
    return new_matrix

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        matrix = []
    sqrdm = list(map(lambda row: list(map(lambda j: (j**2), row)), matrix))
    return sqrdm

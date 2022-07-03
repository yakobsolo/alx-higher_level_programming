#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        row = []
        for x in i:
            row.append(x**2)
        res.append(row)
    return res

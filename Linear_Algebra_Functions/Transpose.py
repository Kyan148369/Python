from Input_Matrix import *


def transpose(matrix):
    matrix_transpose = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        matrix_transpose.append(row)
    print(matrix_transpose)

# calling the func


matrix = inputmatrix(rows, cols)
transpose(matrix)

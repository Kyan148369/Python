from Input_Matrix import *
from Matrix_Addition import *
from Determinant import *


def eigenvalues(matrix):
    a = 2


def identity_matrix(n):
    idmatrix = []
    for i in range(n):
        rowidmatrix = []
        for j in range(n):
            if (i == j):
                a = 1
            else:
                a = 0
            rowidmatrix.append(a)
        idmatrix.append(rowidmatrix)
    return idmatrix


matrix = inputmatrix(rows, cols)
n = 2

eigenvalues(matrix)

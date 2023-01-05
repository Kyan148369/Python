from Input_Matrix import *
from Matrix_Addition import *
from Determinant import *

# Tried to implement it but not too sure how to solve for unknown polynomials in 3x3 and above since it would essentially be solving
# roots of characteristic equation and not sure how to go about getting those variables in python


def eigenvalues(matrix):
    n = rows
    # Subtract identity matrix from matrix, multiplied by v
    lambdamatrix = [
        [matrix[i][j] - v*identity_matrix(n)[i][j] for j in range(n)] for i in range(n)]
    # Find determinant of lambdamatrix
    det = Determinant(lambdamatrix)
    # The roots of the determinant polynomial are the eigenvalues of the original matrix
    eigenvalues = [i for i in range(det+1) if det % i == 0]
    return eigenvalues


def identity_matrix(n):
    idmatrix = []
    for i in range(n):
        rowidmatrix = []
        for j in range(n):
            if i == j:
                a = 1
            else:
                a = 0
            rowidmatrix.append(a)
        idmatrix.append(rowidmatrix)
    return idmatrix


# Take input for rows and cols
rows = int(input('Enter number of rows for matrix: '))
cols = int(input('Enter number of cols for matrix: '))

# Input matrix
matrix = inputmatrix(rows, cols)

# Define v and assign value
v = 1

# Find eigenvalues of matrix
output = eigenvalues(matrix)

# Print output
print(output)

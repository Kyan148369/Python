from Input_Matrix import *

# input rows and column for matrix 1
# rows = int(input('Enter rows of 1st matrix to multiply:'))
# cols = int(input('Enter column of 1st matrix to multiply:'))

# input rows and column for matrix 2
rows2 = int(input('Enter rows of 2nd matrix to multiply:'))
cols2 = int(input('Enter column of 2nd matrix to multiply:'))

# condition for checking if matrices are multiplicable if not throws an else statement saying they aren't
if (((rows == rows2) and (cols == cols2)) or (cols == rows2)):
    # calling function to create the respective matrices
    matrix1 = inputmatrix(rows, cols)
    matrix2 = inputmatrix(rows2, cols2)
# function to multiply both the matrices

    def MatrixMultiplication(matrix1, matrix2):
        # initiliaze new matrix that we obtain after multiplying
        matrixmult = []
        # loop that initializes a particular row of the mult matrix and appends to it to the matrix mult at the bottom of the loop with the append statement
        for i in range(0, rows):
            rcmult = []
            # loop for iterating through and appending each element of a to the multiplied matrices respective row
            for j in range(0, cols2):
                a = 0
            # loop for adding all the elements for a particular element of the new matrix
                for k in range(0, cols):
                    a += (matrix1[i][k] * matrix2[k][j])
                rcmult.append(a)
            matrixmult.append(rcmult)
        return matrixmult

    MatrixMult = MatrixMultiplication(matrix1, matrix2)
    # to print the answer
    print(MatrixMult)

else:
    print("matrices are not compatible for multiplication please input new values")

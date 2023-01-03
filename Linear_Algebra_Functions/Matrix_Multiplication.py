from Input_Matrix import *

# input rows and column for matrix 1
rows1 = int(input('Enter rows of 1st matrix to multiply:'))
cols1 = int(input('Enter column of 1st matrix to multiply:'))

# input rows and column for matrix 2
rows2 = int(input('Enter rows of 2nd matrix to multiply:'))
cols2 = int(input('Enter column of 2nd matrix to multiply:'))

# condition for checking if matrices are multiplicable if not throws an else statement saying they aren't
if (((rows1 == rows2) and (cols1 == cols2)) or (cols1 == rows2)):
    # calling function to create the respective matrices
    matrix1 = inputmatrix(rows1, cols1)
    matrix2 = inputmatrix(rows2, cols2)
# function to multiply both the matrices

    def MatrixMultiplication(matrix1, matrix2):
        # initiliaze new matrix that we obtain after multiplying
        matrixmult = []
        # loop that initializes a particular row of the mult matrix and appends to it to the matrix mult at the bottom of the loop with the append statement
        for i in range(0, rows1):
            rcmult = []
            # loop for iterating through and appending each element of a to the multiplied matrices respective row
            for j in range(0, cols2):
                a = 0
            # loop for adding all the elements for a particular element of the new matrix
                for k in range(0, cols1):
                    a += (matrix1[i][k] * matrix2[k][j])
                rcmult.append(a)
            matrixmult.append(rcmult)
        return matrixmult

    MatrixMult = MatrixMultiplication(matrix1, matrix2)
    # to print the answer
    print(MatrixMult)

else:
    print("matrices are not compatible for multiplication please input new values")

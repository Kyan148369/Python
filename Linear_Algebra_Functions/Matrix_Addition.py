from Input_Matrix import *

rows2 = int(input('Enter number of rows for 2nd matrix to Add:'))
cols2 = int(input('Enter number of cols for 2nd matrix to Add:'))

matrix1 = inputmatrix(rows, cols)
matrix2 = inputmatrix(rows2, cols2)
# checking if its compatible to add both the matrices
if ((rows == rows2) and (cols == cols2)):
    def Matrix_Addition(matrix1, matrix2):
        # initalizing addition matrix
        matrix_add = []
        for i in range(rows):
            # initializing row of the addition matrix
            rmaddition = []
            for j in range(cols):
                a = matrix1[i][j]+matrix2[i][j]
                rmaddition.append(a)
            matrix_add.append(rmaddition)
        return matrix_add
else:
    print('not possible to add both the matrices')


output = Matrix_Addition(matrix1, matrix2)
print(output)

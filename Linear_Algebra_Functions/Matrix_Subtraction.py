from Input_Matrix import *

rows2 = int(input('Enter number of rows for 2nd matrix to Subtract:'))
cols2 = int(input('Enter number of cols for 2nd matrix to Subtract:'))

matrix1 = inputmatrix(rows, cols)
matrix2 = inputmatrix(rows2, cols2)
if ((rows == rows2) and (cols == cols2)):
    def Matrix_Subtraction(matrix1, matrix2):
        matrix_sub = []
        for i in range(rows):
            rmsubtraction = []
            for j in range(cols):
                a = matrix1[i][j]-matrix2[i][j]
                rmsubtraction.append(a)
            matrix_sub.append(rmsubtraction)
        return matrix_sub

else:
    print('not possible to subtract both the matrices')

output = Matrix_Subtraction(matrix1, matrix2)
print(output)

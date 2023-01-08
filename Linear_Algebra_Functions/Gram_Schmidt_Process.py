from Input_Matrix import *
from Transpose import transpose

# Pseudocode will prolly help to transfer it in code
# basically u1 = v1
# u2 = v2 - <v2,u1>/u1^2 * u1(make dot product function for this probably)
# u3 = v3 - <v3,u1>/u1^2* u1 - <v3,u2>/u^2


def Gram_Schmidt_Process(matrix):
    if rows != cols:

        if rows == 1:
            return matrix
        else:
            Ortho_matrix = []
            matrixT = transpose(matrix)
            for i in range(0, cols):
                Ortho_rowmatrix = []
                for j in range(0, cols):
                    t = matrix[i]
                    for k in range(0, i):
                        v += v(i) - ((matrix[j][i] * Ortho_matrix[k][i]) /
                                     Ortho_matrix[j][i]*Ortho_matrix[j][i]) * matrix[i][j]
                    Ortho_rowmatrix.append(v)
                Ortho_matrix.append(Ortho_rowmatrix)
    # Now to normalize each column vector of an orthogonal basis
                GSP_Matrix = []
                a = 0
                b = 0
            for i in range(0, cols):
                GSP_rowmatrix = []
                for j in range(0, rows):
                    b = (Ortho_matrix[j][i] / a)
                    for k in range(0, rows):
                        a += (Ortho_matrix[k][i]) ^ 2
                GSP_rowmatrix.append(b)
            GSP_Matrix.append(GSP_rowmatrix)
        return GSP_Matrix

    else:
        print('Cant apply Gram Schmidt Process for non square matricfes')


matrix = inputmatrix(rows, cols)
Gram_Schmidt_Process(matrix)

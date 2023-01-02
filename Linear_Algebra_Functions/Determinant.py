from Input_Matrix import *
# now calculating determinant function of the matrix we know that
#         Det = ((-1) ^(i+j)) * matrix[i] [j] * cofactor[i][j]

# defining function for determinant with argument being a matrix


def determinant(matrix):
    # if its an empty list or not a square matrix determinant is not defined so we throw a check here for that
    if (len(matrix) > 0 and (len(matrix) == len(matrix[0]))):
        # Initialize the determinant value
        determinant = 0
        # making conditional for when its just a 1x1 matrix 0,0 here since counting starts from 0 in computers
        if (len(matrix) == 1):
            print('determinant is:')
            determinant = matrix[0][0]
            return determinant
        # another conditional for 2x2 matrix
        elif (len(matrix) == 2):
            determinant = (matrix[0][0] * matrix[1][1] -
                           matrix[0][1] * matrix[1][0])
            return determinant
        # for 3x3 and above till an nxn matrix
        else:
            # Loop over the elements of the first row
            for i in range(0, len(matrix)):
                # Update the determinant till n
                determinant += (((-1) ** (i)) * (matrix[0][i])
                                * cofactor(matrix, i))
            print('Determinant is:')
            return determinant
        # this was the else for the conditional if length was 0 or not a square matrix
    else:
        print('Determinant does not exist')

# defining cofactor helper function for the determinant takes matrix, i and j too but for Det only first row so [0][i]


def cofactor(matrix, i):
    # initiliazing the cofactor list
    # for the loop start from the inner loop then proceed up
    matrix_cofactor = []
    for k in range(0, len(matrix)):
        if (k != 0):
            corows = []
            # iterating over the loop for length of matrix and the ifs inside the loop skip that element cause cofactors
            # are everything except that row and column so we resize the determinant in a new list by appending elements esentially,
            # then we recursively call the determinant of the cofactor till we obtain its final value
            for l in range(0, len(matrix)):
                if (l != i):
                    corows.append(matrix[k][l])
            matrix_cofactor.append(corows)
    return determinant(matrix_cofactor)


# calling inputmatrix from Input_Matrix to get the matrix from the user
# we can hardcode it too and simply remove the inputmatrix too if need be
# matrix = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [3, 4, 5, 8]]

matrix = inputmatrix(rows, cols)
# printing the value of the Determinant
print(determinant(matrix))

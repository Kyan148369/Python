
matrix = [[1,2,3],[2,3,4],[3,4,5]]

#for det we can compute by breaking it down into 2x2 matrix and then computing the base case
#from list we have to remove the first 
# now calculating determinant function of the matrix we know that
# for i in range(0, rows):
#     for j in range(0, cols):
#         Det = ((-1) ^(i+j)) * matrix[i] [j] * cofactor[i][j]


def cofactor(matrix):
    matrix_cofactor = []
    for i in range (1,len(matrix[0])):
        corows = []
        for j in range (1,len(matrix)):
            corows.append(matrix[i][j])
        matrix_cofactor.append(corows)
    print (matrix_cofactor)

cofactor(matrix)
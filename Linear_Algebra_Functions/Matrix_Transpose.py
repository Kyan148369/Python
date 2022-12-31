# wanna try to implement calculating determinants of a matrix
# first gotta take matrix input
# take user input for size of matrix
# using 2 nested loops to get a variable size matrix

# just tested out stuff here
a = 1
test = [[a, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3
for i in range(0, n):
    print(test)
for i in range(0, n):
    print(test[i])


print('Please enter number of rows and columns in desired matrix')
rows = int(input('Enter number of rows:'))
cols = int(input('Enter number of cols:'))


# function that takes rows and cols as parameters and accordingly creates a squarematrix if they are equal
# subtract the row and matrix number from diagonal

if (rows == cols):
    print('square matrix')
else:
    print('not a square matrix')


# function that takes rows and cols as parameters and accordingly creates a matrix


def inputmatrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(int(input('Enter a value: ')))
        matrix.append(row)
    print(matrix)
    return matrix
    # calling the func


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
print('Do you want me to take transpose of above matrix if yes enter 1 else enter any number')

if (int(input('Enter value: ')) == 1):
    transpose(matrix)
else:
    print('alright')

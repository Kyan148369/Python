print('Please enter number of rows and columns in desired matrix')
rows = int(input('Enter number of rows:'))
cols = int(input('Enter number of cols:'))
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

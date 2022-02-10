#

import rotate_matrix  # neened if use rotate matrix .clockwise function
column_size = int(input("Enter size of column: "))
row_size = int(input("Enter size of row: "))

# Declaring an empty 1D array.
matrix = []
# Declaring an empty 1D array.
b = []
# Initialize the Matrix with serise number (sorted).

Count = 0
for i in range(row_size):
    b = []
    for j in range(column_size):
        Count += 1
        b.append(Count)

    matrix.append(b)
# use rotate_matrix module to rotate the matrix
# print(rotate_matrix.clockwise(matrix))

# firs step to rotate matrix is Transpose the matrix
for i in range(row_size):
    for j in range(i, column_size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# the second step is reverse each raw in matrix
n = column_size//2
for i in range(row_size):
    for j in range(n):
        matrix[i][j], matrix[i][column_size-1 -
                                j] = matrix[i][column_size-1-j], matrix[i][j]
print(matrix)

# the other wat to Reverse each row using built in function
# for i in range(row_size):
#     matrix[i].reverse()

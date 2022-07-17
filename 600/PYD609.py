def input_matrix():
    matrix = [[], []]
    for i in range(2):
        for j in range(2):
            print("[%d, %d]: " % (i + 1, j + 1), end='')
            matrix[i].append(int(input()))
    return matrix


def print_matrix(matrix):
    for i in range(2):
        for j in range(2):
            print(f'{matrix[i][j]} ', end='')
        print()


print("Enter matrix 1:")
matrix1 = input_matrix()
print("Enter matrix 2:")
matrix2 = input_matrix()
print("Matrix 1:")
print_matrix(matrix1)
print("Matrix 2:")
print_matrix(matrix2)
print("Sum of 2 matrices:")
sum_of_matrix = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        sum_of_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
print_matrix(sum_of_matrix)

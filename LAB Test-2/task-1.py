def rotate_matrix(matrix):
    n = len(matrix)
    if n == 0 or n != len(matrix[0]):
        raise ValueError("Matrix must be non-empty and NxN.")

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix


n = int(input("Enter the size of the NxN matrix: "))
matrix = []

print(f"Enter the elements row by row ({n} numbers per row):")
for _ in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError("Each row must have exactly n elements.")
    matrix.append(row)

print(rotate_matrix(matrix))

def input(order):
    rows, cols = map(int, input(f"size of the matrix ({order}): ").split())
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"row {i} values: ").split()))
        if len(row) != cols:
            raise ValueError(f"invalid number of values. expected {cols} values for each row.")
        matrix.append(row)
    return matrix

def matrix_mult(matrix1, matrix2):
    m, n = len(matrix1), len(matrix1[0])
    p, q = len(matrix2), len(matrix2[0])
    if n != p:
        raise ValueError("number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    result = [[0 for _ in range(q)] for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

m1 = input("matrix 1")
m2 = input("matrix 2")
print("matrix 1:", m1)
print("matrix 2:", m2)

try:
    mult_result = matrix_mult(m1, m2)
    print("matrix multiplication:")
    for row in mult_result:
        print(row)
except ValueError as e:
    print("error:", e)

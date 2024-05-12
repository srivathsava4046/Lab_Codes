def matrix_multiply(A, B):
    # Check if the matrices can be multiplied
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are not compatible for multiplication")

    # Get the dimensions of the matrices
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B)

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication using dynamic programming
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example usage:
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]

result = matrix_multiply(A, B)
for row in result:
    print(row)
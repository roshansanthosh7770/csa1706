def add_matrices(matrix1, matrix2):
    if not matrix1 or not matrix2:
        raise ValueError("Both matrices must be non-empty.")
    if len(matrix1) != len(matrix2) or any(len(r1) != len(r2) for r1, r2 in zip(matrix1, matrix2)):
        raise ValueError("Matrices must have the same dimensions.")

    result = []
    for row1, row2 in zip(matrix1, matrix2):
        result.append([a + b for a, b in zip(row1, row2)])
    return result

def get_matrix_input(rows, cols, name="matrix"):
    print(f"Enter values for {name}:")
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i+1} values separated by space: ").split()
        if len(row) != cols:
            raise ValueError(f"Row must have {cols} values.")
        matrix.append([int(x) for x in row])
    return matrix

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    m1 = get_matrix_input(rows, cols, "Matrix 1")
    m2 = get_matrix_input(rows, cols, "Matrix 2")
    print("Sum of matrices:")
    result = add_matrices(m1, m2)
    for row in result:
        print(row)
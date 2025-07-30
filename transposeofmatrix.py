def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        raise ValueError("Matrix must be non-empty.")
    return [list(row) for row in zip(*matrix)]

def get_matrix_input(rows, cols):
    print("Enter matrix values:")
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
    m = get_matrix_input(rows, cols)
    print("Transposed matrix:")
    result = transpose_matrix(m)
    for row in result:
        print(row)
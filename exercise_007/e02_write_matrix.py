# Write Matrix Data to a File# Writing a matrix to a file (list of lists)

def write_matrix_to_file(matrix: list, filename: str):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(" ".join(map(str, row)) + "\n")

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
write_matrix_to_file(matrix, 'output_matrix.txt')

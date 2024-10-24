# Read Matrix Data from a File# Reading a matrix from a file (list of lists)

def read_matrix_from_file(filename: str) -> list:
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            matrix.append([int(num) for num in line.split()])
    return matrix

# Example usage
matrix = read_matrix_from_file('matrix.txt')
print("Matrix from file:", matrix)

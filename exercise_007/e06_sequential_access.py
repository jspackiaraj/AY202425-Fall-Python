# Sequential File Access# Sequentially reading lines from a file

def sequential_file_read(filename: str):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Example usage
sequential_file_read('example_file.txt')

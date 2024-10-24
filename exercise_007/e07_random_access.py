# Random File Access# Randomly accessing a specific line from a file

def random_access_file(filename: str, line_number: int):
    with open(filename, 'r') as file:
        for current_line_number, line in enumerate(file, start=1):
            if current_line_number == line_number:
                return line.strip()

# Example usage
print(random_access_file('example_file.txt', 3))

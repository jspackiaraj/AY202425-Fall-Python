# Append Data to a File# Appending data to a file

def append_data_to_file(data: str, filename: str):
    with open(filename, 'a') as file:
        file.write(data + "\n")

# Example usage
append_data_to_file("New data to append", 'data_file.txt')

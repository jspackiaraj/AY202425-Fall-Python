# Append Dictionary Data to a File# Appending dictionary data to a file

def append_dict_to_file(data: dict, filename: str):
    with open(filename, 'a') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

# Example usage
data = {"new_node": [400, 500]}
append_dict_to_file(data, 'node_data.txt')

# Binary File Write and Read# Writing and reading binary files

import pickle

def write_binary_data(data, filename: str):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def read_binary_data(filename: str):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Example usage
data = {"beam1": [100, 200], "beam2": [150, 300]}
write_binary_data(data, 'binary_data.dat')
print(read_binary_data('binary_data.dat'))

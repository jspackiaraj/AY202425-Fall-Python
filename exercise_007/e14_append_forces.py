# Append Beam Forces to a File
# Appending beam forces to a file

def append_forces_to_file(forces: list, filename: str):
    with open(filename, 'a') as file:
        for force in forces:
            file.write(str(force) + "\n")

# Example usage
new_forces = [350.5, 400.75]
append_forces_to_file(new_forces, 'forces.txt')

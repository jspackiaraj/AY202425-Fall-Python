# Write and Read List of Beam Forces# Writing and reading a list of beam forces to/from a file

def write_forces_to_file(forces: list, filename: str):
    with open(filename, 'w') as file:
        for force in forces:
            file.write(str(force) + "\n")

def read_forces_from_file(filename: str) -> list:
    with open(filename, 'r') as file:
        return [float(line.strip()) for line in file]

# Example usage
forces = [100.5, 200.75, 300.25]
write_forces_to_file(forces, 'forces.txt')
print(read_forces_from_file('forces.txt'))

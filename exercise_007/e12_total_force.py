# Calculate Total Force from a File# Calculating total force from a file with force values

def calculate_total_force(filename: str) -> float:
    total_force = 0
    with open(filename, 'r') as file:
        for line in file:
            total_force += float(line.strip())
    return total_force

# Example usage
print(calculate_total_force('force_data.txt'))

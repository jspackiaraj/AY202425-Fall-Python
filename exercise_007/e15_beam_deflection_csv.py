# Read and Write Beam Deflection Data
import csv

# Writing beam deflection data to a CSV file
def write_deflection_to_csv(data: list, filename: str):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Reading beam deflection data from a CSV file
def read_deflection_from_csv(filename: str) -> list:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [list(map(float, row)) for row in reader]

# Example usage
deflection_data = [[1, 0.5], [2, 0.75], [3, 1.0]]
write_deflection_to_csv(deflection_data, 'deflection.csv')
print(read_deflection_from_csv('deflection.csv'))


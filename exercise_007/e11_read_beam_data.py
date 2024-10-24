# Read Beam Data from a File# Reading beam data from a file

def read_beam_data(filename: str) -> dict:
    beam_data = {}
    with open(filename, 'r') as file:
        for line in file:
            beam_id, *values = line.split()
            beam_data[beam_id] = list(map(int, values))
    return beam_data

# Example usage
beam_data = read_beam_data('beam_data.txt')
print(beam_data)

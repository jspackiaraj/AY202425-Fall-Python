# Program: Vector Magnitude

import math

def vector_magnitude(vector):
    # Calculate the magnitude using the Euclidean formula
    return math.sqrt(sum(element**2 for element in vector))

# Example vector
vector = [3, 4]

# Calculating magnitude
result = vector_magnitude(vector)
print(f"Vector Magnitude: {result}")

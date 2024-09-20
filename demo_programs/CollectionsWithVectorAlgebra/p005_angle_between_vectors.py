# Program: Angle Between Two Vectors

import math

def dot_product(vector1, vector2):
    return sum(vector1[i] * vector2[i] for i in range(len(vector1)))

def vector_magnitude(vector):
    return math.sqrt(sum(element**2 for element in vector))

def angle_between_vectors(vector1, vector2):
    # Calculate the dot product and magnitudes of the vectors
    dot_prod = dot_product(vector1, vector2)
    magnitude1 = vector_magnitude(vector1)
    magnitude2 = vector_magnitude(vector2)
    
    # Calculate the angle in radians
    return math.acos(dot_prod / (magnitude1 * magnitude2))

# Example vectors
vector1 = [1, 0]
vector2 = [0, 1]

# Calculating angle
result = angle_between_vectors(vector1, vector2)
print(f"Angle Between Vectors (in radians): {result}")

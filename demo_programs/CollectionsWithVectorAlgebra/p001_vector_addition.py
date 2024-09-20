# Program: Vector Addition

def add_vectors(vector1, vector2):
    # Ensure both vectors have the same dimension
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    
    # Perform element-wise addition
    return [vector1[i] + vector2[i] for i in range(len(vector1))]

# Example vectors
vector1 = [2, 4, 6]
vector2 = [1, 3, 5]

# Adding vectors
result = add_vectors(vector1, vector2)
print(f"Vector Addition Result: {result}")

# Program: Dot Product of Two Vectors

def dot_product(vector1, vector2):
    # Ensure both vectors have the same dimension
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    
    # Perform the dot product
    return sum(vector1[i] * vector2[i] for i in range(len(vector1)))

# Example vectors
vector1 = [2, 3, 5]
vector2 = [4, -1, 2]

# Calculating dot product
result = dot_product(vector1, vector2)
print(f"Dot Product Result: {result}")

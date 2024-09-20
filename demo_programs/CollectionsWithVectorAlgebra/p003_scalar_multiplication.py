# Program: Scalar Multiplication

def scalar_multiply(scalar, vector):
    # Multiply each element of the vector by the scalar
    return [scalar * element for element in vector]

# Example scalar and vector
scalar = 3
vector = [1, -2, 4]

# Scalar multiplication
result = scalar_multiply(scalar, vector)
print(f"Scalar Multiplication Result: {result}")

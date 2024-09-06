# Quadratic Solver
import math

def solve_quadratic(coefficients):
    a, b, c = coefficients
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (real_part, imaginary_part), (real_part, -imaginary_part)

coefficients = (1, -3, 2)  # Example: x^2 - 3x + 2 = 0
roots = solve_quadratic(coefficients)
print("Roots:", roots)

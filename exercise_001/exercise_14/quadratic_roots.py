import math
# To find the square root, we have to use a special function named sqrt().
# Unlike print() function, which is part of the core, sqrt() lives in a 
# location named math, we have imported it into our program and are using it.
# In python, math is a module and we are making our program more powerful
# by using the same with little coding effort from us. There are many such 
# modules available and this is a great strength of python. 

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are {root1} and {root2}")
else:
    print("The equation has no real roots")

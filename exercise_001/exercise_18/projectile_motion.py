import math
# To find the sine or cosine value, we have to use a special function named sin() or cos() .
# Unlike print() function, which is part of the core, sin() lives in a 
# location named math, we have imported it into our program and are using it.
# The angles should always be in radians when passing values to the trigonometric 
# functions, so ensure that proper conversion is always done.
# In python, math is a module and we are making our program more powerful
# by using the same with little coding effort from us. There are many such 
# modules available and this is a great strength of python. 

velocity = float(input("Enter initial velocity (m/s): "))
angle = math.radians(float(input("Enter angle of projection (degrees): ")))

# Constants
g = 9.8

# Calculating maximum height
H = (velocity**2 * math.sin(angle)**2) / (2 * g)

# Calculating range
R = (velocity**2 * math.sin(2*angle)) / g

print(f"Maximum height is {H} meters")
print(f"Range is {R} meters")

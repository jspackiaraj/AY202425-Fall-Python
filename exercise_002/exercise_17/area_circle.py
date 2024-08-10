import math
# Pi is the ratio between the circumference and the radius of a circle.
# pi is defined as a constant (observe how () is not used when calling it) in the
# location named math, we have imported it into our program and are using it.
# In python, math is a module and we are making our program more powerful
# by using the same with little coding effort from us. There are many such 
# modules available and this is a great strength of python. 

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
print(f"The area of the circle is {area}")

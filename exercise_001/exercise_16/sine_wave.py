import math
# To find the square root, we have to use a special function named sqrt().
# Unlike print() function, which is part of the core, sqrt() lives in a 
# location named math, we have imported it into our program and are using it.
# In python, math is a module and we are making our program more powerful
# by using the same with little coding effort from us. There are many such 
# modules available and this is a great strength of python. 

for angle in range(0, 361, 10):
    sine_value = math.sin(math.radians(angle))
    print(f"sin({angle}) = {sine_value}")

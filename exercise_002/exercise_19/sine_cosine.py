import math
# To find the sine or cosine value, we have to use a special function named sin() or cos() .
# Unlike print() function, which is part of the core, sin() lives in a 
# location named math, we have imported it into our program and are using it.
# The angles should always be in radians when passing values to the trigonometric 
# functions, so ensure that proper conversion is always done. Observe, how we are using
# the built-in method radians() for the conversion.
# In python, math is a module and we are making our program more powerful
# by using the same with little coding effort from us. There are many such 
# modules available and this is a great strength of python. 

for angle in range(0, 361, 10):
    sine_value = math.sin(math.radians(angle))
    cosine_value = math.cos(math.radians(angle))
    print(f"sin({angle}) = {sine_value}, cos({angle}) = {cosine_value}")

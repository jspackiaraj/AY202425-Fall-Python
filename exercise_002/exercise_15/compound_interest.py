P = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (in decimal): "))
t = int(input("Enter time (in years): "))
n = int(input("Enter number of times interest applied per time period: "))

A = P * (1 + r/n)**(n*t)
print(f"Compound Interest after {t} years is {A}")

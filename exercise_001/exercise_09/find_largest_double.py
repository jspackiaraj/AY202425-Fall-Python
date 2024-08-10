# find_largest_double.py

num_entries = int(input("Enter the number of entries: "))
if num_entries <= 0:
    print("Number of entries must be positive.")
    exit()

largest = None

for _ in range(num_entries):
    try:
        number = float(input("Enter a number (int or float): "))
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if largest is not None:
    print(f"The largest number is: {largest}")
else:
    print("No valid numbers were entered.")

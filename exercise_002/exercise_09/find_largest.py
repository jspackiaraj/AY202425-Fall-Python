# find_largest.py

num_entries = int(input("Enter the number of entries: "))
if num_entries <= 0:
    print("Number of entries must be positive.")
    exit()

largest = None

for _ in range(num_entries):
    try:
        number = int(input("Enter an integer: "))
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter an integer.")

if largest is not None:
    print(f"The largest integer is: {largest}")
else:
    print("No valid numbers were entered.")

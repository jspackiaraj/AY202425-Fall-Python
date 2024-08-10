# find_largest_double_with_negatives.py

largest = None

while True:
    entry = input("Enter a number (int or float, or 'x' to exit): ").strip()
    if entry.lower() == 'x':
        break

    try:
        number = float(entry)
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter a valid number or 'x' to exit.")

if largest is not None:
    print(f"The largest number is: {largest}")
else:
    print("No valid numbers were entered.")

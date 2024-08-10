# find_largest_with_negatives.py

largest = None

while True:
    entry = input("Enter an integer (or 'x' to exit): ").strip()
    if entry.lower() == 'x':
        break

    try:
        number = int(entry)
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter an integer or 'x' to exit.")

if largest is not None:
    print(f"The largest integer is: {largest}")
else:
    print("No valid numbers were entered.")

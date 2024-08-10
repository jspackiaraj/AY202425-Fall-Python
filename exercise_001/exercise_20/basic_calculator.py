while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator...")
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")

        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")
            else:
                print("Error! Division by zero is not allowed.")
    else:
        print("Invalid Input")
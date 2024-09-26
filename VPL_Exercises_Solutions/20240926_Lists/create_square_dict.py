
def create_square_dict(numbers):
    return {number: number**2 for number in numbers}

if __name__ == '__main__':
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    result = create_square_dict(numbers)
    print(result)

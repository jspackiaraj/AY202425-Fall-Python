# e04_skip_negative_numbers.py
numbers = [10, -5, 3, -1, 9, -8]
for num in numbers:
    if num < 0:
        continue
    print(num)

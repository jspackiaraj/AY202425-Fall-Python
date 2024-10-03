# e05_prime_numbers_break.py
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if not is_prime and num > 30:
        break
    if is_prime:
        print(num)

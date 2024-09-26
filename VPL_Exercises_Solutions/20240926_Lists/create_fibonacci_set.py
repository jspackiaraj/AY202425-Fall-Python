
def create_fibonacci_set(n):
    fib_set = set()
    a, b = 0, 1
    for _ in range(n):
        fib_set.add(a)
        a, b = b, a + b
    return fib_set

if __name__ == '__main__':
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    result = create_fibonacci_set(n)
    print(result)

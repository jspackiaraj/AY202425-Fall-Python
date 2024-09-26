
def generate_even_set():
    return {x for x in range(1, 21) if x % 2 == 0}

if __name__ == '__main__':
    result = generate_even_set()
    print(result)

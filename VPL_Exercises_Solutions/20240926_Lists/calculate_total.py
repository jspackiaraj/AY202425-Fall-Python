
def calculate_total(cart, prices):
    total = 0
    for item in cart:
        total += prices.get(item, 0)
    return round(total, 2)

if __name__ == '__main__':
    cart = input("Enter the items in the cart separated by spaces: ").split()
    prices_input = input("Enter the prices as item:price pairs separated by spaces (e.g., apple:0.5): ").split()
    prices = {item.split(':')[0]: float(item.split(':')[1]) for item in prices_input}
    result = calculate_total(cart, prices)
    print(f"The total cost is: {result}")

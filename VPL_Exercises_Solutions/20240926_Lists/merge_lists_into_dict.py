
def merge_lists_into_dict(keys, values):
    return dict(zip(keys, values))

if __name__ == '__main__':
    keys = input("Enter the list of keys separated by spaces: ").split()
    values = list(map(int, input("Enter the list of values separated by spaces: ").split()))
    result = merge_lists_into_dict(keys, values)
    print(result)


def find_common_elements(list1, list2):
    return set(list1).intersection(set(list2))

if __name__ == '__main__':
    list1 = input("Enter the first list of numbers separated by spaces: ").split()
    list2 = input("Enter the second list of numbers separated by spaces: ").split()
    result = find_common_elements(list1, list2)
    print(result)

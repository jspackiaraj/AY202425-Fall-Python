
def find_union_intersection(set1, set2):
    return (set1.union(set2), set1.intersection(set2))

if __name__ == '__main__':
    set1 = set(input("Enter the first set of numbers separated by spaces: ").split())
    set2 = set(input("Enter the second set of numbers separated by spaces: ").split())
    result = find_union_intersection(set1, set2)
    print(f"Union: {result[0]}, Intersection: {result[1]}")

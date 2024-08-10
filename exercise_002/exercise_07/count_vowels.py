vowels = 'aeiouAEIOU'
string = input("Enter a string: ")
count = sum(1 for char in string if char in vowels)
print("Number of vowels in the string:", count)

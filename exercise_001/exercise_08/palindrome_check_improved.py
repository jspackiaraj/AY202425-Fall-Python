# palindrome_check_improved.py

string = input("Enter a string: ")
# Convert the string to lowercase
lowercase_string = string.lower()
# Check if the lowercase string is a palindrome
if lowercase_string == lowercase_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

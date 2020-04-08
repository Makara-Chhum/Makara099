"""
4. Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself.
"""
a = input("Input a string: ")
b = a[0]
string = a[1:].replace(b,'$')
print(b+string)



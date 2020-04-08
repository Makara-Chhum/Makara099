"""
10. Write a Python program to change a given string to a new string
where the first and last chars have been exchanged.
"""
str = input("Input a string: ")
a = str[-1:] + str[1:-1] + str[:1]
print(a)
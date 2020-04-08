"""
9. Write a Python program to remove the n index character from a a nonempty string.
"""
def remove_char(str, n):
    first_part = str[:n]
    Second_part = str[n+1:]
    return first_part + Second_part


str = input("Input a string: ")
print(remove_char(str, 5))
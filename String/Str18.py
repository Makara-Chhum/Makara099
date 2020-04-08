"""
18. Write a Python function to get a string made of its first three character
of a specified string. If the length of the string is less than 3 then return
the original string.
"""
def first_three(string):
    if len(string) >= 3:
        return string[:3]
    else:
        return string


print(first_three('Py'))
print(first_three('Thanks'))

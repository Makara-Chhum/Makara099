"""
6. Write a Python program to add 'ing' at the end of a given string(length should be at
least 3). if the given string already ends with 'ing' then add 'ly' instead. if the
length of the given string is less than 3, leave it unchanged.
"""
def text():
    str = input("Input a string: ")
    if len(str) >= 3 and str[-3:] != 'ing':
        return str+ 'ing'
    elif str[-3:] == 'ing':
        return str+ 'ly'
    else:
        return str

print(text())
print(text())
print(text())
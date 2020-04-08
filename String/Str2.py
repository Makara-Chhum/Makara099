"""
2. Write a Python program to count the number of characters(character frequency)
in a string.
"""
def char():
    str1 = input("Input a string: ")
    a = {}
    for i in str1:
        b = a.keys()
        if i in b:
            a[i] +=1
        else:
            a[i] = 1
    return a

print(char())



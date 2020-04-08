"""
11. Write a Python program to remove the characters which have odd
index values of a given string
"""
str = input("Input a string: ")
for i in range(len(str)):
    result = ""
    if i % 2 == 0:
        result = result + str[i]
        print(result)

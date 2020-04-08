"""
5. Write a Python program to get a single string from two given strings, separated by
a space and swap the first two characters of each string.
"""
string1 = input("Input a string1: ")
string2 = input("Input a string2: ")
a = string1[:2] + string2[2:]
b = string2[:2] + string1[2:]
print(a+' '+b)

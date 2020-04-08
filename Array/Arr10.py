"""
    10. Write a Python program to insert a new item before the second element in an existing array.
"""
from array import *
a = array('i', [1, 2, 3, 4, 5, 6, 7, 8, ])
print("Insert new value before second elements of a:")
print("Before insert :"+str(a))
a.insert(1, 9)
print("After insert :"+str(a))

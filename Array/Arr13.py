"""
    13. Write a Python program to convert an array to an ordinary list with
    the same items.
"""
from array import *
a = array('i',[1, 2, 3, 4, 5, 6])
b = a.tolist()
print(a)
print("Convert an array to list: "+str(b))
"""
    11. Write a Python program to remove a specified item using the index from an array.
"""
from array import *

a = array('i', [1, 2, 3, 4, 5, 6])
print("Original array: "+str(a))
print("Remove the third element from the array:")
a.pop(2)
print("After remove: "+str(a))

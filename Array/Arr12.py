"""
    12. Write a Python program to remove the first occurrence of a specified
    element from an array
"""
from array import *
a = array('i',[1, 5, 2, 3, 4, 5])
print("Original array: "+str(a))
print("Remove the first occurrennce of element from array:")
a.remove(5)
print("After remove: "+str(a))

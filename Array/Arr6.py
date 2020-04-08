"""
    6. Write a Python program to get the number of occurrences of a specified
    element in an array.
"""
from array import *

a = array('i', [1, 2, 3, 4, 3, 2, 3, 4, 3, 3])
print(a)
print("The number of occurrences 3 in array is "+str(a.count(3)))

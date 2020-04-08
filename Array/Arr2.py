#2.Write a Python program to append a new item to the end of the array.
from array import *

a = array('i', [2, 4, 6, 8])
print("First array: " + str(a))
a.append(10)
print("New array: " + str(a))

"""
    7. Write a Python program to append item from inerrable to the end of the array
"""
from array import *
a = array('i',[1, 2, 3, 4, 5, 6, 7])
print(a)
a.extend(a)
print("After append array: "+str(a))
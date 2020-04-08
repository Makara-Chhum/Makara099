"""
    8. Write a Python program to convert an array to an array of
    machine values and return the bytes representation
"""
from array import *

a = array('b', [72, 101, 108, 111, 32, 119, 111, 108, 100])
print("Convert an array to an array of machine values and return the bytes representattion:")
b = a.tobytes()
print(b)

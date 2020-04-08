#4. Write a Python to get the length in bytes of one array item in the internal representation
from array import *

a = array('i', [1, 2, 3, 4])
print("Original array: " + str(a))
print(("The length in bytes of one array: " + str(a.itemsize)))

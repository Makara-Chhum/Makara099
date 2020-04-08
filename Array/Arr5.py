"""
    5.Write a Python program to get the current memory address and the length in elements
    of the buffer used to hold an array? contents and also find the size of the memory buffer in bytes.  
"""
from array import *
a = array('i',[1,2,3,4,5,6,7])
print("The first array: "+str(a))
print("The current memory address and lenght of the buffer: "+str(a.buffer_info()))
print("The size of the memory buffer in bytes: "+str(a.itemsize))
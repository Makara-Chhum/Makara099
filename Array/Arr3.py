#3. Write a Python program to reverse th eorder of the items in te array.
from array import *
a = array('i', [1, 2, 3, 4, 5, 6])
print("Before reverse array: "+str(a))
res = a[::-1]
print("After reverse array: "+str(res))


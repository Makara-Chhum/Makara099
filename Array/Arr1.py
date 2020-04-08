"""
1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
"""
import array
a = array.array('i',[])
b = int(input("Input an array of 5 integers: "))
for i in range(b):
    c = int(input())
    a.append(c)
print(a)
for i in a:
    print(i)
# 13.Write a Python program to generate a 3*4*6 3D array whose each element is *

def funtion(row,cel,element):
    for n in range(row):
        array = cel * [element * ['*']]
        return array

print(funtion(3,4,6))
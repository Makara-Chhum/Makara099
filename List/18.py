# 18.Write a Python program to generate all permutations of a list in Python

from itertools import permutations
number_list = permutations([1,2,3])
for i in number_list:
    print(list(i))
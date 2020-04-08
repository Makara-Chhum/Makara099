# 23.Write a Python program to flatten a shallow list

from itertools import *

number_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
new_list = list(iter(chain(*number_list)))
print(new_list)

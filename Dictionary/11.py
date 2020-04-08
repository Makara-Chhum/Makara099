# 10.Write a Python program to sum all the items in a dictionary.
d = {'One': 2, 'Two': 4, 'Three': 3}
mul = 1
for i in d:
    mul = mul * d[i]
print(mul)

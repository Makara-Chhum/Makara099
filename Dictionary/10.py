# 10.Write a Python program to sum all the items in a dictionary.
d = {'One':6,'Two':2,'Three':3}
sum = 0
for i in d:
    sum += d[i]
print(sum)
# 17.Write a Python program to remove duplicates from Dictionary.

dict = {1, 1, 2, 3, 3, 4, 5, 6, 7}
d = []
for i in dict:
    if i not in d:
        d.append(i)
print(d)
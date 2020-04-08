# 13.Write a Python program to map two lists into a dictionary.
d = {}
key = ['one','two','three','four']
value = [1,2,3,4]
g = zip(key,value)
print(dict(g))
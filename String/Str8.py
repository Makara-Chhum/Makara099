"""
8. Write a Python function that take a list of words and returns the length
of the longest one.
"""
def function(b):
    a = list()
    for i in b:
        a.append((len(i),i))
    a.sort()
    return a[-1][1]




print(function(['Welcome', 'world', 'hi']))
"""
    15. Write a Python program to find the first duplicate element in a given array
    of integers. Return -1 if there are no such elements.
"""
def firstDuplicateSet(a):
    seen = set()
    for i in a:
        if i in seen:
            return i
        seen.add(i)

    return -1

print(firstDuplicateSet([1,3,43,3]))
print(firstDuplicateSet([1,1,1,2,31,3]))
print(firstDuplicateSet([1]))



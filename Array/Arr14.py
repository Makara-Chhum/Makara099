"""
    14. Write a Python program to find whether a given array of integers contains any duplicate element.
    Return true if any value appears at least twice in the said array
    and return false if every element is distinct.
"""
def duplicate(element):
    num_set = set(element)
    if len(element) == len(num_set):
        return False
    else:
        return True


print(duplicate([1]))
print(duplicate([1, 2, 3, 4, 5, 6, 7, 8]))
print(duplicate([1, 2, 1, 1, 2, 3, 1, 3]))

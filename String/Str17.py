"""
17. Write a Python function to get a string made of 4 copies of the last two characters
of a specified string (length must be at least 2)
"""
def insert_end():
    str = input("Input a string: ")
    sub_str = str[-2:]
    return sub_str*4

print(insert_end())
print(insert_end())
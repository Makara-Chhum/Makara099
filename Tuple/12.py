# 12.Write a Python program to remove an item from a tuple.
tuplex = (1, 2, 3, 4, 5, 'h', 'hi', 'hu')
tuplex = list(tuplex)
tuplex.pop(5)
print(tuple(tuplex))

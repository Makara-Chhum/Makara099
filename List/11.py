# 11.Write a Python function that takes two lists and returns True if they have at
# least one common member

def funtion(a, b):
    for i in a:
        for j in b:
            if i == j:
                return True
    return False


print(funtion([1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 10]))
print(funtion([1, 2, 3, 4, 5, 6], [11, 7, 8, 9, 10]))

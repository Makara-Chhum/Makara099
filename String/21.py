# 21.Write a Python function to convert a given string to all uppercase if it contains at least
# 2 uppercase characters in the first 4 characters.

def funtion(str1):
    n = 0
    for i in str1:
        if i.upper() == i:
            n += 1
    if n >= 2:
        return str1.upper()
    return str1

print(funtion('Python'))
print(funtion('PyThon'))
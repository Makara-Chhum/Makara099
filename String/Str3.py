"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given
a string. if the string length is less than 2, return instrad of the empty string.
"""
def string():
    a = input("Input a string: ")
    if len(a) >=2:
        return a[0]+a[1]+a[-2]+a[-1]
    else:
        return ""
print(string())
print(string())
print(string())

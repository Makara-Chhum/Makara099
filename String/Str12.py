"""
12. Write a Python program to count the occurrence of each
word in a given sentence.
"""
string = input("Input a string: ")
a = dict()
word = string.split()
for i in word:
    if i in a:
        a[i]+=1
    else:
        a[i] = 1

print(a)


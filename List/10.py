"""Write a Python program to find the list of words that are longer than n from a
given list of words """
a = ["hello", "Hi", "Welcome", "Beautiful", "Implementation"]
n = int(input("Input a number: "))
b = []
for i in a:
    if len(i) > n:
        b.append(i)
print(b)

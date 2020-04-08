# 4.Write a Python script to check whether a given key already exists in a dictionary.
i = int(input("Input a number: "))
d = {1:10,2:20,3:30,4:40}
if i in d:
    print("Key already exists in a dictionary")
else:
    print("Key hasn't exist in a dictionary")

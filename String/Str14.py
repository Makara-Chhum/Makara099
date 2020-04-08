"""
14. Write a Python program that accepts a comma separated sequence of words as
input and prints unique words in sorted form (alphanumerically)
"""
string = input("Input comma separated sequence of words: ")
words = [word for word in string.split(",")]
print(",".join(sorted(list(set(words)))))

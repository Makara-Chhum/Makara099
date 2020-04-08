'''Write a Python Progeam to count the number of string where the string length is 2 or
more and the first and the last character are same from a given list of strings. 
'''
list = ['abc', 'xyz', 'aba', '1221']
a = []
for i in list:
    if len(list) >2 and i[0] == i[-1]:
        a.append(i)
print(len(a))

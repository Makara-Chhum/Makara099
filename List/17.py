'''17.Write a Python program to generate and print a list except for the first 5
elements, where the values are square of numbers between 1 and 30 (both
included)'''

def funtion():
    number_list = list()
    for i in range(1,31):
        number_list.append(i**2)
    print(number_list[5:])

funtion()
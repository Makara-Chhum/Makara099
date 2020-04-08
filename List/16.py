'''16.Write a Python program to generate and print a list of first and last 5 elements
where the values are square of numbers between 1 and 30 (both included)'''

def funtion():
    num_list = list()
    for i in range(1,31):
        num_list.append(i**2)
    print(num_list[:5])
    print(num_list[-5:])


funtion()


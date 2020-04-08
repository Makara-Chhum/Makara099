# 16.Write a Python program to get a dictionary from an object's fields.

# class dictObj(object):
#     def __init__(self):
#         self.x = 'red'
#         self.y = 'Yellow'
#         self.z = 'Green'
#
#     def do_nothing(self):
#         pass
#
#
# test = dictObj()
# print(test.__dict__)

class object():
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def function(self):
        pass

r1 = object('Tom',20,'white')
print(r1.__dict__)
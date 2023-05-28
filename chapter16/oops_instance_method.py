# class Person:
#     def __init__(self, first_name, last_name, age): # init method is called whenever an object is created # self represents first object that is p1, p2, p3
#         # instance variable
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def full_name(self): # inside class it is mandatory to put self as a first argument if any function
#         return(f'{self.first_name} {self.last_name}')
#     def is_above_18(self):
#         return self.age>18
# p1 = Person('aditi', 'garg', 23)
# p2 = Person('arsh', 'deep', 25)
# print(p1.last_name)
# print(p2.full_name())  # = person.full_name(p2)
# print(p2.is_above_18())


l = [1,2,3,4]
# l.clear()
# or 
list.clear(l)
print(l)
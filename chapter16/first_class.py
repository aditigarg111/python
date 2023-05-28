# class are used to creaet our own object 
class Person:
    def __init__(self, first_name, last_name, age): # init method is called whenever an object is created # self represents first object that is p1, p2, p3
        # instance variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('aditi', 'garg', 23)
p2 = Person('arsh', 'deep', 25)
p3 = Person('avani','garg', 16)

print(p1.first_name)
print(p2.first_name)
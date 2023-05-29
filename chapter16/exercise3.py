class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age): # after the object is created constructor(init method) is called
        Person.count_instance += 1 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('aditi', 'garg', 23)
p2 = Person('arsh', 'deep', 25)
p3 = Person('avani','garg', 16)

print(Person.count_instance)
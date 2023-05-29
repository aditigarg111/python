class Person:
    count_instance = 0 # CLASS VARIABLE
    def __init__(self, first_name, last_name, age): # after the object is created constructor(init method) is called
        Person.count_instance += 1 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    def full_name(self): # INSTANCE METHOD inside class it is mandatory to put self as a first argument if any function
        return(f'{self.first_name} {self.last_name}')
    def is_above_18(self): # INSTANCE METHOD 
        return self.age>18
    
p1 = Person('aditi', 'garg', 23)
p2 = Person('arsh', 'deep', 25)
p3 = Person('avani','garg', 16)
p4 = Person.from_string('khushi,pandey,25')
print(p3.full_name())
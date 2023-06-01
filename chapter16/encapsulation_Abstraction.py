# Encapsulation - when you create a class, it means you are implementing encapsulation. 
# A class is an example of encapsulation as it binds all the data members (instance variables) and methods into a single unit.

# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self.price = price

#     def make_a_call(self, phone_number):
#         print(f'this is the number{phone_number}')

#     def full_name(self):
#         return f'{self.brand} {self.model_name}'
# p1 = Phone('apple', 'iPhone14',150000)
# print(p1.price)
    
# l = [1,2,9,7,3,5]
# l.sort() #--------------- Abstraction
# print(l)

#------------------------------------------------------------------- _name - convention for private names
# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = price    # private variable 

#     def make_a_call(self, phone_number):
#         print(f'this is the number{phone_number}')

#     def full_name(self):
#         return f'{self.brand} {self.model_name}'
# p1 = Phone('apple', 'iPhone14',150000)
# print(p1._price)

# --------------------------------------------------------------------name mangling

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price    # private variable 

    def make_a_call(self, phone_number):
        print(f'this is the number{phone_number}')

    def full_name(self):
        return f'{self.brand} {self.model_name}'
p1 = Phone('apple', 'iPhone14',150000)
# print(p1.__price)
print(p1._Phone__price)

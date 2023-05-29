# class Circle:
#     pi = 3.14     # class variable
#     def __init__(self, radius):
#         self.radius = radius

#     def calc_circumference(self):
#         return 2 * Circle.pi * self.radius   # used circle.pi as it was a class variable
    
# c1 = Circle(4)
# c2 = Circle(9)

# print(c1.calc_circumference())

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# class vaiable for applying sale on every item and closing that sale
class Laptop:
    discount_percent = 10
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name +' '+ model_name

    def apply_discount(self):
        off_price = (Laptop.discount_percent/100)* self.price  # using laptop.discount_percent as it a class variable
        return self.price - off_price

#------------------------------------------------------to remove the discount
Laptop.discount_percent = 100
obj1 = Laptop('apple','mac13', 100000)
obj2 = Laptop('hp','pavillion',50000)
print(obj1.apply_discount())

# to know what the objects have as a variable
print(obj1.__dict__)

# -----------------------------------------------------------------------------------------------------
# to apply special discout on some objects
class Laptop:
    discount_percent = 10
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name +' '+ model_name

    def apply_discount(self):
        off_price = (self.discount_percent/100)* self.price  # using self.discount_percent if you want to change the class variable 
        return self.price - off_price

obj1 = Laptop('apple','mac13', 100000)
obj2 = Laptop('hp','pavillion',50000)
obj2.discount_percent = 50
print(obj2.apply_discount())
print(obj1.apply_discount())
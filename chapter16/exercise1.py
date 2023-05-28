# create a laptop class with attributes brand name, model name, price
# crete two objects /instance of your laptop class

class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name +' '+ model_name # ypu can delcare instance variable here without declaring in the init block

obj1 = Laptop('apple','mac13', 100000)
obj2 = Laptop('hp','pavillion', 50000)

print(obj1.brand_name)
print(obj2.laptop_name)
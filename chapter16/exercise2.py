class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name +' '+ model_name

    def apply_discount(self,num):
        off_price = (num/100)* self.price
        return self.price - off_price


obj1 = Laptop('apple','mac13', 100000)
print(obj1.apply_discount(10))
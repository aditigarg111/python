# def outer_func():
#     def inner_func():
#         print("inside inner func")
#     return inner_func # here inner function is not executed because no round brackets
# var = outer_func()
# var()  # that is why we are calling here so that it gets executed

# def outer_func():
#     def inner_func():
#         print("inside inner func")
#     return inner_func()
# var= outer_func()

# ------------------------ example2 -----------------------------
# def outer_func(msg):
#     def inner_func():
#         print(f"hi the msg is {msg}")
#     return inner_func
# var = outer_func("i am aditi")
# var()

# ----------------------------power of a number function 
def to_power(x): # x = power
    def cal_power(n):
        return n**x
    return cal_power
cube = to_power(3)
print(cube(5))
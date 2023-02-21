# x = 5 #global variable
# def func():
#     x = 7 #local variable
#     return x
# print(func())
# print(x)

# to change global value inside a function 
x = 5 #global variable
def func():
    global x
    x = 7 #local variable
    return x
print(x)
print(func())
print(x)


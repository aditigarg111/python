#  decoraters are used to enhance the functionality of the functions 
# def decorater_function(func):
#     def wrapper_function():
#         print("this is inside function")
#         func()
#     return wrapper_function

# def func1():
#     print("this is function 1")

# var = decorater_function(func1)
# var()

# ------------------------------------------------------------ return is not having ( brackets then no need to call var just declare ------------------------------------------
def decorater_function(func):
    def wrapper_function():
        print("this is inside function")
        return func()
    return wrapper_function()

def func1():
    print("this is function 1")

var = decorater_function(func1)


# ------------------------------------------------ use @ to call the decorator function--------------------------------------------
# def decorater_function(func):
#     def wrapper_function():
#         print("this is inside function")
#         func()
#     return wrapper_function


# @decorater_function
# def func1():
#     print("this is function 1")
# func1()
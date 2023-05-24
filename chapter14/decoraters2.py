def decorater_function(func):
    def wrapper_function(*args, **kwargs):
        print("this is inside function")
        return func(*args, **kwargs)
    return wrapper_function

@decorater_function
def func(a):
    print(f"this is function with argument {a}")

func(7)

# ------------------------------------------ passing two argument in func-----------------------------------------
def decorater_function(func):
    def wrapper_function(*args, **kwargs):
        print("this is inside function")
        return func(*args, **kwargs)
    return wrapper_function
@decorater_function
def add(a,b):
    return(a+b)
print(add(4,5)) # this will give error as above we have not returned anything in the wrapper function 



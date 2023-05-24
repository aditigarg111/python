from functools import wraps
def print_function_details(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"you are calling {function.__name__} function")
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
    return wrapper

@print_function_details
def addition(a,b):
    """this is a addition function"""
    return a+b
print(addition(4,5))
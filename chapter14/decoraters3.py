from functools import wraps
def decorater_function(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        """this is a wrapper function """
        print("this is inside function")
        return func(*args, **kwargs)
    return wrapper_function


@decorater_function
def add(a,b):
    """this is a addition function"""
    return(a+b)

# -----------------------------------now when we see the docstring of add it will not give for the wrapper function -------------------------
print(add.__doc__)
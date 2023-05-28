from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(i)==data_type for i in args]):
                return function(*args, **kwargs)
            print("invalid argument")
        return wrapper
    return decorator

@only_data_type_allow(str)
def str_join(*args):
    string = ''
    for i in args:
        string += i
    return string

print(str_join("aditi","garg"))
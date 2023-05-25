# from functools import wraps
# def for_int_only(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         data_type = []
#         for i in args:
#             data_type.append(type(i)==int)
#         if all(data_type):
#             return function(*args, **kwargs)
#         else:
#             print("invalid argument")
#     return wrapper
    
# @for_int_only
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add_all(1,2,3,4,5,6,[1,2,4]))

# ---------------------------------------small code
from functools import wraps
def for_int_only(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(i)==int for i in args]):
            return function(*args, **kwargs)
        print("invalid argument")
    return wrapper

@for_int_only
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,5,6,[1,2,4]))
# kwargs(keywprd arguments)
# **kwargs (double str operator)
# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# func(first_name = "aditi", last_name = "garg")

# loops

def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

# dictionary unpacking 
d = {"name":"aditi", "age":22}
func(**d)
# func(first_name = "aditi", last_name = "garg")
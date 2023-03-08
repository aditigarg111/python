# define a functiom
# name = ["aditi","avani"]

# print(func(name))
# print(func(name,reverse_str=True))

def fun(l,**kwargs):
    if kwargs.get("reverse_str")==True:
        return[name[::-1].title () for name in l]
    else:
        return[name.title() for name in l]

name = ["aditi","avani"]
print(fun(name))
print(fun(name,reverse_str=True))
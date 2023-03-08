# default parameter
# def fun(name = "unknown", age =23):
#     print (name)
#     print(age)
# fun()

# parameter
# *args
# default parameters
# **kwargs
# if we want to use all of them what should be the order

def fun(name,*args,last_name="unknown",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

fun("aditi", 1,2,3, a=1, b=3)
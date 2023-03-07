# normal args code 
# def multiply(*args):
#     num = 1
#     for i in args:
#         num *= i
#     return num
# print(multiply(2,3,4)) --- here we don't need to pass values in function while calling 

# if we add other parameter in the function the the first number will not be a part of the args 
def multiply(a,*args):
    num = 1
    print(a)
    print(args)
    for i in args:
        num *= i
    return num
print(multiply(2,3,4)) # here we need to pass value in the function while calling if we have declared two variables in the function 
# we cannot write *args before other parameter

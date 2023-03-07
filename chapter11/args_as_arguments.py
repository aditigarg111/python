def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply
nums = [1,2,3]
print(multiply_nums(nums))
# of we want to pass the list we need to upack it for that we use 
print(multiply_nums(*nums))
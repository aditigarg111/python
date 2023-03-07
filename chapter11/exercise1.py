# define a function
# input 
# num, iterable (tuple, list) containing number as args

# example 
# nums = [1,2,3]
# to_power(3, *nums)

# output
# list [1**3,8,27]

# if user did not pass any args then give message pass args

# else return list
# use list comprehension

# solution 
def to_power(num,*args):
    if args:
        return[i**num for i in args]
    else:
        return "you did not pass args"
    
nums= [2,2,3]
print(to_power(2,*nums))

# to check wheter a list is emply or not 
# l = [1,2,3]
# if l:
#     print("not empty")
# else:
#     print("empty")
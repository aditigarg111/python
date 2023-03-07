# make flexible function
# *args
# to have ulimited values in function we use args
# def total(*args): # star operator changes every argument in tuple
#     print(args)
#     print(type(args))
# total(1,2,3,4,8)

# to print the sum of numbers
def total_num (*args):
    total = 0
    for i in args:
        total += i
    return total

print(total_num(1,2,3,4,8))
              


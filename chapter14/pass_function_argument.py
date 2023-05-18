# def square(a):
#     return a*a

# l = [1,2,3,4,5]
# print(list(map(square,l)))
# map fucnction takes a fubction as an argument

# --------------------------------- creating a function that takes a fubction as an argument-----------------
# def square(a):
#     return a*a
# l = [1,2,3,4,5]
# def my_map(func,l):  # here function takes one argyment as function and any one ietrable object a list or tuple
#     new_list = []
#     for i in l:
#         new_list.append(func(i))
#     return new_list
# print(my_map(square,l))
# print(my_map(lambda a: a**3,l))

#  by list comprehension
l = [1,2,3,4,5]
def my_map2(func,l):
    return [func(i) for i in l]
print(my_map2(lambda a: a**3,l))
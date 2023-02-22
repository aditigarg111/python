# Define a function that will take list as an argument and return the revese of it
# [1,2,3,4]--->[4,3,2,1]
#  do this with append and pop return method

# one approach
# def reverse_list(l):
#     l.reverse()
#     return l
# l = [1,2,3,4]
# print(reverse_list(l))    

# second approach
# def reverse_list(l):
#     return l[::-1]

# l = [1,2,3,4]
# print(reverse_list(l))
 
# third approach
def reverse_list(l):
    empty_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        empty_list.append(popped_item)
    return empty_list
l = [1,2,3,4]
print(reverse_list(l))    


    
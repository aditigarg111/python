# define a function that takes list 
# [1,2,3], [4,5,6], [7,8,9] 
# returns average
# (1+4+7)/3, (2+5+8)/3, (3+6+9)/3

# for two list
# def average_finder(l1,l2):
#     average =[]
#     for i in zip(l1,l2):
#         average.append(sum(i)/len(i))
#     return average
# print(average_finder([1,2,3], [4,5,6]))

# for any number of list
# def average_finder(*args):
#     average = []
#     for i in zip(*args): # * is used to unpack the list
#         average.append(sum(i)/len(i))
#     return average
# print(average_finder([1,2,3], [4,5,6], [7,8,9] ))

# make the above code in one line
average_finder = lambda *args: [sum(i)/len(i) for i in zip(*args)]
print(average_finder([1,2,3], [4,5,6], [7,8,9] ))

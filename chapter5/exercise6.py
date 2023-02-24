# write a function that a list as input
# input - [1,2,3,[1,2],[3,4]]
# output - 2 (number of elements)

def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count +=1
    return count
l = [1,2,3,[1,2],[3,4]]
print(sublist_counter(l)) 
# common elemt finder function
# define a function that takes two list 
# and return elements that are common in both list
# input = [1,2,3,4][1,2,4,5,6]
def element_finder(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(element_finder([1,2,3,4],[1,2,4,5,6]))




# define a funstion that takes list 
# input = [1,2,3,4,5,6,7]
# output =[[2,4,6][1,3,5,7]]
def odd_even(l):
    odd_nums=[]
    even_nums=[]
    for i in l:
        if i %2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums,even_nums]
    return output    

l = [2,3,4,5,7,4,11,19]
print(odd_even(l))
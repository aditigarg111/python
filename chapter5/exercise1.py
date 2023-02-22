# define a function which will take numbers as input
# and return list containing square of the element

# eg : [1,2,3,4]
# square_list(number) -------> return [1,4,9,16]

def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square

l = list(range(1,11))
print(square_list(l))    
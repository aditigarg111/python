# numbers = [1,2,3,4]
# def square(a):
#     return a**2
# squares = list(map(square,numbers))
# print (squares)

# use of lambda
# numbers = [1,2,3,4]
# squares = list (map(lambda a:a**2, numbers))
# print (squares)

# list comprehension
# numbers = [1,2,3,4]
# squares = [ i**2 for i in numbers]
# print (squares)

# normal function
numbers = [1,2,3,4]
def square(a):
    return a**2

new_list = []
for num in numbers:
    new_list.append(square(num))

print(new_list)
    

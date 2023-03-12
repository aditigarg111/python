numbers = [1,2,3,4] # iterables
squares = map(lambda a:a**2, numbers) # iterator

# how does for loops works on iterator
# number_iter = iter(numbers)
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))

# iterable
print(next(squares)) 
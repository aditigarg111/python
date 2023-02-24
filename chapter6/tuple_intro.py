# tuple can store any data type
# they are immutable
# no append, no insert, no pop, no remove
# tuples are faster
# methods that we can use in tuple - count, index, len function, slicing
# eg =("one", "two", "three")
# print(eg[::-1])

# cannot change value
# eg[0] = 4
# print(eg)

# looping in tuple
# mixed = (1,2,3,4.0)
# for i in mixed:
#     print(i)

# tuple with one element
# to do so you need to give space after one element
# num=(1,)
# print(type(num))
# words = ("aditi",)
# print(type(words))

# tuples without parenthesis
# animal = "cat", "dog", "cow"
# print(type(animal))

# tuple unpacking
# animal = ("cat", "dog", "cow")
# animal1,animal2,animal3 = animal # values should be same as assigned in tuple
# print(animal1)

# list inside tuple
# animal = ("cat", ["dog", "cow"])
# no change can be made to the tuple nut a list inside can be changed
# animal[1].pop()
# print(animal)
# animal[1].append ('aditi')
# print(animal)

# functions
# 1 min
# mixed = (1,2,3,4.0)
# print(min(mixed))
# max
# print(max(mixed))

# tuples from range
# nums = tuple(range(1,20))
# print(nums)

# to change tuples in list
nums = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
print (type(nums))
nums = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
print (type(nums))



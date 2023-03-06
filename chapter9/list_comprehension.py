# Q- create a list of square of number from 1 to 10
# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# using list comprehension
# square2 = [i**2 for i in range(1,11)]
# print(square2)

# Q - create a list of negative number from 1 to 10
# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# using list comprehension
# negative =[(-i) for i in range(1,11)]
# print(negative)

names = ["khushi","taru","arsh"]
# new_list["k","t","a"]
# using normal list 
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)

# list comprehension
new_list=[name[0] for name in names]
print(new_list)

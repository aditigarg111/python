# even odd numbers in a list
# number = list(range(1,11))
# nums=[]
# for i in number:
#     if i %2 ==0:
#         nums.append(i)
# print(nums)

# list comprehension with range already created
number = list(range(1,11))
nums = [i for i in number if i %2 ==0]
print(nums)

# list comprehension with range not created
odd_nums=[i for i in range(1,11) if i %2 !=0]
print(odd_nums)
   
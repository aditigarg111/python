# numbers1 = [2,4,6,8,10]
# numbers2 = [1,2,3,4,5,6]

# evens1 = []
# for num in numbers1:
#     evens1.append(num % 2 == 0)

# print(evens1)

# all command --- checks if all numbers are even or not
# print(all([num%2 ==0 for num in numbers1]))

# any command --- checks if any number is even or not
# print(any([num%2 ==0 for num in numbers1]))
# --------------------------------------------------------------practice ----------------------------------------------------------------
def my_sum (*args):
    if all(type(arg) == int or type(arg) == float for arg in args):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "wrong input"
print(my_sum(1,2,3,4,2.3))

# lambda function(anonymous function)
# add = lambda a,b:a+b
# print(add(3,5))

# multiply = lambda a,b:a*b
# print(multiply(3,5))

# print(add)
# print(multiply)

# even = lambda a: a%2 ==0
# print(even(9))

# last_char = lambda a: a[-1]
# print(last_char("aditi"))

# if-else with lambda
func = lambda s: True if len(s) > 5 else False
print(func("aditi"))

# without if-else
func = lambda s: len(s) > 5
print(func("aditi"))
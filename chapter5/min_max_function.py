l=[2,45,90]
# print(min(numbers))

# print(max(numbers))

# write a function that takes a list and prints the difference of the greatest and minimum element
def greatest_diff(l):
    return max(l) - min(l)
print(greatest_diff(l))    
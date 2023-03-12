# we use enumerate function with fot loop to track position of our element
# without enumerate 
# names = ["acs","niejg","knwmor"]
# pos = 0
# for name in names:
#     print(f"{pos} --------> {name}")
#     pos +=1

# without enumerate function
# names = ["acs","niejg","knwmor"]
# for pos,name in enumerate(names):
#     print(f"{pos} --------> {name}")

# define a function that takes twi arguments
# 1. list containing string
# 2. string that want to find in your list
# and this function will return the index of string in your list and if string is not presesnt then return -1
names = ["acs","niejg","knwmor"]
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
    return -1

print(find_pos(names,"adiit"))

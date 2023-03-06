# sets - unordred collection of unique items 
# you cannot store list or dictonary inside a set
s = {1,2,3,4,2} # only unique items will be printed 
# print(s)
# to remove duplicates
# l = [1,2,3,4,5,5,5,6,3,4,3,8,9]
# s2 = set(l)
# print(s2)
# # convert back into list 
# s2 = list(set(l))
# print(s2)

# to add element in set 
# s.add(6)
# print(s)

# to remove something from set 
# s.remove(4) ----- it should have that number inside set otheriwse will throw error 
# print(s)
# s.discard(9) # this will not give error evenm though the number is not in the set 
# print(s)

# clear 
# s.clear()
# print(s)

# copy method
s1 = s.copy()
print(s)
print(s1)

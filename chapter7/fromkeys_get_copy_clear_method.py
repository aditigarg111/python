#  fromkey method ---- used to create dictonary
# d = {"name":"unknown","age":"unknown","hair":"unknown"}---- when u want to keep vaues of different key same then use fromkey
# d = dict.fromkeys(["name","age","hair"],"unknown")
# print(d)

# get method 
d = {"name":"unknown","age":"unknown","hair":"unknown"}
# print(d.get("names"))# if u put something what is not in the dictonary this will show none but not error
# print(d["names"]) # shows error

# if else
# if d.get("names"):
#     print("present")
# else:
#     print("not present")

# clear method
# d.clear()
# print(d)

# copy method
d1 = d.copy() # makes two dictonary
# d1 = d # makes only one dictonary
print(d1.popitem())
print(d)


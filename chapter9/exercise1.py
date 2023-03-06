# define a function that takes a list of strings
# list containing revese of the string
# example = l ["abc","def","xyz"]
# reverse_string(l) = ["cba","fed","zyx"]

# list comprehension
def reverse_string(l):
    return[name[::-1] for name in l]
print(reverse_string(["abc","def","xyz"]))

# normal function 
def reverse_string(l):
    new_list=[]
    for name in l:
        new_list.append(name[::-1])
    return new_list
print(reverse_string(("abc","def","xyz")))
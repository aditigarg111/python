# define a function that takes words inside a list and returns reverse of each elemt inside that list
# ["abc","tuv","yaz"]--------> ["cba","vut","zay"]
def reverse(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements

l = ["abc","def","ijk"]
print(reverse(l))

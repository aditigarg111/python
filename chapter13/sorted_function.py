# ----------------------------to sort in list we use sort function
# fruits = ["apple", "mango", "grapes"]
# fruits.sort()
# print(fruits)

# ----------------------------to sort in tuple we use sorted function will return a list
# fruits = ("apple", "mango", "grapes")
# sorted(fruits)
# print(fruits)
# this will not arrange because tuple is immutable and it will return a list so 
# print(sorted(fruits))


# ----------------------------to sort in set we use sorted function will return a list
# fruits = {"apple", "mango", "grapes"}
# print(sorted(fruits))

# ----------------------------to sort in dictonaries we use sorted function will return a list
student2 = [
    {'name' : 'aditi', 'score': 90},
    {'name' : 'avani', 'score': 70},
    {'name' : 'arsh', 'score': 60}
]
print(sorted(student2, key= lambda item : item.get('score')))
print(sorted(student2, key= lambda item : item['score'], reverse = True))  # to get in descending order
print(sorted(student2, key= lambda item : item.get('score')))

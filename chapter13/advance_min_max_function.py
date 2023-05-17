# basics
# numbers = [1,2,4,5,7]
# print(max(numbers))
# print(min(numbers))

# advance
# to calculate the largest length of elemnt inside the below list
# def func(items):
#     return len(items)
# names = ["aditi","arsh","avani"]
# print(min(names, key = func))
# print(max(names, key = func))


# -------------------lambda function------------------
# names = ["aditi","arsh","avani"]
# print(max(names,key = lambda item : len(item)))

# --------------------------find max according to score
# student2 = [
    # {'name' : 'aditi', 'score': 90,'age':22},
    # {'name' : 'avani', 'score': 70,'age':16},
    # {'name' : 'arsh', 'score': 60,'age':24}
# ]
# print(max(student2,key = lambda item :item.get('score')))
# #  to get the name of highest scorer
# print(max(student2,key = lambda item :item.get('score'))['name'])
student1 = {
       'aditi':{'score': 90,'age':22},
       'avani':{'score': 80,'age':16},
       'arsh':{'score': 70,'age':26},
}
print(max(student1,key = lambda item : student1[item]['age']))

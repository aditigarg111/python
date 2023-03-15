# user_id = ["user1","user2"]
# names =["aditi","avani","arsh"] # zip will end once the smaller list ends
#  zip wil give you a tuple as an object which will be a iterator
# print(list(zip(user_id,names)))# this wont print anything because it is a iterator

# example = [(1,"a"),(2,"b"),(3,"c")]
# print (dict(example)) # changes into dictonary

#  zipping can be done for more than two list 
# user_id = ["user1","user2","user3"]
# names =["aditi","avani","arsh"]
# last_name = ["garg","pandey","deep"]
# print(list(zip(user_id,names,last_name)))

# from one list make two
# l =[(1,2),(3,4),(5,6)]
# l1 = [1,3,5]
# l2 = [2,4,6]
# we can use *zip function to do so
# print(list(zip(*l))) # this will create two tuple after breaking the list

#  now to make two seperate list
# l =[(1,2),(3,4),(5,6)]
# l1,l2 = list(zip(*l))
# print(list(l1))
# print(list(l2))

# to see which element is greater in both list index by index like 1 or 2 , 3or 4 
l1 = [1,3,5,7]
l2 = [2,4,6,8]
new_list =[]
for i in zip(l1,l2):
    new_list.append(max(i))
print(new_list)









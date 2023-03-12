# user_id = ["user1","user2"]
# names =["aditi","avani","arsh"] # zip will end once the smaller list ends
#  zip wil give you a tuple as an object which will be a iterator
# print(list(zip(user_id,names)))# this wont print anything because it is a iterator

# example = [(1,"a"),(2,"b"),(3,"c")]
# print (dict(example)) # changes into dictonary

#  zipping can be done for more than two list 
user_id = ["user1","user2","user3"]
names =["aditi","avani","arsh"]
last_name = ["garg","pandey","deep"]
print(list(zip(user_id,names,last_name)))

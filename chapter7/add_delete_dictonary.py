user_info={
    "name":"aditi",
    "age":24,
    "fav_movie":["krish","dhoom"],
    "fav_music":["classic","jazz","pop"]
}
# add data
# user_info["food"]=["noodles","pasta"]
# print (user_info)

# pop data(put key in bracket)------ returns list
# popped_item = user_info.pop("fav_music") # return popped value 
# print(f"popped item is {popped_item}")
# print (user_info)

# pop item method (used to delete a random key value pair) ---- returns tuple
popped_item = user_info.popitem() # randomly pops item 
print(popped_item)
print(user_info)




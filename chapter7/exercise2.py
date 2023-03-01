# user_info={
#     "name":"aditi",
#     "age":24,
#     "fav_movie":["krish","dhoom"],
#     "fav_songs":["song1","song2"]
# }
# ask user to input all this
user = {}
name = input("enter your name : ") 
age = input("enter your age: ")
fav_movies = input ("enter your fav movies seperated by ,").split(",")
fav_songs = input ("enter your fav songs seperated by ,").split(",")

# to put the values in the dictonary
user["name"] = name
user["age"] = age
user["fav_movies"] = fav_movies
user["fav_songs"] = fav_songs

for key,value in user.items():
    print(f"{key}:{value}")


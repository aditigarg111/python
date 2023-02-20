#take 2 comma seperated value from user 
# 1. user_name
# 2. character

# print 2 lines
# 1. length of the name entered 
# 2. count the number of character that user entered 
# name,char = input("enter your name and char").split(",")
# print(f"length of the name is {len(name)}")
# print(f"charater count {name.lower().count(char.lower())}")

# to remove spaces
# name.strip().lower().count(char.strip().lower())
# char.strip().lower()
name,char = input("enter your name and char").split(",")
print(f"length of the name is {len(name)}")
print(f"charater count {name.strip().lower().count(char.strip().lower())}")

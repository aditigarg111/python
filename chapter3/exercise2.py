# ask user name and age 
# if user name starts with ('a' or 'A')then age is above 10
# then print you can watch coco
# else print sorry you cannot watch coco
name = input("enter your name")
age = int(input("enter your age:"))
if age == 10 and name[0] =='a'or name[0]=='A':
    print("you can watch coco")
else:
    print("sorry you cannot watch coco")    

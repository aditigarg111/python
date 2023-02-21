# name = "aditi"
# for i in range(len(name)):
#     print(i)

# name = "aditi"
# for i in name:
#     print(i)

# ask user to input a number containing more than one digit 
# example 1256
# print sum 1+2+3+4

num= input("enter a number: ")
total = 0
for i in num:
    total += int(i)
print(total)
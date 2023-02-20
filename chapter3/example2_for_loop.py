# ask user to input a number containing more than one digit 
# example 1256
# print sum 1+2+3+4

num = input("enter a number ")
total = 0
for i in range(0,len(num)):
    total += int(num[i])
print(total)    
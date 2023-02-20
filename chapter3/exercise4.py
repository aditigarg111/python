# ask user to input a number containing more than one digit 
# example 1256
# print sum 1+2+3+4

num = input("enter number ")
total = 0
i = 0
while i < len(num):
    total += int(num[i])
    i+= 1
print(total)    

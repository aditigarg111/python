#sum of n natural number
# ask user for natural number(n)
#print total from 1 to n

num = int(input("enter  a number :"))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1
print (sum)    

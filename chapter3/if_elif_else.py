age  = int(input("enter your age :"))
if 0<age<=3:
    print("ticket price : Free")
elif 3<age<=10:
    print("ticket price : 150")
elif 10<age<=60:
    print("ticket price : 250")
else:
    print("ticket price : 500")    

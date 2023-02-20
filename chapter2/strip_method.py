#to remove spaces in your String
name = "   aditi    "
dots =".............."
#left space 
print(name+dots)
print(name.lstrip()+dots)
#right space 
print(name.rstrip()+dots)
#strip
print(name.strip()+dots)
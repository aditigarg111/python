# def user_info(first_name, last_name, age):
#     print(f"user first name is {first_name}")
#     print(f"user lsst name is {last_name}")
#     print(f"user age is {age}")
    
# user_info("aditi","garg",22)    

# default values 
def user_info(first_name, last_name, age=22):
    print(f"user first name is {first_name}")
    print(f"user lsst name is {last_name}")
    print(f"user age is {age}")
    
user_info("aditi","garg")    

# default parameter can only be at last position
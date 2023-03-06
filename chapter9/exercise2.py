# num to string
# define a function
# input =["true","false",[1,2,3],1,1.1]
# output = ["1","1.1"]
def num_to_string(l):
    return[str(i) for i in l if (type(i)==int or type(i)==float)]
print(num_to_string(["true","false",[1,2,3],1,1.1]))
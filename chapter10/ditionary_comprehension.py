# d = {1:1,2:4,3:9}
# square = {i:i**2 for i in range(1,11)}
# print(square)
# # to use f string liuke square of i is 2,,4 ....
# square = {f"square of {i} is": i**2 for i in range(1,11)}
# print(square)
# for a,b in square.items():
#     print(f"{a}:{b}")

# to count the number of character 
string = "aditi"
word_count = {char : string.count(char) for char in string}
print(word_count)
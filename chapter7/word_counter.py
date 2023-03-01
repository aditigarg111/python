# aditi
# d = {"a":1,"d":1,"i":2,"t":1,"i":2} # it obverrides no need to store in temp
# print(d)

def word_counter(s):
    count = {}
    for i in s:
        count[i] = s.count(i)
    return count
print(word_counter("aditi"))
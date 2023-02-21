# define is_palindrome function that takes one word as string input
# and return true if it is palindorme else false

# palindrome - words that reads same as backward
# eg.
# madam, naman

# def is_palindrome(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False

# print(is_palindrome("aditi"))            
# print(is_palindrome("naman")) 

#shortcut
# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False

# print(is_palindrome("aditi"))            
# print(is_palindrome("naman")) 

#shortest way
def is_palindrome(word):
    return word == word[::-1]
    
print(is_palindrome("aditi"))            
print(is_palindrome("naman")) 
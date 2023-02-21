#DRY = don't repeat you code best solution
# winning_number = 40
# guess = 1
# number = int(input("enter a number: "))
# game_over = False
# while not game_over:
#     if number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times")
#         game_over = True
#     elif number < winning_number:
#         print("too low")
#     else:
#         print("too high")
#     guess+=1
#     number = int(input("guess again: "))  

#solution 2
# winning_number = 40
# guess = 1
# number = int(input("enter a number: "))
# while True:
#     if number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times")
#         break
#     elif number < winning_number:
#         print("too low")
#     else:
#         print("too high")
#     guess+=1
#     number = int(input("guess again: "))  

#solution 3
# winning_number = 40
# guess = 1
# while True:
#     number = int(input("enter a number: "))
#     if number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times")
#         break
#     elif number < winning_number:
#         print("too low")
#     else:
#         print("too high")
#     guess+=1

#random number   
import random 
winning_number = random.randint(1,100)
guess = 1
number = int(input("enter a number: "))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"you win, and you guessed this number in {guess} times")
        game_over = True
    elif number < winning_number:
        print("too low")
    else:
        print("too high")
    guess+=1
    number = int(input("guess again: ")) 




     
#modify number guessing game 
# use random package
# import random
# number = random.randint(1,100)

winning_number = 40
guess = 1
number = int(input("enter a number: "))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"you win, and you guessed this number in {guess} times")
        game_over = True
    elif number < winning_number:
        print("too low")
        guess+= 1
        number = int(input("guess again: "))   
    else:
        print("too high")
        guess+=1
        number = int(input("guess again: "))     

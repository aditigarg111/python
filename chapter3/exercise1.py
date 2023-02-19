# make a variable, like winning_game and assign a number to it
# ask a user to guess a number
# if user guesses correctly then print "you win"
# if user didn't guessed correctly then 
#     if guessed lower than the number print too low
#     if guessed greater than the number print too high
    
winning_game = 50
guessed_num = int(input("guess a number"))
if winning_game == guessed_num:
    print("you win")
else:
    if guessed_num < winning_game:
        print("num is too low")
    else:
        print("num is too high")    
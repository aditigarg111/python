winning_game = 50
guessed_num = int(input("guess a number"))
if winning_game == guessed_num:
    print("you win")
else:
    if guessed_num < winning_game:
        print("num is too low")
    else:
        print("num is too high")   
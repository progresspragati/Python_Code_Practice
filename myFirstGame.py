MAX_ATTEMPTS = 3
LOW, HIGH = 1, 100

import random
def guessingNumberGame():
    random_num = random.randrange(LOW, HIGH)
    print(f"**************Welcome!**************\nGuess The Number Between {LOW} to {HIGH}.")
    print("************************************")
    i = 1
    j = 0
    while i <= MAX_ATTEMPTS and j == 0:
        try:
            guess_num = int(input("Enter Your Guess Number:"))
        except:
            print("Given input is not a number!Please, enter a number!")
            continue
        if guess_num == random_num:
            print(f"You guessed right number in {i} attempts.")
            print("Congratulations! You won the Game!")
            j = 1
        else:
            if guess_num > random_num:
                print("Guessed number is too high")
            else:
                print("Guessed number is too low")
            print("Please Try Again!")
        i += 1
    if j == 0:
        print("Your have tried Maximum Attempts, You have lost the Game!")
        print(f"The correct number is {random_num}")
    is_continue_game = input("Do you want to play again?(y/n):")
    if is_continue_game == "y":
        print("")
        guessingNumberGame()
    return


guessingNumberGame()

import random

MAX_ATTEMPTS = 10
LOW, HIGH = 1, 100

def getUserGuess():
    while True:
        try:
            guess_num = int(input("Enter Your Guess Number:\n-> "))
        except ValueError:
            print("Given input is not a number!Please, enter a number!\n")
            continue
        if guess_num < LOW or guess_num > HIGH:
            print(f"Given input is out of range.Please, Enter the number between {LOW} and {HIGH}.")
            continue
        return guess_num

def processGuess(random_num):
    attempts = 1
    won = False
    while attempts <= MAX_ATTEMPTS and not won:
        guess_num = getUserGuess()
        if guess_num == random_num:
            print(f"You guessed right number in {attempts} attempts.")
            print("\nCongratulations! You won the Game!")
            won = True
        else:
            if guess_num > random_num:
                print("Guessed number is too high!")
            else:
                print("Guessed number is too low!")
            if MAX_ATTEMPTS - attempts:
                print(f"Please Try Again! You have left {MAX_ATTEMPTS - attempts} attempts.\n")
        attempts += 1
    if not won:
        print("You have tried maximum attempts, You have lost the Game!")
        print(f"The correct number is {random_num}")
        print("Please, play again!")

def playRound():
    random_num = random.randint(LOW, HIGH)
    print(f"\n**************Welcome!**************\nGuess The Number Between {LOW} to {HIGH}.")
    print("************************************\n")
    processGuess(random_num)

def guessingNumberGame():
    while True:
       playRound() #We play game with this function
       is_continue_game = input("\nDo you want to play again?(y/n):").strip().lower()
       if is_continue_game != "y":
           print("\nThanks for playing!")
           break
    return


guessingNumberGame()

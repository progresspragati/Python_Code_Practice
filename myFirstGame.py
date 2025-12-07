import random

MAX_ATTEMPTS = 10
LOW, HIGH = 1, 100

def guessingNumberGame():
    is_continue_game = "y"
    while is_continue_game == "y":
        random_num = random.randint(LOW, HIGH)
        print(f"\n**************Welcome!**************\nGuess The Number Between {LOW} to {HIGH}.")
        print("************************************\n")
        attempts = 1
        won = False
        while attempts <= MAX_ATTEMPTS and not won:
            try:
                guess_num = int(input("Enter Your Guess Number:\n-> "))
            except ValueError:
                print("Given input is not a number!Please, enter a number!")
                continue
            if guess_num < LOW or guess_num > HIGH:
                print(f"Given input is out of range.Please, Enter the number between {LOW} and {HIGH}.")
                continue
            if guess_num == random_num:
                print(f"You guessed right number in {attempts} attempts.")
                print("\nCongratulations! You won the Game!")
                won = True
            else:
                if guess_num > random_num:
                    print("Guessed number is too high")
                else:
                    print("Guessed number is too low")
                print(f"Please Try Again! You have left {MAX_ATTEMPTS - attempts} attempts.")
            attempts += 1
        if not won:
            print("You have tried maximum attempts, You have lost the Game!")
            print(f"The correct number is {random_num}")
        is_continue_game = input("\nDo you want to play again?(y/n):").strip().lower()
    return


guessingNumberGame()

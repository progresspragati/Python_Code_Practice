import random
random_num = random.randrange(1,10)
print("**************Welcome!**************\nGuess The Number Between 1 to 10.")
print("************************************")
i = 0
while i < 5:
    try:
        guess_num = int(input("Enter Your Guess Number:"))
    except:
        print("Given input is not a number!")
    if guess_num == random_num:
        print("Congratulations! You won the Game!")
        exit()
    else:
        if guess_num > random_num:
            print("Guessed number is too high")
        else:
            print("Guessed number is too low")
        print("Please Try Again!")
    i += 1
print("Your have tried Maximum Attempts, You have lost the Game!")
print(f"The correct number is {random_num}")
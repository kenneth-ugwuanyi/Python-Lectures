"""print("Welcome to the ultimate guessing game that will test your intelligence")

print()

import random

correct_num = random.randint(1, 100)

trial = 5

def correct_guess():
     correct_guess = int(input("please input a random number"))

while trial > 0:
    select = int(input(" Please enter a random number between 1 and 100: "))
    if select == myNumber:
        print(" You have won the jackpot! Congratulations")
        break

    else:
        print("Your guess is wrong try again")
        trial -= 1
        print(f"You have {trial} trials left")

        if trial == 0:
            print("The game is over you have exhausted your trials! please try again later")"""

import random

print("Welcome to the ultimate number guessing game")
print("You have exactly five chances to win big in this game")

while True:
    right_number = random.randint(1, 100)
    trial = 0

    while trial < 5:
        guess = int(input("Please enter a random number between 1 and 100: "))

        if guess == right_number:
            print("Congratulations! You just hit the jackpot!")
            break

        elif guess < right_number:
            print(f"Sorry, your guess is less than the right number. You have {4 - trial} tries left.")
            trial += 1

        elif guess > right_number:
            print(f"Sorry, your guess is higher than the right number. You have {4 - trial} trials left.")
            trial += 1

        if trial >= 5:
            print(f"Game over! You have used the maximum of {trial} allowed. The correct answer is {right_number}.")
            play_again = input("Enter y to start a new game, or any other key to exit: ")
            if play_again != "y":
                break
                if play_again != "y":
                    break















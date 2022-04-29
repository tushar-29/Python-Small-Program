import random


def game_level(stage):
    if stage == "hard":
        return 5
    elif stage == "easy":
        return 10
    else:
        print("Wrong level entry \n so default level is 'easy' ")
        return 10


def high_low(guess_num, num):
    if guess_num > num:
        print("guessed no. was too high")
    elif guess_num < num:
        print("guessed no. was too low")


print("WELCOME TO THE NUMBER GUESSING GAME FORM 0 TO 100")
NUM = random.randint(0, 100)
level = input("Type 'hard' or 'easy' for different level of the game : ").lower()
live = game_level(level)
while live > 0:
    guess = int(input("Enter your guess between 0 to 100 : "))
    if guess == NUM:
        print(f"YOU WIN \nYou have guess the no. {NUM}")
        exit(1)
    else:
        live -= 1
        high_low(guess, NUM)
print(f"You loose \n the no. was {NUM}")

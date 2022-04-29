import random


def shape_finder(x, y):

    def get_shape(shape):
        if shape == 0:
            return "ROCK"
        elif shape == 1:
            return "PAPER"
        else:
            return "SCISSOR"
    print("Your choice is {}".format(get_shape(x)))
    print("Your choice is {}".format(get_shape(y)))
    

print("PROGRAM TO PLAY ROCK PAPER SCISSOR GAME")
input("PRESS ENTER TO START ")
user = int(input("Enter 0 for rock, 1 for paper and 2 for scissor : "))
comp = int(random.randint(0, 2))
# comparing the outcomes
if user == comp:
    print("ITS  A DRAW ")
    shape_finder(user, comp)

elif (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
    print("YOU LOSE ")
    shape_finder(user, comp)

elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
    print("YOU WIN")
    shape_finder(user, comp)
else:
    print("INVALID ENTRY")
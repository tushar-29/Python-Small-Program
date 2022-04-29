import random
print("\nWELCOME TO BLACKJACK/21 GAME : ")
input("PRESS ENTER TO START THE GAME  \n")
def add_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def count_cards(add_card):
    if 11 in add_card and sum(add_card) > 21:
        add_card.remove(11)
        add_card.append(1)
    return sum(add_card)


def check_for_win(user_sum, dealer_sum, user_card, dealer_card):
    print("GAME OVER")
    print(f"Your cards are {user_card}")
    print(f"Dealer cards are {dealer_card}")
    print(f"Your score is {user_sum}")
    print(f"Dealer score is {dealer_sum}")
    if user_sum > dealer_sum:
        if user_sum <= 21:
            print("YOU WIN")
        else:
            print("YOU LOST")
    elif dealer_sum > user_sum:
        if dealer_sum <= 21:
            print("YOU LOSE")
        else:
            print("YOU WIN")
    elif dealer_sum > 21 and user_sum > 21:
        print("ITS A DRAW")


while True:
    dealer_card = []
    user_card = []
    for i in range(0, 2):
        user_card.append(add_card())
        dealer_card.append(add_card())

    user_score = count_cards(user_card)
    dealer_score = count_cards(dealer_card)

    print(f"Your cards are {user_card} .")
    print(f"Dealer cards are [{dealer_card[1]} , ?] . ")
    print(f"Your score is {user_score}")


    if dealer_score < 14:
        print("Dealer score is less then 14 so dealer pick a card.")
        print(f"Dealer cards are [{dealer_card[0]}, {dealer_card[1]}, ?]")
        dealer_card.append(add_card())
        dealer_score = count_cards(dealer_card)
    if user_score == 21 or dealer_score == 21 or user_score > 21:
        break
    else:
        x = input(f"Do you want to add more cards say 'YES' or 'NO'\n NO will take us for results : \n").lower()
        if x == "yes":
            user_card.append(add_card())
            user_score = count_cards(user_card)
            break
        else:
            break
check_for_win(user_score, dealer_score, user_card, dealer_card)

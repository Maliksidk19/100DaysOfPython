import random
from Files.blackjack_art import logo

cards = {
    'Ace': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

userCards = []
dealerCards = []

print(logo)
print("Welcome to Blackjack Card Game")

userCard1 = random.choice(list(cards.items()))
userCard2 = random.choice(list(cards.items()))

userCards.append(userCard1)
userCards.append(userCard2)
userScore = userCards[0][1] + userCards[1][1]
print(f"User has cards {userCards[0][0]} and {userCards[1][0]}, User has a score of {userScore}")

dealerCard1 = random.choice(list(cards.items()))
dealerCard2 = random.choice(list(cards.items()))

dealerCards.append(dealerCard1)
dealerCards.append(dealerCard2)
dealerScore = dealerCards[0][1] + dealerCards[1][1]
print(f"Dealer has cards {dealerCards[0][0]}, Dealer has a score of {dealerCards[0][1]}")

print("\nHint: Enter 'hit' to choose a new card, Enter 'stand' to give turn to dealer.")
hitOrStand = input("What you want to choose? ")

if hitOrStand == 'hit':
    userNewCard = random.choice(list(cards.items()))
    userCards.append(userNewCard)
    userScore = userScore + userCards[len(userCards) - 1][1]
    print(f"\nNow user has cards {userCards[0][0]}, {userCards[1][0]} and {userCards[2][0]}, User has a score of {userScore}")
    if userScore > 21:
        print("Dealer Wins!")
    if userScore <= 21:
        print("\nHint: Enter 'hit' to choose a new card, Enter 'stand' to give turn to dealer.")
        hitOrStand = input("What you want to choose? ")
        if hitOrStand == 'hit':
            userNewCard = random.choice(list(cards.items()))
            userCards.append(userNewCard)
            userScore = userScore + userCards[len(userCards) - 1][1]
            print(f"\nNow user has cards {userCards[0][0]}, {userCards[1][0]}, {userCards[2][0]} and {userCards[3][0]}, User has a score of {userScore}")
            if userScore > 21:
                print("Dealer Wins!")
            if userScore <= 21:
                print("\nHint: Enter 'hit' to choose a new card, Enter 'stand' to give turn to dealer.")
                hitOrStand = input("What you want to choose? ")

if hitOrStand == 'stand':
    print(f"\nDealer has cards {dealerCards[0][0]} and {dealerCards[1][0]}, Dealer has a score of {dealerScore}")
    while dealerScore < 16:
        dealerNewCard = random.choice(list(cards.items()))
        dealerCards.append(dealerNewCard)
        dealerScore = dealerScore + dealerCards[2][1]
        print("Dealer Hits!!")
        print(f"Now dealer has cards {dealerCards[0][0]}, {dealerCards[1][0]} and {dealerCards[2][0]}, Dealer has a score of {dealerScore}")
    if dealerScore > 21:
        print("User Wins!")
    elif dealerScore > userScore:
        print("Dealer Wins!")
    elif dealerScore < userScore:
        print("User Wins!")
    elif dealerScore == userScore:
        print("Draw!!")

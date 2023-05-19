from Files.higherlower_art import logo, vs
from Files.higherlower_gamedata import data
import random

score = 0
chosenA = random.choice(data)
chosenB = random.choice(data)
while True:
    print(logo)
    chosenC = random.choice(data)
    print(f"Compare A: {chosenA['name']}, a {chosenA['description']}, from {chosenA['country']}.")
    print(vs)
    print(f"Against B: {chosenB['name']}, a {chosenB['description']}, from {chosenB['country']}.")

    followers = input("Who has more followers? Type 'A' or 'B': ")

    if followers == "A":
        if chosenA["follower_count"] > chosenB["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}. ")
            chosenA = chosenB
            chosenB = chosenC
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            exit()
    elif followers == "B":
        if chosenB["follower_count"] > chosenA["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}. ")
            chosenA = chosenB
            chosenB = chosenC
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            exit()
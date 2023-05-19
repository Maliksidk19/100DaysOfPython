from Files.guess_art import logo
import random
chosen = random.randint(1,100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def guessNumber(n):
    i = n
    while i > 0:
        print(f"You have {i} attempts reamining to guess the number")
        guess = int(input("Make a guess: "))
        if i == 1 and guess < chosen:
            print("Too low.")
        elif i == 1 and guess > chosen:
            print("Too high.")
        elif guess < chosen:
            print("Too low.")
            print("Guess again.")
        elif guess > chosen:
            print("Too high.")
            print("Guess again.")
        elif guess == chosen:
            print(f"You got it! The answer was {chosen}.")
            exit()
        i -= 1
    
    print("You've run out of guesses, you lose.")

if difficulty == 'easy':
    guessNumber(10)
elif difficulty == 'hard':
    guessNumber(5)
        
        
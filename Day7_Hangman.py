import random
from Files.hangman_art import stages, logo
from Files.hangman_wordlist import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False

display = []

for _ in range(word_length):
    display += '_'

print(logo)

print("Welcome to Hangman Game.")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"The letter {guess} you guessed is already selected.")
    for position in range(word_length):
        letter = chosen_word[position]
        
        if guess == letter:
            display[position] = letter
            
    if guess not in display:
        print(f"You guessed {guess}, It's not present in word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
    
    print(f'{" ".join(display)}')
    
    if '_' not in display:
        end_of_game = True
        print("You Win.")
        
    print(stages[lives])
import pandas as pd

data = pd.read_csv('Files/nato_phonetic_alphabet.csv')

nato_phonetic_alphabets = {row.letter: row.code for (index, row) in data.iterrows() if row.letter != 'letter'}

user_input = input("Enter a word here: ").upper()

result = [nato_phonetic_alphabets[letter] for letter in user_input]

print(result)
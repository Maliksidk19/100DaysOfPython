import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't','u','v', 'w', 'x', 'y', 'z', 'A', 'B',
    'C', 'D', 'E','F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to Random Password Generator.")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password = ""
for n in range(0, nr_letters):
    password += random.choice(letters)

for n in range(0, nr_symbols):
    password += random.choice(symbols)
    
for n in range(0, nr_numbers):
    password += random.choice(numbers)

print(f"Your password is: {password}")

random_password = "".join(random.sample(password, len(password)))

print(f"Your random password is: {random_password}")
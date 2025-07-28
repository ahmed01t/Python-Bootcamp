import string
import random

# List 1: All alphabets (uppercase + lowercase)
alphabets = list(string.ascii_letters)  # 'A'-'Z' and 'a'-'z'

# List 2: All digits
numbers = list(string.digits)  # '0'-'9'

# List 3: All punctuation symbols
symbols = list(string.punctuation)  # Special characters like !@#$%^&*() etc.
print("Welcome to my password generator!")
letters=int(input("how many letters you want in your password?\n"))
n_numbers=int(input("how many numbers you want in your password?\n"))
n_symbols=int(input("how many symbols you want in your in password?\n"))
password_list=[]
for char in range(0,letters):
    password_list.append(random.choice(alphabets))

for char in range(0,n_numbers):
    password_list.append(random.choice(numbers))

for char in range(0,n_symbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password=""
for char in password_list:
 password+=char
print(f"your password is {password}")
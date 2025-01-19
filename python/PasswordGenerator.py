import string
import random 

print("Password Generator \n")

alphabet = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list(string.punctuation)

password = [] # Empty password list to store the characters

num_alpha = int(input("Enter the number of alphabets you need: "))
num_digit = int(input("Enter the number of digits you need: "))
num_special = int(input("Enter the number of special characters you need: "))

for n in range(0, num_alpha):
    password.append(random.choice(alphabet))

for n in range(0, num_digit):
    password.append(random.choice(digits))

for n in range(0, num_special):
    password.append(random.choice(special_characters))

random.shuffle(password) # Shuffles the items within the list

password_string = "" # Empty password string to store the items within the password list as a legal string

for char in password:
   password_string += char # Concatenates single characters into a string

print(password_string)
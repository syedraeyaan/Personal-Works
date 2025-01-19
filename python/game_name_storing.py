print("Enter games which you like")

game = [] # Empty list to store 5 game name
name = "" # Empty string to store individual game name

choice = int(input("How many games would you like to save ? "))

for n in range (0,choice):
    name = input("Name: ")
    game.append(name)

print(game)
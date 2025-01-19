print("Enter 5 games which you like")

game = [] # Empty list to store 5 game name
name = "" # Empty string to store individual game name

for n in range (0,5):
    name = input("Name: ")
    game.append(name)

print(game)
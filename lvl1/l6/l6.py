import random

games =["fortnite","valorant","lol","ffff"]
print(games)
print(games[1])
games[3]="pubg"
print(games)
games.append("csgo")
print(games)
games.remove("fortnite")
print(games)
last=games.pop()
print(f"last was{last}.now{games}")
for game in games:
    print(game)
length = len(games)
for i in range (length):
    print(f"{i+1}: {games[i]}")
if "lol" in games:
    print("you are a comp player")
if "ffff" not in games:
    print("games list is valid")
# create games library editor
character = ["Wise", "Cheeky", "Cheerful", "Lame", "Cowardly", "Brave", "Crazy", "Proud", "Big-Eared", "Unstoppable"]
animal = ["Tiger", "Gopher", "Eagle", "Rabbit", "Deer", "Hog", "Saiga", "Bear", "Mustang", "Giraffe"]
first_name = random.choice(character)
second_name = random.choice(animal)
print(f"In the Chickasaw tribe your name would be: {first_name} {second_name}!")
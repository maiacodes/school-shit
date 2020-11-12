from random import randint
from user import login
import scores

print("-- Welcome to the stupid dice game --")

# Set play variables
players = []
rounds = 0
max_rounds = 5

def indent():
    print("------")

# Login player 1
authed, player1 = login.loginPlayer(1)
if not authed:
    print("Incorrect!")
    quit()
print(f"Hello {player1.name}!")
indent()
players.append(player1)

# Login player 2
authed, player2 = login.loginPlayer(2)
if not authed:
    print("Incorrect!")
    quit()
print(f"Hello {player2.name}!")
players.append(player2)

import random

def rollDice():
    return random.randint(1, 6)

# Rounder
while rounds < max_rounds+1:
    indent()
    print(f"ROUND {rounds}")
    for player in players:
        indent()
        print(f"{player.name}, Ready to roll the dice?")
        if input("Press `y` to roll: ") == 'y':
            roll = rollDice()
            print(f"You rolled a {roll}!")
            player.addScore(roll)
            print(f"{player.name}, your score is now {player.score}")
    rounds = rounds + 1



if players[0].score == players[1].score:
    print("There's a tie! Keep playing...")

indent()
print("END OF GAME!")
best_player = players[0]
for player in players:
    if player.score > best_player.score:
        best_player = player
    print(f"{player.name}: {player.score} Points")

indent()
scores.storeScore(best_player.name, best_player.score)
print(f"{best_player.name} won with {best_player.score} points!")
input("- Press enter to see the top scores -")
scores.showTop()
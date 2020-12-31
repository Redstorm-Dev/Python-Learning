import random
import os

print("How many games?:",end="")
gamesnum = input().strip()
while not gamesnum.isdigit():
    print("Invalid number!")
    gamesnum = input()
    os.system("cls")

gamesplayed = 0
if int(gamesnum) == 0:
    print("You've completed all",gamesnum,"ga--oh wait, none?\nOh well")
    exit()
while gamesplayed <= int(gamesnum):
    moves = ['Rock','Paper','Scissors']
    print("Choose your move [Rock, Paper, Scissors]: ",end="")
    move = input()
    law = move in moves
    while not law:
        print("Invalid move.")
        move = input()
        os.system("cls")
        law = move in moves
    cpumove = random.choice(moves)
    print("Your move:",move,". CPU Move:",cpumove,".")
    os.system("cls")
    gamesplayed += 1

print("You've completed all",gamesnum,"games!")
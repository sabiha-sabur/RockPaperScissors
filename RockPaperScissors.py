#import modules
from random import randint

#options for the game
choice=["rock","paper","scissors"]

computer = choice[randint(0,2)]

#start the game
print("Welcome to Rock, Paper, Scissors")
player = input("Type in your choice:").lower()
print("Computer chose: "+ computer)

#logic of the game 
if player == computer:
    print("Draw")
elif player == "rock" and computer == "paper":
    print("Computer wins :(")
elif player == "paper" and computer == "scissors":
    print("Computer wins :(")
elif player == "scissors" and computer == "rock":
    print("Computer wins :(")
elif player == "paper" and computer == "rock":
    print("Player wins!!! :)")
elif player == "scissors" and computer == "paper":
    print("Player wins!!! :)")
elif player == "rock" and computer == "scissors":
    print("Player wins!!! :)")

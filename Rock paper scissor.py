'''
---Docstring for Rock paper scissor---


first we import the random method

second we used ot create a list to take the three strings/Elements.

third we used take two input by user and computer for performing the game.computer variable
assign list Element with random choice method

fourth we used if...elif...else condition to check user and computer 

'''


import random

list = ["Rock","paper","Scissor"] 

user_choice = input("Enter your Chance ( Rock , paper , Scissor ) = ")

computer_choice = random.choice(list)

print(f"User choice = {user_choice}\ncomputer choice = {computer_choice}")

if user_choice == computer_choice:
    print("Both choices same: Match Tie")

elif user_choice == "Rock":
    if computer_choice == "paper":
        print("paper covers Rock = computer win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "paper":
    if computer_choice == "Scissor":
        print("Scissor cut the Paper = computer win ")
    else:
        print("paper cover rock = User win")

elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Rock break the Scissor = computer win")
    else:
        print("Scissor cut the paper = user win")

else:
    print("Thanks for playing the game")
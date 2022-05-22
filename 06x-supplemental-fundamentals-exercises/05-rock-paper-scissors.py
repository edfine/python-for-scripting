# Write a script that, when executed, allows the user to 
# play a game of rock paper scissors against a computer.
# To do this, you will need to accept input from the user,
# and use python's random module to control the computer's
# choices...

# Here is a little code to help you get started:

# This builtin function, choice, randomly selects an item from a list.
from random import choice
sample_list = ['rock', 'paper', 'scissors']

player_typed = input("Choose rock paper or scissors\n> ")
while player_typed not in sample_list:
    print("Try again, and please choose rock paper or scissors")
    player_typed = input("Choose rock paper or scissors\n> ")

print("Random selection: ", choice(sample_list))
print("Player typed: ", player_typed)

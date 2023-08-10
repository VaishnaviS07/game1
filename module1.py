#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      khush
#
# Created:     11-08-2023
# Copyright:   (c) khush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "stone" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "stone") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Hurray"
    else:
        return "Looser"

def main():
    choices = ["stone", "paper", "scissors"]
    while True:
        print("Choose your move: stone, paper, or scissors (or 'quit' to exit)")
        player_choice = input().lower()

        if player_choice == "quit":
            print("See you soon")
            break

        if player_choice not in choices:
            print("WRONG ENTRY")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()

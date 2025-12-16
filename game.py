# create a simple rock, paper, scissors game
# provide a welcome message
# get user's choice
# generate computer's choice
# compare choices and determine the winner
# display the result
# ask if the user wants to play again
# say goodbye when the user decides to quit and exit the game
# use one function to handle the game logic

import random
from re import match
from unittest import case

#play_again_options enum
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

user_choices = ['rock', 'paper', 'scissors', 'r', 'p', 's']
computer_choices = ['rock', 'paper', 'scissors']
play_again_options = enum('NO', 'YES', 'N', 'Y')

def play_around() -> None:

    # Welcome message
    print("Welcome to Rock, Paper, Scissors!")  
    
    
    #define enum for play again options like 'n', 'no', 'y', 'yes'
    play_again_options = enum('NO', 'YES', 'N', 'Y')

    while True:
    # Get user's choice
        user_choice = input("Enter your choice ((r)ock, (p)aper, (s)cissors) or '(q)uit' to exit: ").lower()
            
        # Generate computer's choice
        computer_choice = random.choice(computer_choices)

        result = play(user_choice.lower(), computer_choice.lower())
        if result == "":
            continue
        # Display the result
        print(result)
        # Ask if the user wants to play again
        
        play_again = input("Do you want to play again? (yes/no): ")
        match play_again.upper():
            case 'NO' | 'N':
                print("Thanks for playing! Goodbye!")
                break
            case 'YES' | 'Y':
                continue
            case _:
                print("Invalid input. Playing again by default.")
                continue
            # case _:
            #     print("Invalid input. Please enter 'yes' or 'no'.")
                

#return result string
def play(user_choice="", computer_choice="") -> str:
    
    if user_choice == 'quit' or user_choice == 'q':
        print("Thanks for playing! Goodbye!")
        exit()
    if user_choice not in user_choices:
        print("Invalid choice. Please try again.")
        return ""
    
    print(f"Computer chose: {computer_choice}")
    # Compare choices and determine the winner
    if user_choice[0] == computer_choice[0]:
        result = "It's a tie!"
    elif (user_choice in ('rock', 'r') and computer_choice == 'scissors') or \
            (user_choice in ('paper', 'p') and computer_choice == 'rock') or \
            (user_choice in ('scissors', 's') and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "Computer wins!"
    return result

# Start the game
if __name__ == "__main__":
    play_around()

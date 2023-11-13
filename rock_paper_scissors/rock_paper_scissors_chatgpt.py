#using chatGPT to improve my code and here is the Improvements that I have learned from it:

#   break down the play function into a single responsibility function that improve the code 
#   add a validation for the input 
#   improve the readability
#   add the main() function to determine form where the program begins


import random

CHOICES = ["rock", "paper", "scissors"]


def get_user_choice():
    while True:
        user_choice = input("Enter your move (rock, paper, scissors): ").lower()
        if user_choice in CHOICES:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "win"
    else:
        return "lose"


def play_round():
    user_choice = get_user_choice()
    computer_choice = random.choice(CHOICES)
    print(f"Computer chose {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "draw":
        print("It's a draw!")
    elif result == "win":
        print("You win!")
    else:
        print("The computer won!")


def main():
    print("Welcome to Rock, Paper, Scissors game")
    play_round()

    while input("Play again? Press 'y' for yes: ").lower() == "y":
        play_round()


if __name__ == "__main__":
    main()

import random

choices_list = ["rock", "paper", "scissors"]


def play():
    user_choice = input("enter Your move: \n")
    computer_choice = choices_list[random.randint(0, 2)]
    print("computer chose "+computer_choice)
    if user_choice == computer_choice:
        print("draw")
    elif (
        user_choice == "rock" and computer_choice == "scissors"
        or user_choice == "paper" and computer_choice == "rock"
        or user_choice == "scissors" and computer_choice == "paper"
    ):
        print("You Win!")
    else:
        print("The computer won!")


print("Welcome to rock paper scissors game ")
play()
want_to_play = input("Play again? press 'y' for yes \n")
while want_to_play == "y":
    play()
    want_to_play = input("Play again? press 'y' for yes \n")

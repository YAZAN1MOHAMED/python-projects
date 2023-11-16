import random

print(
    "--------------------------------Welcome to the guessing game!--------------------------------\n",
    "the computer will chose a random number and you must guess it, try achieve the lowest attempts",
)

attempts_list = []
def show_score():
    if not attempts_list:
        print("There is no high score yet, play to get the next high score!")
    else:
        print(f"the current high score is {min(attempts_list)}")

play = input("Do you want to play? y/n\n").lower()
if play == "y":
    computer_choice = random.randint(1, 10)
    attempts = 0
    while True:
        try:
            user_choice = int(input("Enter a number between 1 and 10: "))
            if user_choice<1 or  user_choice > 10:
                raise ValueError("Input is not between 1 and 10")
            attempts += 1
            if user_choice == computer_choice:
                print(f"great you got it right!\n number of attempts= {attempts}")
                attempts_list.append(attempts)
                play=input("Want to play again? y/n\n").lower()
                if play=="y":
                    computer_choice = random.randint(1, 10)
                    attempts = 0
                    continue
                else:
                    print("Have a good day!")
                    show_score()
                    break
            elif user_choice > computer_choice:
                print("It's lower")
                continue
            else:
                print("It's higher")
                continue
        except ValueError as err:
            print(err)


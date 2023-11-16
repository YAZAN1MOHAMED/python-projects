# In this game I used only the plan instructions to prompt chat gpt and it done a good job with only one prompt

import random

def guessing_game():
    play_again = input("Do you want to play the guessing game? (yes/no): ").lower()

    if play_again == 'yes':
        attempts = 0
        current_score = float('inf')  # Set initial score to infinity

        while True:
            computer_choice = random.randint(1, 10)

            user_input = input("Guess a number between 1 and 10: ")

            # Check if the input is a valid number
            if not user_input.isdigit():
                print("Please enter a valid number.")
                continue

            user_number = int(user_input)

            # Check if the input is in the valid range
            if not 1 <= user_number <= 10:
                print("Please enter a number between 1 and 10.")
                continue

            attempts += 1

            if user_number > computer_choice:
                print("Your number is greater. Try again!")
            elif user_number == computer_choice:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

                # Update the score if the current attempts are less than the current score
                if attempts < current_score:
                    current_score = attempts
                    print(f"New lowest number of attempts: {current_score}")

                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again != 'yes':
                    break
                else:
                    attempts = 0  # Reset attempts for a new game
            else:
                print("Your number is smaller. Try again!")

    else:
        print("Maybe next time. Goodbye!")

# Run the game
guessing_game()

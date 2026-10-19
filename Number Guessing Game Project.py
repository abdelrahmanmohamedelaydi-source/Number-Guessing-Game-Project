import random

MAX_ATTEMPTS = 7


def display_rules():
    print("Welcome to Number Guessing Game!\n")
    print("I have selected a number between 1 and 100.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it.\n")


def play_game(number):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        # keep asking until the input is valid (attempt number doesn't change)
        while True:
            try:
                guess = int(input(f"Attempt {attempt}/{MAX_ATTEMPTS} - Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.\n")
                continue
            except EOFError:  # no input available, stop instead of looping forever
                print("\nNo input received. Exiting.")
                return
            if 1 <= guess <= 100:
                break
            print("Please enter a number between 1 and 100.\n")

        if guess == number:
            print("\nCongratulations! You guessed the correct number!")
            print(f"You guessed it in {attempt} attempt(s).")
            return
        elif guess < number:
            print("Too Low! Try a higher number.\n")
        else:
            print("Too High! Try a lower number.\n")

    print("\nGame Over!")
    print("The correct number was:", number)


display_rules()
play_game(random.randint(1, 100))
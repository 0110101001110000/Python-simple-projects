from art import logo
from random import randint


# --------------------------------------------------------------------------- #
# NUMBER GUESSING GAME ------------------------------------------------------ #
# --------------------------------------------------------------------------- #


# Functions
def difficulty_input():
    """Treat and return the player difficulty (hard or easy)."""

    options = ["hard", "easy"]
    player_input = input("Choose a difficulty. Type 'hard' or 'easy': ").lower()
    while player_input not in options:
        print("Something wrong, try again.")
        player_input = input("Choose a difficulty. Type 'hard' or 'easy': ").lower()
    return player_input


def set_attempts(difficulty):
    """Return the amount of user attempts (5 to hard or 10 to easy)."""

    if difficulty == "hard":
        return 5
    elif difficulty == "easy":
        return 10
    else:
        return None


def number_input():
    """Get, treat and return the player number."""

    while True:
        number = input("Make a guess: ").replace(" ", "")
        if number.isnumeric():
            number = int(number)
            return number
        else:
            print("Something wrong, try again.")


def compare_both_numbers(random_n, player_n):
    """Compare both of numbers, return the new amount of attempts and a message of each cases."""

    if attempts - 1 <= 0:
        return attempts - attempts, "x"
    elif random_n < player_n:
        return attempts - 1, "+"
    elif random_n > player_n:
        return attempts - 1, "-"
    elif random_n == player_n:
        return attempts - attempts, "="
    else:
        return None


# Greetings
print("Wellcome to the Number Guessing Game.")
print(logo)

# Generate a random number between 1 and 100.
print("I'm thinking of a number between 1 and 100.")
RANDOM_NUMBER = randint(1, 100)

# Get the user choose, game in hard mode or in easy mode.
DIFFICULTY = difficulty_input()

# Set user attempts
attempts = set_attempts(DIFFICULTY)

# Variables
game_loop = True
messages = {
        "+": "Too high.",
        "-": "Too low.",
        "=": "You win!",
        "x": "You lose."
        }

# Init the game
while game_loop:
    # Show user attempts
    print(f"You have {attempts} attempts remaining to guess the number.")

    # Get the user number
    player_number = number_input()

    # Compare with the generated number
    new_attempt, message_index = compare_both_numbers(RANDOM_NUMBER, player_number)

    # Show the message
    print(messages[message_index])

    # Set the new amount of player attempts
    attempts = new_attempt

    # Stop the game
    if attempts <= 0:
        break

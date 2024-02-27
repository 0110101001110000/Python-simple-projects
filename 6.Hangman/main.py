import random
import hangman_art
import hangman_words
# from replit import clear


# --------------------------------------------------------------------------- #
# HANGMAN PART 4 ------------------------------------------------------------ #
# --------------------------------------------------------------------------- #


# Variables
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
stages = hangman_art.stages
logo = hangman_art.logo
display = []
game_loop = True
lives = 6

# Show game logo
print(logo)

# For each letter in the chosen_word, add a "_" to 'display'.
for i in range(len(chosen_word)):
    display.append("_")

# Loop
while game_loop:

    # Get user letter
    guess = input("Guess a letter: ").lower()

    # Clear the terminal
    #clear()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    # Reduce lives
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the world. You lose a life.")
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}")

    # Print current stage
    print(stages[lives])

    # Set the final game result
    if "_" not in display:
        game_loop = False
        print("You win.")
    elif lives <= 0:
        game_loop = False
        print("You lose.")
        print("Answer:", chosen_word)

from art import logo
from time import sleep
from random import choice
# from replit import clear


# --------------------------------------------------------------------------- #
# BLACKJACK PROJECT --------------------------------------------------------- #
# --------------------------------------------------------------------------- #


# Functions


def treat_y_n(player_input):
    while True:
        if player_input == "y":
            return True
        elif player_input == "n":
            return False
        else:
            print("Wrong choice, try again.")


def winner(dealer_cards, dealer_score, player_cards, player_score):
    sleep(1)

    if dealer_score > 21:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("You win.")

    elif player_score > 21:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("You lose.")

    else:
        if dealer_score == player_score:
            print("Draw!")
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")

        elif dealer_score > player_score:
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
            print("You lose.")

        else:
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
            print("You win.")


def play_game():
    sleep(1)

    # Greetings
    print("Welcome to the BlackJack Game.")
    print(logo)

    # Variables
    hand_card_loop = True
    dealer_cards = []
    player_cards = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Sort the carts
    dealer_cards.append(choice(cards))
    dealer_cards.append(choice(cards))
    player_cards.append(choice(cards))
    player_cards.append(choice(cards))

    # Sum the score
    dealer_score = sum(dealer_cards)
    player_score = sum(player_cards)

    # Show current results
    print(f"    Your cards {player_cards}, current score: {player_score}")
    print(f"    Computer's first card: {dealer_cards[0]}")

    # Game loop
    while hand_card_loop:
        # Get if the player will hand a new card
        hand_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        # Treat player input
        hand_card = treat_y_n(hand_card)

        if hand_card:
            # Sort new card
            player_cards.append(choice(cards))

            # Sum the score
            player_score = sum(player_cards)

            # Show the current results
            if player_score <= 21:
                print(f"    Your cards {player_cards}, current score: {player_score}")
                print(f"    Computer's first card: {dealer_cards[0]}")
            else:
                # Declare the winner
                winner(dealer_cards, dealer_score, player_cards, player_score)
                hand_card_loop = False
        else:
            # Declare the winner
            if dealer_score >= 17:
                winner(dealer_cards, dealer_score, player_cards, player_score)
                hand_card_loop = False

        # Sort the dealer card
        if dealer_score < 17:
            dealer_card = choice(cards)
            if (dealer_card == 11) and (sum(dealer_cards) + dealer_card > 21):
                dealer_cards.append(1)
                dealer_score = sum(dealer_cards)
            else:
                dealer_cards.append(dealer_card)
                dealer_score = sum(dealer_cards)

        if dealer_score > 21:
            # Declare the winner
            winner(dealer_cards, dealer_score, player_cards, player_score)
            hand_card_loop = False


# Variables
game_loop = True

# Loop
while game_loop:
    
    game_loop = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    
    # Treat player input
    game_loop = treat_y_n(game_loop)

    if game_loop:
        # Clear terminal
        # clear()

        # Call the game logic
        play_game()

    else:
        sleep(1)
        print("Exiting...")
        sleep(1)
        print("Goodbye.")
        game_loop = False
    
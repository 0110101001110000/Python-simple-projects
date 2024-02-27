from art import logo
# from replit import clear


# --------------------------------------------------------------------------- #
# BLIND AUCTION ------------------------------------------------------------- #
# --------------------------------------------------------------------------- #


# Greetings
print("Welcome to the Blind Auction Program.")
print(logo)

# Variables
highest = 0
dictionary = {}
wrong_choose = False

# loop
while True:
    # Get user inputs
    name = input("What is your name?: ").capitalize()
    bid = float(input("What's your bid?: $"))
    bidders = input("Are there any other bidders? Type yes or no. ").capitalize()

    # Add new user
    dictionary[name] = bid

    # Stop the program
    if bidders == "Yes":
        #clean()
        pass
    elif bidders == "No":
        break
    else:
        print("Something wrong, try again.")
        wrong_choose = True
        break

# Show the results
if not wrong_choose:
    # Set the highest bid
    for user in dictionary:
        bid = dictionary[user]

        if bid > highest:
            winner = user
            highest = bid

    # Show the winner
    print(f"The winner is {winner} with a bid of ${round(highest)}.")

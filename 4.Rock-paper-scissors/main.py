import random


# --------------------------------------------------------------------------- #
# ROCK PAPER SCISSORS ------------------------------------------------------- #
# --------------------------------------------------------------------------- #


# Greetings
print("Welcome to the Rock Paper Scissors.")

# Variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

valid_data = False

# Get user choose
choose = int(input("What do you choose? Type 1 to Rock, 2 for Paper or 3 for Scissors.\n-> "))

# Validate data
if (choose == 1) or (choose == 2) or (choose == 3):
    valid_data = True
else:
    print("Something wrong, try again.")

# Print user choose
if valid_data:
    # Generate the computer chose
    rand_chose = random.randint(1, 3)

    # Print user choose
    if choose == 1:
        print(rock)
    elif choose == 2:
        print(paper)
    else:
        print(scissors)

    # Print computer chose
    print("Computer chose:")
    if rand_chose == 1:
        print(rock)
    elif rand_chose == 2:
        print(paper)
    else:
        print(scissors)

    # Validate who will win
    if (choose == 1) and (rand_chose == 3):
        print("You Win!")
    elif (choose == 2) and (rand_chose == 1):
        print("You Win!")
    elif (choose == 3) and (rand_chose == 2):
        print("You Win!")
    else:
        if choose == rand_chose:
            print("Tie!")
        else:
            print("You Lose!")

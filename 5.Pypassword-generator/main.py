import random


# --------------------------------------------------------------------------- #
# PYPASSWORD GENERATOR ------------------------------------------------------ #
# --------------------------------------------------------------------------- #


# Greetings
print("Welcome to PyPassword Generator.")
print('''
  ad8888888888ba
 dP'         `"8b,
 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
 8  8' `8           "88baadP""""YbaaadP"""YbdP""Yb
 8  8   8              """        """      ""    8b
 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
 8  `"""'       ,d8""
 Yb,         ,ad8"
  "Y8888888888P"
''')

# Inputs
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

# Variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
scores = [0, 0, 0]
win = -1
password = ""

# Generate the random password
for i in range(0, (nr_letters + nr_symbols + nr_numbers)):

    # Get the chance of the letters
    if nr_letters != 0:
        scores[0] = random.randint(1, 100)
    else:
        scores[0] = 0

    # Get the chance of the numbers
    if nr_numbers != 0:
        scores[1] = random.randint(1, 100)
    else:
        scores[1] = 0

    # Get the chance of the symbols
    if nr_symbols != 0:
        scores[2] = random.randint(1, 100)
    else:
        scores[2] = 0

    # Compare the results and add in the password
    if (scores[0] >= scores[1]) and (scores[0] >= scores[2]):
        rand_letter = random.randint(0, len(letters) - 1)
        password += letters[rand_letter]
        nr_letters -= 1
    elif (scores[1] >= scores[0]) and (scores[1] >= scores[2]):
        rand_number = random.randint(0, len(numbers) - 1)
        password += numbers[rand_number]
        nr_numbers -= 1
    else:
        rand_number = random.randint(0, len(symbols) - 1)
        password += symbols[rand_number]
        nr_symbols -= 1

# Show results
print(password)

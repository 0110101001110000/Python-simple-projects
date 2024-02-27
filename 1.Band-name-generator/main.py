from art import logo


# --------------------------------------------------------------------------- #
# Band Name Generator ------------------------------------------------------- #
# --------------------------------------------------------------------------- #


# Create a greeting for your program.
print("Welcome to the Band Name Generator.")
print(logo)

# Ask the user for the city that they grew up in.
city_name = input("What's name of the city you grew up in?\n-> ")

# Ask the user for the name of a pet.
pet_name = input("What's name of your pet?\n-> ")

# Combine the name of their city and pet and show them their band name.
band_name = city_name + pet_name
print("Congratulations! your band name is " + band_name + ".")

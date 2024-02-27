from art import logo


# --------------------------------------------------------------------------- #
# TIP CALCULATOR ------------------------------------------------------------ #
# --------------------------------------------------------------------------- #


# Greeting
print("Welcome to the Tip Calculator.")
print(logo)

# Get user values
total = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate how much each people should pay
percentage = ((percentage / 100) * total)
final_amount = ((total + percentage) / people)
final_amount = "{:.2f}".format(final_amount)

print(f"Each people should pay: ${final_amount}")

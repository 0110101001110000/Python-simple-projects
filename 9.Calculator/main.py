from art import logo


# --------------------------------------------------------------------------- #
# Calculator ---------------------------------------------------------------- #
# --------------------------------------------------------------------------- #


# Functions


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Variables
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Calculating:


def calculator():
    # Greetings
    print("Welcome to the Pythonista Calculator.")
    print(logo)

    # Get first number
    num1 = float(input("What's the first number?: "))

    # Show the operations
    for operation in operations:
        print(operation)

    # Get operation to work
    operation_symbol = input("Pick an operation from the line above: ")
    operation_symbol = operation_symbol.replace(" ", "")

    # Get second number
    num2 = float(input("What's the second number?: "))

    # Set the answer
    calculation_function = operations[operation_symbol]
    previous_answer = calculation_function(num1, num2)

    # Show result
    print(f"{num1} {operation_symbol} {num2} = {previous_answer}")

    # Loop:
    while True:
        # Get if will continue calculating
        should_continue = input(f"Pick 'y' to continue calculating with {previous_answer}, or type 'n' to start a new calculation, or type 'q' to quit: ").lower()
        should_continue = should_continue.replace(" ", "")
        should_continue = should_continue.lower()

        if should_continue == "y":
            # Get another operation to work
            operation_symbol = input("Pick another operation: ")
            operation_symbol = operation_symbol.replace(" ", "")

            # Get third number
            num3 = float(input("What's the next number?: "))

            # Set the answer
            calculation_function = operations[operation_symbol]
            last_answer = calculation_function(previous_answer, num3)

            # Show result
            print(f"{previous_answer} {operation_symbol} {num3} = {last_answer}")

            previous_answer = last_answer

        elif should_continue == "n":
            calculator()
        else:
            print("Exiting...")
            print("Goodbye.")
            break


# Run main code
calculator()

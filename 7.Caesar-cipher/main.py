from art import logo


# --------------------------------------------------------------------------- #
# CAESAR CIPHER ------------------------------------------------------------- #
# --------------------------------------------------------------------------- #


# Greetings
print(logo)

# Variables
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
continue_loop = True


def ceasar(text, shift, direction):
    # Output variable
    cipher_text = ""

    for letter in text:
        # Variables
        alphabet_len = (len(alphabet) - 1)

        if letter in alphabet:
            alphabet_index = alphabet.index(letter)

            # Set new letter index
            if direction == "encrypt":
                alphabet_index = alphabet_index + shift
                while alphabet_index > alphabet_len:
                    alphabet_index = alphabet_index - alphabet_len
                    alphabet_index = alphabet_index - 1
            else:
                alphabet_index = alphabet_index - shift
                while alphabet_index < 0:
                    alphabet_index = alphabet_len + alphabet_index
                    alphabet_index = alphabet_index + 1

            # Add cipher letter
            cipher_text += alphabet[alphabet_index]

        else:
            cipher_text += letter

    # Show result
    print(f"The encoded text is {cipher_text}")


# Loop
while continue_loop:
    # User inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n-> ").lower()
    text = input("Type your message:\n-> ").lower()
    shift = int(input("Type the shift number:\n-> "))

    # Encrypt
    if direction == "encode":
        ceasar(text, shift, "encrypt")
    # Decrypt
    elif direction == "decode":
        ceasar(text, shift, "decrypt")
    else:
        print(f'"{direction}" is not a valid option.')

    # Stop loop
    continue_loop_choose = input("Type 'yes' if"
                                 " you want to go again. Otherwise type 'no'.\n-> ").lower()
    if continue_loop_choose == "yes":
        pass
    else:
        print("Goodbye.")
        break

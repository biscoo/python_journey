# Caesar Cipher Implementation in Python

# Alphabet list used for shifting characters
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Ask user whether to encode or decode
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# Ask for the message to process
text = input("Type your message:\n").lower()
# Ask for the shift number
shift = int(input("Type the shift number:\n"))


def caesar(direction, text, shift):
    """
    Caesar cipher function.
    Shifts characters in the input text based on the shift amount.
    
    Parameters:
        direction (str): 'encode' to encrypt, 'decode' to decrypt
        text (str): the message to encode/decode
        shift (int): the number of positions to shift
    """
    temp_word = ''

    for char in text:
        if char in alphabet:
            if direction == "encode":
                temp_word += alphabet[(alphabet.index(char) + shift) % 26]
            elif direction == "decode":
                temp_word += alphabet[(alphabet.index(char) - shift) % 26]
        else:
            # Keep non-alphabet characters (spaces, punctuation, etc.)
            temp_word += char

    # Print the result
    if direction == 'encode':
        print(f"The encoded word of ({text}) is: {temp_word}")
    elif direction == 'decode':
        print(f"The decoded word of ({text}) is: {temp_word}")


# Call the Caesar cipher function
caesar(direction, text, shift)

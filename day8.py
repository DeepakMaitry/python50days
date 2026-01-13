# function structure
"""
def my_function():
    # Do this
    # Then do this
    # Finally do this
my_function()
"""
"""
def my_function2(something):
    # do this with something
    
"""

"""

def greet():
    print("Hello")
    print("how do you do?")
    print("Isn't the weather nice?")


greet()
"""

# Functions that allows for inputs
"""

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Deepak")  # here Deepak is Argument and name is Parameter

"""

"""
# Functions with more that 1 input


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Deepak", "Mumbai")  # here Deepak and Mumbai are Arguments and name and location are Parameters
"""

# or you can directly do this def my_function(a = 1, b = 2, c = 3):
# or also def my_function(1, 2, 3):

"""
def my_function(a=1, b=2, c=3):
    print(a + b + c)

my_function()
"""

# or similiarly

"""
def my_function(a, b, c):
    print(a+b+c)
    
my_function(a=1, b = 2, c = 3)
"""

import day8art

print(day8art.logo)

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.


# hello 2

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


"""
fruits = ["Apple", "Peach", "Pear"]
fruits.index("Apple")
"""

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.


# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.


# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift_amount *= -1
                
    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d text is {output_text}")


should_continue = True

while should_continue:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
        
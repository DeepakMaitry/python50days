"""

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
import random

chosen_word = random.choice(word_list)
print(chosen_word)
print("\n")
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-1: - Use a while loop to let the user guess again

no_of_lives = len(chosen_word)
guess = ""
while no_of_lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        print("Right")
    else:
        print("Wrong")
        no_of_lives -= 1
        print(f"You have {no_of_lives} lives left")
        if no_of_lives == 0:
            print("You lose")
            break



# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

for letter in chosen_word:
  print("_", end=" ")

print("\n")
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")



# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display = []
for _ in range(len(chosen_word)):
  display.append("_")

for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter
print(display)

"""

import random

# import hangman_words
from hangman_words import word_list

# import hangman_art
from hangman_art import stages, logo


'''
stages = [  # using raw string ideal for ascii art
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]
'''

word_list = ["aardvark", "baboon", "camel"]

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:

    print(
        f"****************************{lives}/6 LIVES LEFT****************************"
    )

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You already guessed this letter.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if lives == 0:
        game_over = True
        print(
            f"*****************************IT WAS {chosen_word}! YOU LOSE**********************************"
        )

    if "_" not in display:
        game_over = True
        print("*****************************YOU WIN*******************************")

    print(stages[lives])

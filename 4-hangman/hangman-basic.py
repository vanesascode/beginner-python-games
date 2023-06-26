import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(
        word
    )  # sets the unique letters into a list between curly brackets
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # the letters the user has been guessing

    # getting user input:
    while len(word_letters) > 0:
        # letters used:
        print("You have used these letters: ", " ".join(used_letters))

        # what current word is (e.g W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")  # this is printing an empty line

        elif user_letter in used_letters:
            print("\nYou have already used that character. Guess another letter.")

        else:
            print("\nInvalid character. Please try again.")

    print("Yes! You guessed the word", word, "!!")


hangman()

import random

# You must guess the computer's secret name:


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, try higher.")
        elif guess > random_number:
            print("Sorry, try lower.")
    print(f"Great! Yes, it was number: {random_number}")


guess(20)

# Think of a secret number The computer must guess your secret number:


def computer_guess(x):
    print("==== Now think of a secret number between 1 and {x}.")
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:  # if low and high were the same number it would give an error.
            guess = random.randint(low, high)
        else:
            guess = low  # or it could be = high, since they are the same number.
        feedback = input(f"Is {guess} too high (A) or too low (B), or correct (C)? ")
        if feedback == "a":
            high = guess - 1
        elif feedback == "b":
            low = guess + 1
    print(f"==== Yeah, the computer guessed your number, the number: {guess}")


computer_guess(20)

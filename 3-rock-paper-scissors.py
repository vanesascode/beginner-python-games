import random


def play():
    valid_choices = ["r", "p", "s"]
    user = input("Choose 'r' for rock, 'p' for paper, 's' for scissors: ")
    while user not in valid_choices:
        print("==== Try again! ====")
        user = input("==== Choose 'r' for rock, 'p' for paper, or 's' for scissors: ")
    computer = random.choice(["r", "p", "s"])
    while user == computer:
        print("It's a tie")
        print("==== Try again! ====")
        user = input("==== Choose 'r' for rock, 'p' for paper, or 's' for scissors: ")

    if is_win(user, computer):
        return f"You won, because the computer chose '{computer}'!"

    return f"You lost, because the computer chose '{computer}'!"


def is_win(player, opponent):
    # it returns true if player wins
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


print(play())

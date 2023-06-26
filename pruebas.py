import string


word = "alfonso".upper()

word_letters = set(word)

print(word_letters)
# {'F', 'L', 'A', 'O', 'N', 'S'}

print("You have used these letters ", "-".join(word))  # 2 parameters!
# A L F O N S O

print("You have used these letters ", " ".join(word_letters))
# O A F S N L

palabra1 = "casita"
palabra2 = "as"
word_list = [letter if letter in palabra2 else "-" for letter in palabra1]
print("  ".join(word_list).upper())

word2 = set(string.ascii_uppercase)

print(word2)
# {'M', 'U', 'Q', 'V', 'G', 'P', 'B', 'W', 'Y', 'F', 'Z', 'I', 'L', 'R', 'O', 'D', 'A', 'E', 'N', 'X', 'T', 'K', 'H', 'C', 'J', 'S'}

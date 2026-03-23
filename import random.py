import random

def to_roman(num):
    roman_numerals = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
        11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV',
        16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX'
    }
    return roman_numerals.get(num, str(num))

print("Hi! Let's play a guess-the-number game.")
secret = random.randint(1, 20)

while True:
    guess_str = input("Guess a number 1-20: ")
    if not guess_str.strip():
        print("Please type a number.")
        continue
    try:
        guess = int(guess_str)
    except ValueError:
        print("Enter an integer.")
        continue
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print(f"You got it! The number was {to_roman(secret)}. 🎉")
        break

print("Rolling a dice...")
roll = random.randint(1, 6)
print("You rolled:", to_roman(roll))
import random

def to_roman(num):
    roman_numerals = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
        11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV',
        16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX'
    }
    return roman_numerals.get(num, str(num))

print("Hi! Let's play a guess-the-number game.")
secret = random.randint(1, 20)

while True:
    guess_str = input("Guess a number 1-20: ")
    if not guess_str.strip():
        print("Please type a number.")
        continue
    try:
        guess = int(guess_str)
    except ValueError:
        print("Enter an integer.")
        continue
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print(f"You got it! The number was {to_roman(secret)}. 🎉")
        break

print("Rolling a dice...")
roll = random.randint(1, 6)
print("You rolled:", to_roman(roll))
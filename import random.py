import random

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
        print("You got it! 🎉")
        break

print("Rolling a dice...")
roll = random.randint(1, 6)
print("You rolled:", roll)
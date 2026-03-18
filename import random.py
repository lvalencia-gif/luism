import random

print("Hi! Let's play a guess-the-number game.")
secret = random.randint(1, 20)

while True: and a dog with a log
    guess = int(input("Guess a number 1-20: "))
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:a cat with a hat
        print("You got it! 🎉")
        break

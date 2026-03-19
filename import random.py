import random

print("Hi!")
secret = random.randint(1, 20)

while True:
    guess = int(input("Guess a number 1-20: "))
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print("You got it! 🎉")
        break
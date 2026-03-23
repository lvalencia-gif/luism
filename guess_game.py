import random

ROMAN_PAIRS = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]


def to_roman(num: int) -> str:
    if not isinstance(num, int) or num <= 0:
        raise ValueError('Number must be a positive integer')
    if num > 3999:
        return str(num)

    result = []
    for value, symbol in ROMAN_PAIRS:
        while num >= value:
            result.append(symbol)
            num -= value
    return ''.join(result)


def read_int(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        answer = input(prompt).strip()
        if not answer:
            print('Please type a number.')
            continue

        if answer.lower() in ['q', 'quit', 'exit']:
            raise KeyboardInterrupt

        try:
            value = int(answer)
        except ValueError:
            print('Enter an integer.')
            continue

        if value < min_value or value > max_value:
            print(f'Enter a number between {min_value} and {max_value}.')
            continue

        return value


def play_game() -> None:
    print("Hi! Let's play a guess-the-number game.")
    secret = random.randint(1, 1000)

    while True:
        try:
            guess = new_func()
        except KeyboardInterrupt:
            print('\nGame exited. Bye!')
            return

        if guess < secret:
            print('Too low.')
        elif guess > secret:
            print('Too high.')
        else:
            print(f'You got it! The number was {to_roman(secret)}. 🎉')
            break

    print('\nRolling a dice...')
    roll = random.randint(1, 6)
    print('You rolled:', to_roman(roll))

def new_func():
    guess = read_int('Guess a number 1-1000 (or q to quit): ', 1, 1000)
    return guess


if __name__ == '__main__':
    while True:
        play_game()
        again = input('Play again? (y/n): ').strip().lower()
        if again not in ('y', 'yes'):
            print('Thanks for playing!')
            break
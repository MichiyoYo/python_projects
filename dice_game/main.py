import random


def check_valid(input_str):
    return (input_str in ['n', 'y'], input_str)


def roll_the_dice():
    play = check_valid(input('Roll the dice?(y/n): ').lower())
    while (play[0] and play[1] == 'y'):
        d1, d2 = random.choices([1, 2, 3, 4, 5, 6], k=2)
        print(f"({d1}, {d2})")
        play = check_valid(input('Roll the dice?(y/n): ').lower())

    if not play[0]:
        print('Invalid input')
        roll_the_dice()
    else:
        print('Ok bye!')


roll_the_dice()

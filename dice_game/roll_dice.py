import random
from validators import input_validators


def roll_the_dice():
    while True:
        play = input('Roll the dice?(y/n): ').lower()
        try:
            play_choice = input_validators.is_valid_char(play, ['y', 'n'])
        except ValueError as err:
            print(err)
        else:
            if play_choice == 'n':
                print('Ok bye!')
                break
            d1, d2 = random.choices([1, 2, 3, 4, 5, 6], k=2)
            print(f"({d1}, {d2})")

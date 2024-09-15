import random
from validators import input_validators


def roll_the_dice():
    play = input('Roll the dice?(y/n): ').lower()
    try:
        choice = input_validators.is_valid_char(play, ['y', 'n'])
    except ValueError as err:
        print(err)
    else:
        print(choice)

# def roll_the_dice():
#     play = input_validators.is_valid_char(
#         input('Roll the dice?(y/n): ').lower(), ['y', 'n'])
#     while (play[0] and play[1] == 'y'):
#         d1, d2 = random.choices([1, 2, 3, 4, 5, 6], k=2)
#         print(f"({d1}, {d2})")
#         play = input_validators.is_valid_char(
#             input('Roll the dice?(y/n): ').lower(), ['y', 'n'])

#     if not play[0]:
#         print('Invalid input')
#         roll_the_dice()
#     else:
#         print('Ok bye!')

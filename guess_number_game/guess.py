import random
from validators import input_validators


def guess_the_number():
    cpu_pick = random.randint(1, 100)
    print(cpu_pick)
    count = 0
    while True:
        count += 1
        try:
            player_pick = input_validators.is_num(
                input('Guess the Number (between 1 and 100): '))
        except ValueError as err:
            print(err)
        else:
            if player_pick < cpu_pick:
                print("Too low!")
            elif player_pick > cpu_pick:
                print("Too high!")
            else:
                break

    print(f"Congratulations! You guessed the number in {count} attempts")

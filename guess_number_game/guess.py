import random

cpu_pick = random.randint(1, 101)

player_pick = int(input('Guess the Number (between 1 and 100): '))
count = 0
while (cpu_pick != player_pick):
    if player_pick < cpu_pick:
        print("Too low!")
    if player_pick > cpu_pick:
        print("Too high!")
    player_pick = int(input('Guess the Number (between 1 and 100): '))
    count += 1

print(f"Congratulations! You guessed the number in {count} attempts")

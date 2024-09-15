from dice_game import roll_dice
from guess_number_game import guess

game = input("""
What game do you want to play?
1) Roll the dice
2) Guess the number
""")

if game == '1':
    roll_dice.roll_the_dice()
if game == '2':
    guess.guess_the_number()

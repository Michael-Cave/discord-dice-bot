import random

# Basic Dice class
class Dice:
    def __init__(self, num_dice, sides):
        self._num_dice = num_dice
        self._sides = sides
        self.results = []

    # Rolls the dice
    def roll_dice(self):
        for i in range(self._num_dice):
            self.results.append(random.randrange(1, self._sides + 1))
        return self.results
    
def test_case():
    d1 = Dice(10, 6)
    rolled_dice = d1.roll_dice()
    print(rolled_dice)

test_case()
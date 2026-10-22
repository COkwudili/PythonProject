from random import random

from utils import find_max

numbers = [10, 3, 6, 2]
max = find_max(numbers)
print (max)

import ecommerce.__init__
ecommerce.__init__.calc_shipping()


import random

class Dice :
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print (dice.roll())

from pathlib import Path

path = Path("ecommerce")
print (path.exists())

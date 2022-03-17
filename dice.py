import random

class Dice:
  def __init__(self, low, high):
    self.low = low
    self.high = high

  def roll(self):
    return random.randint(self.low, self.high)
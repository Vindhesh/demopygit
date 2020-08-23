import random

class Dice:
    def __init__(self):
        self.side  = 0

    def throw(self):
        self.side = random.randint(1,6)

    def get_value(self):
        return self.side
    
my_dice = Dice()
for i in range(1, 11):
    my_dice.throw()
    print("The dice value is: ", my_dice.get_value())

    
 

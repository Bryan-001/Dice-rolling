import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        third = random.randint(1, 6)
        return first, second, third

    def name(self):
        print("Hi roller, such a Flex!BIGUP")

dice = Dice()

print(dice.roll())
dice.name()

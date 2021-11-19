import random

class Spell:
    def __init__(self, name, dmg, cost):
        self.name = name
        self.dmg = dmg
        self.cost = cost


    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)  

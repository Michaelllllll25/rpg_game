import random

class Spell:
    def __init__(self, name: str, dmg: int, cost: int) -> None:
        self.name = name
        self.dmg = dmg
        self.cost = cost

    def generate_damage(self):
        """Generates a damage amount
        
        Returns:
            A number between -15 and 15
        """
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)  # gets a number that is in the range of -15 and 15

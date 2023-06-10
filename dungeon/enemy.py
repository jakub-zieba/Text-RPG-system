import random


class Enemy:
    """Simple enemy class"""

    def __init__(self, min_atk: int = 200, max_atk: int = 300, description: str = ""):
        self.min_atk = min_atk
        self.max_atk = max_atk
        self.description = description

    # add some methods like combat handling and loot drop maby
 
    def attack(self):
        return(random.randint(self.min_atk, self.max_atk))
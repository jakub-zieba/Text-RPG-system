import random
from collections import defaultdict


class Player:
    """Class representing a player """
    def __init__(self):
        # base parameters for player, stamina and mana are not used atm
        self.health: int = 2000
        self.min_base_damage: int = 100
        self.max_base_damage: int = 200
        # self.stamina: int = 500
        # self.mana: int = 500
        # those can be modified by equipment changes
        self.min_damage = self.min_base_damage
        self.max_damage = self.max_base_damage
        self.backpack = defaultdict(lambda: 0)

    def grab_item(self, item) -> None:
        self.backpack[item] += 1

    def drop_item(self, item):
        if self.backpack[item] == 1:
            self.backpack.pop(item)
            return item
        if self.backpack[item] >= 1:
            self.backpack[item] -= 1
            print("You dropped:", item.name, "amount left:", self.backpack[item])
            return item
        else:
            print("No such thing in your backpack.")
            return None

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)
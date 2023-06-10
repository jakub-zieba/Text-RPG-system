import random
from collections import defaultdict

from dungeon.item import BaseItem


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
        self.backpack: dict[BaseItem, int] = defaultdict(lambda: 0)
        self.items_equipped: list[BaseItem] = []
        # statistics system is to be used later
        self.statistics = {
            "strength": 5,
            "agility": 5,
            "wisdom": 5,
            "luck": 5,
            "vitality": 5
        }

    def grab_item(self, item: BaseItem) -> None:
        self.backpack[item] += 1

    def drop_item(self, item: BaseItem) -> BaseItem | None:
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

    def get_backpack_content(self) -> dict:
        return dict(self.backpack)

    def equip_item(self, item: BaseItem) -> None:
        if not item.is_equipable:
            print("You can't equip this item")
            pass
        if item not in self.backpack.keys():
            print("No such item in your backpack, therefore you can't equip it")
            pass
        if self.backpack[item] > 1:
            self.backpack[item] -= 1
        else:
            self.backpack.pop(item)
        self.items_equipped.append(item)
        item.change_stats(self)

    def get_equipment(self):
        return self.items_equipped

    def attack(self) -> int:
        return random.randint(self.min_damage, self.max_damage)

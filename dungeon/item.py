"""All items need to have these 4 fields
is_equipable: bool
is_consumable: bool
name: str
description: str"""
from abc import abstractmethod


class BaseItem:
    @abstractmethod
    def __init__(self):
        self.is_equipable: bool = False
        self.is_consumable: bool = False
        self.name: str = ""
        self.description: str = ""

    @abstractmethod
    def change_stats(self, player: "Player"):
        raise NotImplemented

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class ConsumableHealthPotion(BaseItem):
    """Health regenarating potion, consumable item,
    consume to regain HP"""
    def __init__(self) -> None:
        self.name = "Health Potion"
        self.description = """A small bottle containing ruby-red, crystal-clear liquid. 
            You will regain 500 HP after drinking it"""
        self.healing_value = 500
        self.is_equipable = False
        self.is_consumable = True


class EquipableSword(BaseItem):
    def __init__(self):
        self.name = "Short straight sword"
        self.description = """You can beat goblins and humans with it, 
            but against big monsters it just won't do. Great for lvl 1 crooks."""
        self.min_attack_damage = 250
        self.max_attack_damage = 300
        self.is_equipable = True
        self.is_consumable = False

    def change_stats(self, player: "Player"):
        player.min_damage = self.min_attack_damage
        player.max_damage = self.max_attack_damage

"""All items need to have these 4 fields
is_equippable: bool
is_consumable: bool
name: str
description: str"""


class BaseItem:
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
        self.is_equippable = False
        self.is_consumable = True


class EquippableSword(BaseItem):
    def __init__(self):
        self.name = "Short straight sword"
        self.description = """You can beat goblins and humans with it, 
            but against big monsters it just won't do. Great for lvl 1 crooks."""
        self.min_attack_damage = 250
        self.max_attack_damage = 300
        self.is_equippable = True
        self.is_consumable = False

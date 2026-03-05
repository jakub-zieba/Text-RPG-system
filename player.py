from collections import defaultdict

from combat_entity import CombatEntity, _STATS
from dungeon.item import BaseItem

_DEFAULT_PLAYER_STATS = {
    _STATS.strength: 20,   # min_damage=100, max_damage=200
    _STATS.vitality: 100,  # max_health=2000
    _STATS.agility: 5,     # dodge_chance=2.5%
    _STATS.wisdom: 5,
    _STATS.luck: 5,        # crit_chance=2.5%
}


class Player(CombatEntity):
    """Class representing a player."""

    def __init__(self, base_stats: dict[_STATS, int] | None = None):
        super().__init__(base_stats if base_stats is not None else _DEFAULT_PLAYER_STATS)
        self.backpack: dict[BaseItem, int] = defaultdict(lambda: 0)
        self.items_equipped: list[BaseItem] = []

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

    def get_backpack_content(self) -> None:
        if not self.backpack:
            print("Your backpack is empty.")
            return

        print("You are browsing your backpack and you see:")
        for item, qty in self.backpack.items():
            print(f"[{item.name}] x{qty}")
            print(f"  {'description':<20}: {item.description.strip()}")
            extra = {k: v for k, v in vars(item).items() if k not in ("name", "description")}
            for prop, val in extra.items():
                print(f"  {prop.replace('_', ' '):<20}: {val}")

    def equip_item(self, item: BaseItem) -> None:
        if not item.is_equipable:
            print("You can't equip this item")
            return
        if item not in self.backpack.keys():
            print("No such item in your backpack, therefore you can't equip it")
            return
        if self.backpack[item] > 1:
            self.backpack[item] -= 1
        else:
            self.backpack.pop(item)
        self.items_equipped.append(item)
        item.change_stats(self)

    def get_equipment(self):
        return self.items_equipped

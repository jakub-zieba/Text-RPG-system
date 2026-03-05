from abc import abstractmethod

from combat_entity import CombatEntity, _STATS


class Enemy(CombatEntity):
    """Base class for all enemies.

    Each subclass must define a _BASE_STATS class attribute and set self.name
    in its __init__.
    """

    _BASE_STATS: dict[_STATS, int] = {}

    @abstractmethod
    def __init__(self, description: str = "") -> None:
        super().__init__(self._BASE_STATS)
        self.description = description

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class Skeleton(Enemy):
    _BASE_STATS = {
        _STATS.strength: 4,   # min_damage=20, max_damage=40
        _STATS.vitality: 80,  # max_health=1600
        _STATS.agility: 3,    # dodge_chance=1.5%
        _STATS.wisdom: 1,
        _STATS.luck: 2,       # crit_chance=1%
    }

    def __init__(self, description: str = "Lvl 1. skeleton warrior equipped with rusty sword"):
        super().__init__(description)
        self.name = "Skeleton"

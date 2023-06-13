import random
from abc import abstractmethod


class Enemy:
    """Simple enemy class"""

    @abstractmethod
    def __init__(self, min_atk: int = 200, max_atk: int = 300, description: str = ""):
        self.min_atk = min_atk
        self.max_atk = max_atk
        self.description = description

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name
    # add some methods like combat handling and loot drop maby

    @abstractmethod
    def attack(self) -> int:
        raise NotImplemented


class Skeleton(Enemy):
    def __init__(
        self,
        min_atk: int = 20,
        max_atk: int = 30,
        description: str = "Lvl 1. skeleton warrior equipped with rusty sword"
    ):
        super().__init__(min_atk, max_atk, description)

    def attack(self) -> int:
        return random.randint(self.min_atk, self.max_atk)

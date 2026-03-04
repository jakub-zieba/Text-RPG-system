import random

_STATS = ("strength", "vitality", "agility", "wisdom", "luck")


class CombatEntity:
    """Base class for all combat participants (player and enemies).

    All combat numbers are derived from five base stats:
        strength  -> min/max physical damage
        vitality  -> max health
        agility   -> dodge chance
        wisdom    -> reserved for mana / spell power
        luck      -> crit chance

    Equipment and effects write to stat_bonuses, which are summed with
    base_stats before any derived property is computed.
    """

    def __init__(self, base_stats: dict[str, int]) -> None:
        self.base_stats: dict[str, int] = {s: base_stats.get(s, 1) for s in _STATS}
        self.stat_bonuses: dict[str, int] = {s: 0 for s in _STATS}
        self.current_health: int = self.max_health

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _stat(self, name: str) -> int:
        return self.base_stats[name] + self.stat_bonuses[name]

    # ------------------------------------------------------------------
    # Derived stats (read-only properties)
    # ------------------------------------------------------------------

    @property
    def max_health(self) -> int:
        return self._stat("vitality") * 20

    @property
    def min_damage(self) -> int:
        return self._stat("strength") * 5

    @property
    def max_damage(self) -> int:
        return self._stat("strength") * 10

    @property
    def crit_chance(self) -> float:
        """Crit chance as a percentage (luck * 0.5)."""
        return self._stat("luck") * 0.5

    @property
    def dodge_chance(self) -> float:
        """Dodge chance as a percentage (agility * 0.5)."""
        return self._stat("agility") * 0.5

    # ------------------------------------------------------------------
    # Combat actions
    # ------------------------------------------------------------------

    def attack(self) -> int:
        """Roll damage; doubles on crit."""
        damage = random.randint(self.min_damage, self.max_damage)
        if random.random() < self.crit_chance / 100:
            damage *= 2
        return damage

    def take_damage(self, amount: int) -> int:
        """Apply incoming damage after a dodge roll.

        Returns the actual damage taken (0 if dodged).
        """
        if random.random() < self.dodge_chance / 100:
            return 0
        self.current_health = max(0, self.current_health - amount)
        return amount

    def is_alive(self) -> bool:
        return self.current_health > 0

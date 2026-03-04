# Combat System

All combat participants — players and enemies — share a common base class `CombatEntity` ([combat_entity.py](../../combat_entity.py)). This ensures the same rules govern both sides of every fight.

## CombatEntity

`CombatEntity` holds two stat dictionaries:

- `base_stats` — intrinsic values set at creation, defined per class
- `stat_bonuses` — additive bonuses applied by equipment or effects, start at zero

All derived combat values are computed from `base_stats[stat] + stat_bonuses[stat]`.

## Base Stats

| Stat | Governs |
|---|---|
| `strength` | Physical damage output |
| `vitality` | Maximum health |
| `agility` | Dodge chance |
| `wisdom` | Reserved — mana / spell power (TBC) |
| `luck` | Critical hit chance |

Stats use a 1–100 integer scale.

## Derived Stats

| Derived value | Formula |
|---|---|
| `max_health` | `vitality × 20` |
| `min_damage` | `strength × 5` |
| `max_damage` | `strength × 10` |
| `crit_chance` | `luck × 0.5` % |
| `dodge_chance` | `agility × 0.5` % |

Derived stats are read-only properties — they cannot be set directly.

## Combat Flow

Each round consists of one `attack()` call from each participant, resolved in sequence.

### Attack resolution
1. Roll damage in `[min_damage, max_damage]`
2. Check for critical hit — if `random() < crit_chance / 100`, damage is doubled
3. Pass the result to the target's `take_damage(amount)`

### Damage resolution
1. Check for dodge — if `random() < dodge_chance / 100`, the hit is ignored entirely and `0` is returned
2. Otherwise subtract from `current_health` (floored at 0)
3. Return actual damage taken

### End condition
A participant is eliminated when `is_alive()` returns `False` (`current_health == 0`).

Combat ends when all enemies in the room are eliminated. The player cannot leave a room with living enemies.

## Player

Defined in [player.py](../../player.py). `Player.__init__` accepts an optional `base_stats` dict; if omitted, the defaults below are used. Multiple players may be instantiated with different stat builds.

Default player stats:

| Stat | Value | Effect |
|---|---|---|
| `strength` | 20 | 100–200 base damage |
| `vitality` | 100 | 2000 max health |
| `agility` | 5 | 2.5% dodge chance |
| `wisdom` | 5 | — |
| `luck` | 5 | 2.5% crit chance |

## Enemies

Defined in [dungeon/enemy.py](../../dungeon/enemy.py). Each enemy class encapsulates its own `_BASE_STATS` as a class attribute. Adding a new enemy type requires only defining `_BASE_STATS`, a `name`, and optionally a `description`.

### Skeleton

| Stat | Value | Effect |
|---|---|---|
| `strength` | 4 | 20–40 damage |
| `vitality` | 5 | 100 max health |
| `agility` | 3 | 1.5% dodge chance |
| `wisdom` | 1 | — |
| `luck` | 2 | 1% crit chance |

## Equipment

Equipment items extend `BaseItem` and implement `change_stats(entity)`. When equipped, `change_stats` is called immediately and writes to `entity.stat_bonuses`. Because derived stats recompute from the updated bonuses, all effects are applied instantly and consistently for both players and enemies.

### Example — Short Straight Sword
Grants `+30 strength` via `stat_bonuses["strength"]`.

Effect on default player: strength rises from 20 → 50, giving 250–500 damage.

Consumable items (e.g. `ConsumableHealthPotion`) modify `current_health` directly and do not interact with `stat_bonuses`.

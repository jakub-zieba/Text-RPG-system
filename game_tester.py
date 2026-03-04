from dungeon.generators import generate_dungeon, visualize_dungeon
from dungeon.item import EquipableSword, ConsumableHealthPotion
from dungeon.enemy import Skeleton
import player

"""
This scripts is for basic game functionality testing
"""

# temporary solution for game sizing
sd_size = input("Provide max dungeon depth (like 10 or 25, etc)")
while not sd_size.isnumeric():
    sd_size = input("Provide max dungeon depth, it must be number (like 10 or 25, etc)")
max_dungeon_size: int = int(sd_size)

dungeon_map = generate_dungeon(max_dungeon_size//2, max_dungeon_size)
print("Map:\n", visualize_dungeon(dungeon_map))


player = player.Player()

potion = ConsumableHealthPotion()
second_potion = ConsumableHealthPotion()
small_sword = EquipableSword()

player.grab_item(potion)
player.grab_item(small_sword)
print("Backpack:", player.get_backpack_content())
player.equip_item(small_sword)
print("Equipped stuff:", player.get_equipment())
print("Backpack after equipping sword:", player.get_backpack_content())
player.grab_item(second_potion)
print("Backpack after getting second potion:", player.get_backpack_content())

# --- Combat test ---
print("\n=== Combat Test ===")
skeleton = Skeleton()
print(f"Player  HP: {player.current_health}/{player.max_health}  dmg: {player.min_damage}-{player.max_damage}  crit: {player.crit_chance}%  dodge: {player.dodge_chance}%")
print(f"Skeleton HP: {skeleton.current_health}/{skeleton.max_health}  dmg: {skeleton.min_damage}-{skeleton.max_damage}  crit: {skeleton.crit_chance}%  dodge: {skeleton.dodge_chance}%")
print()

round_num = 1
while player.is_alive() and skeleton.is_alive():
    p_dmg = player.attack()
    taken_by_skeleton = skeleton.take_damage(p_dmg)
    if taken_by_skeleton == 0:
        print(f"Round {round_num}: Player attacks for {p_dmg} — Skeleton dodged!")
    else:
        print(f"Round {round_num}: Player attacks for {taken_by_skeleton} — Skeleton HP: {skeleton.current_health}/{skeleton.max_health}")

    if not skeleton.is_alive():
        break

    s_dmg = skeleton.attack()
    taken_by_player = player.take_damage(s_dmg)
    if taken_by_player == 0:
        print(f"Round {round_num}: Skeleton attacks for {s_dmg} — Player dodged!")
    else:
        print(f"Round {round_num}: Skeleton attacks for {taken_by_player} — Player HP: {player.current_health}/{player.max_health}")

    round_num += 1

winner = "Player" if player.is_alive() else "Skeleton"
print(f"\n{winner} wins after {round_num} round(s).")

from dungeon.generators import generate_dungeon
from dungeon.item import EquippableSword, ConsumableHealthPotion
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
print("Map:", dungeon_map)


player = player.Player()

potion = ConsumableHealthPotion()
second_potion = ConsumableHealthPotion()
small_sword = EquippableSword()

player.grab_item(potion)
player.grab_item(small_sword)
print("Backpack:", player.get_backpack_content())
player.equip_item(small_sword)
print("Equipped stuff:", player.get_equipment())
player.grab_item(second_potion)
print("Backpack after equipping sword:", player.get_backpack_content())

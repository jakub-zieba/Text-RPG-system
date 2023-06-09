from .dungeon import generators
import player

#temporary solution for game sizing
max_dungeon_size_x: int = input("Provide max dungeon size on X axis")
max_dungeon_size_y: int = input("Provide max dungeon size on Y axis")


generators.generate_dungeon(max_dungeon_size_x, max_dungeon_size_y)

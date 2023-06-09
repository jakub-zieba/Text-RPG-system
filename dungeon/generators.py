import random

from dungeon.room import Room


def generate_room() -> Room:
    x = random.randint(0, 50)
    y = random.randint(0, 50)
    return Room(x, y)

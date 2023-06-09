import random

from dungeon.room import Room


def generate_room(x: int, y: int) -> Room:
    """Creates a single room instance"""
    return Room(x, y)


def _get_room_placement_permission(room_table: list[list], x: int, y: int) -> tuple[bool, bool]:
    """Return tuple indicating if (we can place a room, we HAVE TO place a room)"""
    up = left = cross_right = None
    if y != 0:
        up = room_table[y - 1][x]
    if x != 0:
        left = room_table[y][x - 1]
    if y != 0 and x < len(room_table[0]) - 1:
        cross_right = room_table[y - 1][x + 1]

    return (left is not None or up is not None), (up is not None and cross_right is None)


def generate_dungeon(max_size_x: int, max_size_y: int) -> list[Room]:
    """Builds dungeon map"""
    tmp_table: list[list[Room | None]] = [[None] * max_size_x for _ in range(max_size_y)]

    # Place first room on random first row
    rand_x = random.randint(0, max_size_x)
    first_room = generate_room(rand_x, 0)
    tmp_table[0][rand_x] = first_room

    for y in range(max_size_y):
        for x in range(max_size_x):
            can_be_placed, have_to_be_placed = _get_room_placement_permission(tmp_table, x, y)
            if have_to_be_placed:
                room = generate_room(x, y)
                tmp_table[y][x] = room
                continue
            if can_be_placed and random.choice([True, False]):
                room = generate_room(x, y)
                tmp_table[y][x] = room

    return [room for room_list in tmp_table for room in room_list if room is not None]

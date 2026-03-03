import random

from dungeon.room import Room, Direction
from dungeon.enemy import Skeleton
from dungeon.item import ConsumableHealthPotion


def _generate_room(x: int, y: int) -> Room:
    """Creates a single room instance"""
    enemies = []
    loot = []
    if random.choice([True, False]):
        # x is used as a pseudo difficulty indicator
        # if there are enemies loot automatically should also be there
        # TODO: Make a propper difficulty indicator based on dungeon depth and assign propper enemy or enemy group size
        for i in range(x):
            enemies.append([Skeleton()])
        loot.append(ConsumableHealthPotion())

    return Room(x, y, enemies, loot)


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


def _connect_rooms(dungeon_table: list, max_size_x: int, max_size_y: int) -> None:
    """Arrange doors between rooms based on their placement"""
    for y in range(max_size_y):
        for x in range(max_size_x):
            up = right = down = left = None
            room: Room | None = dungeon_table[y][x]
            if not room:
                continue

            if 0 <= x < max_size_x - 1:
                right = dungeon_table[y][x + 1]
            if 0 < x <= max_size_x - 1:
                left = dungeon_table[y][x - 1]
            if 0 <= y < max_size_y - 1:
                down = dungeon_table[y + 1][x]
            if 0 < y <= max_size_y - 1:
                up = dungeon_table[y - 1][x]

            if right:
                room.set_neighbour_room(Direction.EAST, right)
            if left:
                room.set_neighbour_room(Direction.WEST, left)
            if up:
                room.set_neighbour_room(Direction.NORTH, up)
            if down:
                room.set_neighbour_room(Direction.SOUTH, down)


def generate_dungeon(max_size_x: int, max_size_y: int) -> list[Room]:
    """Builds dungeon map"""
    tmp_table: list[list[Room | None]] = [[None] * max_size_x for _ in range(max_size_y)]

    # Place first room on random first row
    rand_x = random.randint(0, max_size_x)
    first_room = _generate_room(rand_x, 0)
    tmp_table[rand_x][0] = first_room

    for y in range(max_size_y):
        for x in range(max_size_x):
            can_be_placed, have_to_be_placed = _get_room_placement_permission(tmp_table, x, y)
            if have_to_be_placed:
                room = _generate_room(x, y)
                tmp_table[y][x] = room
                continue
            if can_be_placed and random.choice([True, False]):
                room = _generate_room(x, y)
                tmp_table[y][x] = room

    _connect_rooms(tmp_table, max_size_x, max_size_y)
    return [room for room_list in tmp_table for room in room_list if room is not None]

def visualize_dungeon(rooms: list[Room]) -> str:
    """Returns an ASCII art representation of the dungeon layout.

    Symbols:
      [ ] - empty room      [e] - room with enemies
      [l] - room with loot  [*] - enemies and loot
      ---  horizontal door   |   vertical door
    """
    if not rooms:
        return "(empty dungeon)"

    max_x = max(r.position[0] for r in rooms) + 1
    max_y = max(r.position[1] for r in rooms) + 1
    grid = {r.position: r for r in rooms}

    def _symbol(room: Room) -> str:
        has_e = bool(room.room_enemies_inside)
        has_l = bool(room.room_treasures_inside)
        if has_e and has_l:
            return "[*]"
        if has_e:
            return "[e]"
        if has_l:
            return "[l]"
        return "[ ]"

    lines = []
    for y in range(max_y):
        room_row = ""
        connector_row = ""
        for x in range(max_x):
            room = grid.get((x, y))
            room_row += _symbol(room) if room else "   "

            if x < max_x - 1:
                east = grid.get((x + 1, y))
                room_row += "---" if room and east and Direction.EAST in room.door_information else "   "

            if y < max_y - 1:
                south = grid.get((x, y + 1))
                connector_row += " | " if room and south and Direction.SOUTH in room.door_information else "   "
                if x < max_x - 1:
                    connector_row += "   "

        lines.append(room_row)
        if y < max_y - 1:
            lines.append(connector_row)

    return "\n".join(lines)
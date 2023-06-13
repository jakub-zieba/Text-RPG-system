from enum import Enum, auto


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class Room:
    # all rooms will be of a square shape, limiting their entrances/exits to 4
    # and a maximum of 4 doors on each side
    # each door needs to contain georgraphical direction as key and id of the room they lead to as value

    # TODO: Dynamically set this value. Maybe during generation from file/db?
    room_description = '''
        A text description of a room, this is default.
    '''

    # These lists will contain instances of enemies and treasures
    # enemies will need to be defeated first in order to obtain treasures
    def __init__(self, x: int, y: int, room_enemies_inside: list = [], room_treasures_inside: list = []):
        self.position: tuple[int, int] = (x, y)
        self.door_information: dict[Direction, Room] = dict()
        self.room_enemies_inside = room_enemies_inside
        self.room_treasures_inside = room_treasures_inside

    def __repr__(self):
        return f"Room<{self.position}>"

    def set_neighbour_room(self, direction: Direction, room: "Room") -> None:
        self.door_information[direction] = room

    # @property
    # def room_treasures(self):
    #     return self.room_door_information
    #
    # @room_treasures.setter
    # def room_treasures(self, room_treasures_inside):
    #     self.room_treasures_inside = room_treasures_inside
    #
    # @property
    # def room_enemies(self):
    #     return self.room_enemies_inside
    #
    # @room_enemies.setter
    # def room_enemies(self, room_enemies_inside):
    #     self.room_enemies_inside = room_enemies_inside
    
from enum import Enum, auto


class Direction(Enum):
    north = auto()
    south = auto()
    east = auto()
    west = auto()


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
    def __init__(self, x: int, y: int):
        self.position: tuple[int, int] = (x, y)
        self.room_door_information: dict[Direction, Room] = dict()
        self.room_enemies_inside: list = []
        self.room_treasures_inside: list = []

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
    
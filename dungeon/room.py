class RoomId:
    _id = ""
    _x = 0
    _y = 0

    def __init__(self, id, x, y):
            self._id = id
            self._x = x
            self._y = y

class Room:
    # all rooms will be of a square shape, limiting their entrances/exits to 4
    # and a maximum of 4 doors on each side
    # each door needs to contain georgraphical direction as key and id of the room they lead to as value

    room_door_information = {
        "north" : "",
        "south" : "",
        "east" : "",
        "west" : ""
    }

    room_description = '''
        A text description of a room, this is default.
    '''

    # These lists will contain instances of enemies and treasures
    # enemies will need to be defeated first in order to obtain treasures
    room_enemies_inside = []
    room_treasures_inside = []

    def __init__(self, room_id, room_door_information):
        self.room_id = room_id
        self.room_door_information = room_door_information

    @property
    def roomTreasures(self):
        return self.room_door_information
    
    @roomTreasures.setter
    def roomDoors(self, room_treasures_inside):
        self.room_treasures_inside = room_treasures_inside
    
    @property
    def roomEnemies(self):
        return self.room_enemies_inside

    @roomEnemies.setter
    def roomEnemies(self, room_enemies_inside):
        self.room_enemies_inside = room_enemies_inside    
    
class RoomId:
    id = ""
    x = 0
    y = 0

    def __init__(self, id, x, y):
            self.id = id
            self.x = x
            self.y = y

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

    room_id = RoomId("",0,0)
    
    room_description = '''
        A text description of a room, this is default.
    '''

    # These lists will contain instances of enemies and treasures
    # enemies will need to be defeated first in order to obtain treasures
    room_enemies_inside = []
    room_treasures_inside = []

    def __init__(self, room_id, room_door_information, room_enemies_inside, room_treasures_inside):
        self.room_id = room_id
        self.room_door_information = room_door_information
        self.room_enemies_inside = room_enemies_inside
        self.room_treasures_inside = room_treasures_inside

    
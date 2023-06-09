from dungeon.room import Room


def generate_room(x: int, y:int) -> Room:
    """Creates a single room instance"""
    x = x
    y = y
    return Room(x, y)

def generate_dungeon(max_dungeon_size_x:int, max_dungeon_size_y:int):
    """Builds dungeon map"""
    #for i in range(max_dungeon_size):
        #generate_room(x, y)

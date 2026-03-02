# Dungeon design
Dungeons have rectangular maps where a path is constructed by connecting individual rooms.
In the alpha version each room must have doors connecting with all other rooms next to it. In the beta version this requirement should be optional but under the condition there is no orphaned room in a dungeon.

## Room
A room can:
  a) be empty
  b) contain one or more enemies
  c) contain an NPC
  d) contain a treasure chest

### Room interactions
If the room contains enemies the combat mode is entered where the player must defeat all enemies located in the room. The combat will be described in combat.md

If the room contains a treasure chest the player may choose to interact with it or leave as-is.

If the room contains an NPC the dialogue is opened which can be exited always excempt from when a decision is being made. Decisions will impact dungeon storyline.

Empty room can be left immediately using any doors.

## Navigation

Player is unable to view his current location in the dungeon.
Player can go through any door in the room he is located in provided he completes room interactions.




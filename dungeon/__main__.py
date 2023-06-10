from dungeon.dialogues import Dialogue
from dungeon.generators import generate_dungeon

if __name__ == "__main__":
    # generate_dungeon(10, 10)
    Dialogue.load_dialogue_file("intro")
    for i in Dialogue():
        print(i)
    for i in Dialogue():
        print(i)

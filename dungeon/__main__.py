from dungeon.decision_tree import generate_dialogue_tree

# from dungeon.dialogues import Dialogue
# from dungeon.generators import generate_dungeon

if __name__ == "__main__":
    # generate_dungeon(10, 10)
    # Dialogue.load_dialogue_file("intro")
    # for i in Dialogue():
    #     print(i)
    # for i in Dialogue():
    #     print(i)

    tree = generate_dialogue_tree("test_d")

    tree.exec()

    while True:
        if not tree.current_position.children:
            print("Dialogue came to an end")
            break
        for idx, child in enumerate(tree.current_position.children):
            print(f"{idx}: {child.short}")

        option = input("Which option to choose: ")
        if not option.isdigit():
            print("Bzidka opcja")
            continue

        tree.next_node(int(option))
        tree.exec()

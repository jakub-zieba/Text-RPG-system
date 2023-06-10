from dungeon.decision_tree import Node, DecisionTree
# from dungeon.dialogues import Dialogue
# from dungeon.generators import generate_dungeon

if __name__ == "__main__":
    # generate_dungeon(10, 10)
    # Dialogue.load_dialogue_file("intro")
    # for i in Dialogue():
    #     print(i)
    # for i in Dialogue():
    #     print(i)
    node = Node("Root", "main") \
        .set_next(Node("#1 from root", "left_branch")) \
        .set_next(Node("#2 from root", "right_branch")
                  .set_next(Node("#1 from child", "left_right_branch"))
                  .set_next(Node("#2 from child", "right_right_branch")))

    tree = DecisionTree(node)

    tree.exec()

    while True:
        if not tree.current_position.children:
            print("Dialogue came to an end")
            break
        for idx in range(len(tree.current_position.children)):
            print(f"{idx}: ...")

        option = input("Which option to choose: ")
        if not option.isdigit():
            print("Bzidka opcja")
            continue

        tree.next_node(int(option))
        tree.exec()

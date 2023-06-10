from dungeon.dialogues import Dialogue


class Node:

    def __init__(self, _id: str, dialogue_name: str):
        self._id = _id
        self.dialogue_name = dialogue_name
        self.parent: Node | None = None
        self.children: list[Node | None] = []

    def set_next(self, node: "Node") -> "Node":
        self.children.append(node)
        node.parent = self
        return self

    def exec(self):
        Dialogue.load_dialogue_file(self.dialogue_name)
        for line in Dialogue():
            print(line)

    def __repr__(self):
        return f"Node<{self._id}>"


class DecisionTree:

    def __init__(self, node: Node, bidirectional: bool = False):
        self.entry_point = node
        self.current_position = node
        self.bidirectional = bidirectional

    def next_node(self, node_number: int):
        try:
            self.current_position = self.current_position.children[node_number]
        except IndexError:
            print("This option is not available")

    def exec(self):
        self.current_position.exec()



# node = Node("Root", "main")\
#     .set_next(Node("#1 from root", "left_branch"))\
#     .set_next(Node("#2 from root", "right_branch")
#               .set_next(Node("#1 from child", "left_right_branch"))
#               .set_next(Node("#2 from child", "right_right_branch")))
#
# tree = DecisionTree(node)

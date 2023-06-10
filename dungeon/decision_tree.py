from dataclasses import dataclass
from typing import List

import yaml

from pathlib import Path

from tonalite import from_dict


@dataclass
class Node:
    short: str | None
    long: str
    # Can not use generic here
    # see: https://docs.python.org/3/library/typing.html#typing.ForwardRef
    children: List["Node"]

    def exec(self):
        print(self.long)


class DecisionTree:

    def __init__(self, node: Node):
        self.entry_point = node
        self.current_position = node

    def next_node(self, node_number: int):
        try:
            self.current_position = self.current_position.children[node_number]
        except IndexError:
            print("This option is not available")

    def exec(self):
        self.current_position.exec()


def generate_dialogue_tree(dialogue_name: str) -> DecisionTree | None:
    dialogue_path = Path(__file__).parent / f"dialogues/{dialogue_name}.yaml"
    if not dialogue_path.exists():
        print(f"Provided dialogue: {dialogue_name} does not exists!")
        return None

    with open(dialogue_path) as file:
        result = yaml.safe_load(file)

    parsed_node = from_dict(data_class=Node, data=result)
    return DecisionTree(parsed_node)

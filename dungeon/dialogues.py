from pathlib import Path
from typing import TextIO

from dungeon.const import DUMMY_DIALOGUE_PATH


class Dialogue:
    """
    Covers multiple lines of dialogue for player

    In order to show dialogue lines we need:
        1. explicitly load file
        2. we can iterate over dialogue (only once)

    To be able to read same file again, it needs to be reloaded using `load_dialogue_file`
    """

    dialogue_path: Path = DUMMY_DIALOGUE_PATH
    dialogue_file: TextIO | None = None

    @classmethod
    def load_dialogue_file(cls, name: str) -> None:
        cls.dialogue_path = Path(__file__).parent / f"dialogues/{name}.txt"
        if not cls.dialogue_path.exists():
            print("Provided dialogue does not exists!")

    @classmethod
    def _setup_dummy_file(cls) -> None:
        """Used for making sure we will loop over one dialogue only once"""
        cls.dialogue_path = DUMMY_DIALOGUE_PATH

    def __iter__(self):
        if self.dialogue_path != DUMMY_DIALOGUE_PATH:
            self.dialogue_file = open(self.dialogue_path, 'r')
        return self

    def __next__(self):
        if self.dialogue_file is None:
            raise StopIteration

        if not (line := self.dialogue_file.readline().rstrip('\n')):
            self.dialogue_file.close()
            self.dialogue_file = None
            self._setup_dummy_file()
            raise StopIteration

        return line

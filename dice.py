import random

class Dice:

    def __init__(self, faces: tuple) -> None:

        self.faces = faces

    def roll(self) -> str:

        return random.choice(self.faces)

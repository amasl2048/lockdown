from creature import Creature

class Intruder(Creature):

    def __init__(self, name, character, number: int):

        self.description = {
            "name": name,
            "character": character,
            "number": 0
            }

        self.state = {
            "combat": False,
            "room_id": 0,
            "hits": 0,
            "alive": True
            }

    def hit(self, hits: int):
        self.state["hits"] += hits

    def get_hits(self) -> int:
        return self.state["hits"]

    def die(self):
        self.state["alive"] = False
        self.state["room_id"] = None

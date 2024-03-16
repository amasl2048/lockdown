import pprint
pp = pprint.PrettyPrinter(indent=4)

from config import PLAYERS

class Person:

    def __init__(self, name, color, character, room_id: str, knowledge: int):

        self.description = {
            "name": name,
            "color": color,
            "character": character
            }

        self.state = {
            "pass": False,
            "combat": False,
            "room_id": room_id,
            "knowledge": knowledge,
            "slime": False,
            "infected": False,
            "light_wound": 0,
            "serious_wounds": 0
            }

        self.hands = {
            "left_hand": list(),
            "right_hand": list(),
        }

        self.deck = {
            "action_deck": set(),
            "discard_deck": set(),
            "hand": set()
            }

        self.inventory = []

    def set_person(self, name: str, color: str, character: str) -> bool:

        if not character in PLAYERS:
            return False

        self.description["name"] = name
        self.description["color"] = color
        self.description["character"] = character

        return True

    def get_stat(self) -> str:

        stat = []
        if self.state["combat"]:
            stat.append("COMBAT")
        if self.state["slime"]:
            stat.append("SLIME")
        if self.state["infected"]:
            stat.append("INFECTED")

        return " | ".join(stat)

    def get_location(self) -> str:

        return self.state["room_id"]

    def set_location(self, room: str) -> str:

        self.state["room_id"] = room

    def get_name(self) -> str:

        return self.description["name"]

    def get_character(self) -> str:

        return self.description["character"]

    def light_wound(self):

        if self.state["light_wound"] < 2:
            self.state["light_wound"] += 1

        else:
            self.state["serious_wounds"] += 1
            self.state["light_wound"] = 0

    def slime(self):

        self.state["slime"] = True

    def clear_slime(self):

        self.state["slime"] = False

    def infected(self):

        self.state["infected"] = True

    def clear_infection(self):

        self.state["infected"] = False

    def combat(self):

        self.state["combat"] = True

    def clear_combat(self):

        self.state["combat"] = False

    def is_combat(self) -> bool:

        if self.state["combat"]:
            return True

        return False


    def show(self):
        pp.pprint(self.description)
        pp.pprint(self.state)

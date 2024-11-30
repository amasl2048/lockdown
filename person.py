import config as CFG
from creature import Creature
from deck import Deck

class Person(Creature):

    def __init__(self, name, color, character, room_id: str):

        self.description = {
            "name": name,
            "color": color,
            "character": character,
            "number": 0
            }

        self.state = {
            "pass": False,
            "combat": False,
            "room_id": room_id,
            "signal": False,
            "slime": False,
            "infected": False,
            "light_wounds": 0,
            "serious_wounds": 0,
            "dressed_wounds": 0,
            "alive": True
            }

        self.hands = {
            "left_hand": None,
            "right_hand": None,
        }

        self.deck = {
            "action": Deck(),
            "discard": Deck(),
            "hand": Deck()
            }

        self.inventory = []
        self.mission_code = None

    def set_person(self, name: str, color: str, character: str) -> bool:

        if not character in CFG.CHARACTERS:
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

    def check_hand(self) -> int:
        return self.deck["hand"].number()

    def get_color(self) -> str:
        return self.description["color"]
    
    def get_light_wounds(self) -> int:
        return self.state["light_wounds"]
    
    def get_serious_wounds(self) -> int:
        return self.state["serious_wounds"]


    def light_wound(self):

        if self.state["serious_wounds"] == 3:
            self.state["alive"] = False

        if self.state["light_wounds"] < 2:
            self.state["light_wounds"] += 1
        else:
            self.state["serious_wounds"] += 1
            self.state["light_wounds"] = 0

        if self.state["serious_wounds"] > 3:
            self.state["alive"] = False


    def serious_wound(self):
        self.state["serious_wounds"] += 1
        if self.state["serious_wounds"] > 3:
            self.state["alive"] = False


    def dress_wound(self) -> bool:
        if self.state["dressed_wounds"] >= self.state["serious_wounds"]:
            return False
        self.state["dressed_wounds"] += 1
        return True

    def check_wound_effect(self) -> bool:
        if self.state["dressed_wounds"] < self.state["serious_wounds"]:
            return True
        return False  # not affected
    
    def heal_light_wound(self):
        if self.state["light_wounds"] == 1 \
            or self.state["light_wounds"] == 2:
            self.state["light_wounds"] -= 1

    def heal_dressed_wound(self):
        if self.state["dressed_wounds"] > 0:
            self.state["serious_wounds"] -= 1
            self.state["dressed_wounds"] -= 1


    def slime(self):
        self.state["slime"] = True

    def clear_slime(self):
        self.state["slime"] = False

    def check_infected(self):
        return self.state["infected"]

    def infected(self):
        self.state["infected"] = True

    def clear_infection(self):
        self.state["infected"] = False

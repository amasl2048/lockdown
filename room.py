import pprint
pp = pprint.PrettyPrinter(indent=4)

import config as CFG
from person import Person
from path import Path

class Room:

    def __init__(self, 
                 id: int, 
                 name: str, 
                 section: int,
                 effect: str,
                 items: int):

        self.description = {
            "id": id,
            "name": name,
            "section": section
        }

        self.state = {
            "open": False,
            "effect": effect,
            "broken": False,
            "fire": False,
            "items": items
        }

        self.players = []
        self.intruders = []
        self.objects = []

        self.path = {}             # "connected_room: str": "path_number: int"
        self.corridors = {}        # "corridor: str": "connected_room: int"

    def is_fire(self) -> bool:

        if not self.state["open"]:
            return False

        if self.state["fire"]:
            return True

        return

    def is_broken(self) -> bool:

        if not self.state["open"]:
            return False

        if self.state["broken"]:
            return True

        return False

    def effect(self) -> str:

        if not self.state["open"]:
            return ""

        effect = []
        if self.state["fire"]:
            effect.append("FIRE")
        if self.state["broken"]:
            effect.append("BROKEN")

        return " | ".join(effect)

    def items(self) -> str:

        if not self.state["open"]:
            return "Unknown"

        return str(self.state["items"])


    def get_path_from_corridor(self, corridor: str) -> str:

        to_room = str(self.corridors[corridor])
        path = str(self.path[to_room])

        return path

    def get_path(self) -> set:

        pt = []
        for rm in self.path.keys():
            pt.append(str(self.path[rm]))

        return set(pt)

    def get_connected_rooms(self) -> list:

        rooms = list(self.path.keys())
        if "0" in rooms:
            rooms.remove("0")

        return rooms

    def get_remote_room(self, corridor: str) -> str:

        return str(self.corridors[corridor])

    def apply_effects(self) -> str:

        effect = self.state["effect"]
        if effect == "FIRE":
            self.state["fire"] = True
        elif effect == "MALFUNCTION":
            self.state["broken"] = True

        return effect

    def open_room(self):

        self.state["open"] = True

    def get_players_names(self) -> list:

        names = []

        for p in self.players:
            names.append(p.get_name())

        return names

    def check_players(self) -> bool:

        for p in self.players:
            character = p.get_character()
            if character in CFG.PLAYERS:
                return True

        return False

    def get_intruders_names(self) -> list:

        names = []

        for p in self.intruders:
            names.append(p.get_name())

        return names

    def check_intruders(self) -> bool:

        for p in self.intruders:
            character = p.get_character()
            if character in CFG.INTRUDERS:
                return True

        return False

    def check_room(self) -> (bool, str):

        explored = self.state["open"]
        if explored:
            name = self.description["name"]
        else:
            name = "Unknown"

        return explored, name

    def enter_room(self, person: Person):

        character = person.get_character()

        if character in CFG.PLAYERS:
            self.players.append(person)
        elif character in CFG.INTRUDERS:
            self.intruders.append(person)

    def exit_room(self, person: Person):

        character = person.get_character()

        if character in CFG.PLAYERS:
            self.players.remove(person)
        elif character in CFG.INTRUDERS:
            self.intruders.remove(person)           #FIXME


    def show(self):
        pp.pprint(self.description)
        pp.pprint(self.state)
        print("Connected rooms:")
        pp.pprint(self.path)
        print("Corridors:")
        pp.pprint(self.corridors)

        print("Players:")
        print(self.get_players_names())

        print("Intruders:")
        print(self.get_intruders_names())

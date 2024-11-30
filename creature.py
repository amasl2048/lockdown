import pprint
pp = pprint.PrettyPrinter(indent=4)

class Creature:

    def __init__(self):

        self.description = {
            "name": "",
            "character": "",
            "number": 0
            }

        self.state = {
            "combat": False,
            "room_id": "",
            "alive": True
            }

    def get_name(self) -> str:
        return self.description["name"]
    
    def get_location(self) -> str:
        return self.state["room_id"]

    def set_location(self, room: str):
        self.state["room_id"] = room

    def get_character(self) -> str:
        return self.description["character"]
    
    def check_alive(self) -> bool:
        return self.state["alive"]
    
    def die(self):
        self.state["alive"] = False

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

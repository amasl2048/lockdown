import pprint
pp = pprint.PrettyPrinter(indent=4)

DOOR = ("OPEN", "CLOSED", "BROKEN")

class Path:

    def __init__(self, id: int, room1: str, room2: str, corridors: list) -> None:
        
        self.description = {
            "id": id,
            "first": room1,
            "second": room2,
            "corridors": corridors
        }

        self.state = {
            "door": "OPEN",
            "noise": False
        }

    def get_corridors(self) -> list:

        return self.description["corridors"]

    def get_rooms(self) -> (str, str):

        return self.description["first"], self.description["second"]

    # noise
    def make_noise(self):

        self.state["noise"] = True

    def clear_noise(self):

        self.state["noise"] = False

    def is_noise(self):

        return self.state["noise"]


    # door
    def show_state(self) -> str:

        state = []

        if not self.state["door"] == "OPEN":
            state.append(self.state["door"])

        if self.state["noise"]:
            state.append("NOISE")

        return " | ".join(state)

    def is_closed(self) -> bool:

        if self.state["door"] == "CLOSED":
            return True

        return False

    def close_door(self):

        if self.state["door"] == "OPEN":
            self.state["door"] = "CLOSED"

    def open_door(self):

        if self.state["door"] == "CLOSED":
            self.state["door"] = "OPEN"

    def break_door(self):

        self.state["door"] = "BROKEN"


    def show(self):
        pp.pprint(self.description)
        pp.pprint(self.state)

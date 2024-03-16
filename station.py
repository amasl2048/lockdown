import pprint
pp = pprint.PrettyPrinter(indent=4)

from config import TOTAL_ROOMS
from room import Room
from person import Person
from path import Path


class Station:

    def __init__(self) -> None:

        self.state = {
            "fire": 0,
            "malfunction": 0
        }

        self.power = {
            "1": True,
            "2": True,
            "3": False
        }

        self.rooms = {}  # Room objects dict
        self.path = {}   # Path objects dict

    def burnout(self) -> str:

        fire = 0
        for rm in range(1, TOTAL_ROOMS+1):

            if self.rooms[str(rm)].is_fire():
                fire += 1

        return "%s %%" % str(int(fire/TOTAL_ROOMS))

    def destruction(self) -> str:

        broken = 0
        for rm in range(1, TOTAL_ROOMS+1):

            if self.rooms[str(rm)].is_broken():
                broken += 1

        return "%s %%" % str(int(broken/TOTAL_ROOMS))


    def remove_all_noise(self, room: str):

        paths = self.rooms[room].get_path()

        for p in paths:
            self.path[p].clear_noise()

        return

    def make_all_noise(self, room: str) -> bool:

        paths = self.rooms[room].get_path()
        encounter = False
        for p in paths:
            if self.path[p].is_noise():
                encounter = True
                return encounter

            self.path[p].make_noise()

        return encounter

    def move(self, person: Person, from_room: str, to_room: str):

        self.exit_room(person, from_room)
        self.enter_room(person, to_room)

        #self.rooms[from_room].exit_room(person)
        #self.rooms[to_room].enter_room(person)

    def get_path(self, room1: str, room2: str) -> (bool, str):

        try:
            path = str(self.rooms[room1].path[room2])
        except Exception as e:
            return False, e

        return True, path

    def check_connected(self, current_room: str, room: str) -> bool:

        if room in self.rooms[current_room].get_connected_rooms():
            return True

        return False

    def enter_room(self, person: Person, room: str):

        self.rooms[room].enter_room(person)
        person.set_location(room)

    def exit_room(self, person: Person, room: str):

        self.rooms[room].exit_room(person)
        person.set_location("")

        

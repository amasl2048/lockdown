import random
import pprint
pp = pprint.PrettyPrinter(indent=4)

from config import TOTAL_ROOMS
#from room import Room
from creature import Creature
from person import Person
from intruder import Intruder
#from path import Path


class Station:

    def __init__(self) -> None:

        self.state = {
            "destination": "",
            "fire": 0,
            "malfunction": 0,
            "intruders_counter": 0
        }

        self.engine = {
            "1": random.choice((True, False)),
            "2": random.choice((True, False)),
            "3": random.choice((True, False))
        }

        self.rooms = {}  # Room objects dict
        self.path = {}   # Path objects dict


    def check_engine(self, num: int) -> str:
        if self.engine[str(num)]:
            return "Engine %i working" % num
        else:
            return "Engine %i damaged" % num


    def check_destination(self):
        return self.state["destination"]
    
    def set_destination(self, dest: str):
        self.state["destination"] = dest


    def burnout(self) -> str:

        fire = 0
        for rm in range(1, TOTAL_ROOMS+1):

            if self.rooms[str(rm)].is_fire():
                fire += 1

        return "%i/%i (%s%%)" % (fire, TOTAL_ROOMS,
                                str(int(fire/TOTAL_ROOMS)))


    def destruction(self) -> str:

        broken = 0
        for rm in range(1, TOTAL_ROOMS+1):

            if self.rooms[str(rm)].is_broken():
                broken += 1

        return "%i/%i (%s%%)" % (broken, TOTAL_ROOMS,
                                 str(int(broken/TOTAL_ROOMS)))


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


    def move(self, creature: Creature, from_room: str, to_room: str):
        self.exit_room(creature, from_room)
        self.enter_room(creature, to_room)


    def get_path(self, room1: str, room2: str):  # -> (Bool, str)

        try:
            path = str(self.rooms[room1].path[room2])
        except Exception as e:
            return False, e

        return True, path

    def check_connected(self, current_room: str, room: str) -> bool:

        if room in self.rooms[current_room].get_connected_rooms():
            return True

        return False

    def enter_room(self, creature: Creature, room_id: str):
        self.rooms[room_id].enter_room(creature)
        creature.set_location(room_id)

    def exit_room(self, creature: Creature, room_id: str):
        self.rooms[room_id].exit_room(creature)
        creature.set_location("0")  #FIXME: 0

    def remove_intruder(self, intruder:Intruder):
        room_id = intruder.get_location()
        self.rooms[room_id].exit_room(intruder)
        del intruder

    def show_rooms(self):
        for room_id in self.rooms.keys():

            items = self.rooms[room_id].heavy_objects
            if items:
                print(items)

            for alien in self.rooms[room_id].intruders:
                print(room_id, alien.get_name())

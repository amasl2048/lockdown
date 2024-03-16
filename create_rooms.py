import random
import pprint
pp = pprint.PrettyPrinter(indent=4)

import config as CFG
from station import Station
from room import Room


def bool_prob(probability=0.5):
    return random.random() < probability


def add_rooms(station: Station) -> None:

    room_list1 = list(CFG.ROOMS_I)
    room_list2 = list(CFG.ROOMS_II)

    # S1
    section = 1
    for r in [1, 2]:

        selected_room = random.choice(room_list2)
        room_list2.remove(selected_room)

        station.rooms[str(r)] = Room(id=r,
                                name=selected_room,
                                section=section,
                                effect = random.choice(CFG.EFFECTS),
                                items=random.randint(1,6))

    # S2
    section = 2
    for r in [3, 4]:

        selected_room = random.choice(room_list2)
        room_list2.remove(selected_room)

        station.rooms[str(r)] = Room(id=r,
                                name=selected_room,
                                section=section,
                                effect = random.choice(CFG.EFFECTS),
                                items=random.randint(1,6))

    for r in range(5,10):

        selected_room = random.choice(room_list1)
        room_list1.remove(selected_room)

        station.rooms[str(r)] = Room(id=r,
                                name=selected_room,
                                section=section,
                                effect = random.choice(CFG.EFFECTS),
                                items=random.randint(1,6))

    # S3
    section = 3
    for r in [10, 11]:

        selected_room = random.choice(room_list2)
        room_list2.remove(selected_room)

        station.rooms[str(r)] = Room(id=r,
                                name=selected_room,
                                section=section,
                                effect = random.choice(CFG.EFFECTS),
                                items=random.randint(1,6))

    for r in range(12, 17):

        selected_room = random.choice(room_list1)
        room_list1.remove(selected_room)

        station.rooms[str(r)] = Room(id=r,
                                name=selected_room,
                                section=section,
                                effect = random.choice(CFG.EFFECTS),
                                items=random.randint(1,6))

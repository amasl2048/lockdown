import pprint
pp = pprint.PrettyPrinter(indent=4)

from station import Station
from room import Room

def open_sp_rooms(station: Station):

    for rm in range(17, 24):

        station.rooms[str(rm)].open_room()

def add_sp_rooms(station: Station) -> None:

    station.rooms[str(0)] = Room(id=0,
                                name="Technical Corridor",
                                section=0,
                                effect = "",
                                items=0)

    # S1
    station.rooms[str(17)] = Room(id=17,
                                name="Repository",
                                section=1,
                                effect = "",
                                items=0)

    station.rooms[str(21)] = Room(id=21,
                                name="Elevator Room S-01",
                                section=1,
                                effect = "",
                                items=0)

    # S2
    station.rooms[str(18)] = Room(id=18,
                                name="Alert Room",
                                section=2,
                                effect = "",
                                items=0)

    station.rooms[str(22)] =  Room(id=22,
                                name="Elevator Room S-02",
                                section=2,
                                effect = "",
                                items=0)

    # S3
    station.rooms[str(19)] = Room(id=19,
                                name="Backup Power Supply",
                                section=3,
                                effect = "",
                                items=0)

    station.rooms[str(20)] = Room(id=20,
                                name="Isolation Room",
                                section=3,
                                effect = "",
                                items=0)

    station.rooms[str(23)] = Room(id=23,
                                name="Elevator Room S-03",
                                section=3,
                                effect = "",
                                items=0)
 
    open_sp_rooms(station)

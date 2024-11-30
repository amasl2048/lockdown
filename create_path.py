import pprint
pp = pprint.PrettyPrinter(indent=4)

from station import Station
from path import Path

def add_path(station: Station) -> None:

    # Technical corridor '0'

    station.path["0"] = Path(id=0, room1="0", room2="0", corridors=["0"])

    station.rooms["0"].path = {"0": 0,
                               "1": 0,  # "to_room": path
                               "2": 0}
    station.rooms["0"].corridors = {"1": 0,  # "corridor": to_room
                                    "2": 0,
                                    "3": 0,
                                    "4": 0}
    
    # S1

    ## Room1
    station.rooms["1"].path = {"0": 0, "17": 3, "21": 1}
    station.rooms["1"].corridors = {"1": 0,
                                    "2": 21,
                                    "3": 17,
                                    "4": 17}

    ## Room2
    station.rooms["2"].path = {"0": 0, "17": 4, "21": 2}
    station.rooms["2"].corridors = {"1": 21,
                                    "2": 17,
                                    "3": 0,
                                    "4": 0}
    
    station.path["1"] = Path(id=1, room1="1", room2="21", corridors=["2"])
    station.path["2"] = Path(id=2, room1="2", room2="21", corridors=["1"])

    ## Room21
    #station.rooms["21"].path = {"1": 1, "2": 2}
    station.rooms["21"].path = {"0": 0, "1": 1, "2": 2}  #FIXME
    station.rooms["21"].corridors = {"1": 2,
                                     "2": 1,
                                     "3": 0,
                                     "4": 0}

    ## Room17
    #station.rooms["17"].path = {"1": 3, "2": 4}
    station.rooms["17"].path = {"0": 0, "1": 3, "2": 4} #FIXME
    station.rooms["17"].corridors = {"1": 0,
                                     "2": 2,
                                     "3": 1,
                                     "4": 1}

    station.path["3"] = Path(id=3, room1="1", room2="17", corridors=["3", "4"])
    station.path["4"] = Path(id=4, room1="2", room2="17", corridors=["2"])

import random
from station import Station
from intruder import Intruder

def retreat(station: Station, intruder: Intruder, room_id: str) -> str:

    name = intruder.get_name()
    direction = str(random.randint(1,4))  #  ; print("Corridor: ", direction)
    #print(station.rooms[room_id].corridors)
    to_room_id = str(station.rooms[room_id].corridors[direction])

    msg = "\n%s try to retreat over %s corridor to %s room" % \
            (name, direction, to_room_id)

    if to_room_id == "0":
        rn = "Technical Corridor"
        station.rooms[room_id].exit_room(intruder)
        del intruder
        msg += "\n%s fled to %s" % (name, rn)
        return msg

    else:
        expl, rn = station.rooms[to_room_id].check_room()
        pn = station.rooms[room_id].get_path_from_corridor(direction)

        if station.path[pn].is_closed():
            station.path[pn].break_door()
            msg += "\nDoor to %s room is broken" % direction

        station.move(intruder, room_id, to_room_id)
        msg += "\n%s retreat to room %s (%s)" % (name, to_room_id, rn)

    return msg




    return msg

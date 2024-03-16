from start_game import game1
from person import Person
from station import Station

def resolve_encounter(station: Station, room: str):

    # remove all noise
    station.remove_all_noise(room)
    msg = "Remove all noise.\n"

    # draw intruder token
    token = game1.get_pool().get()

    # Blank token
    if token == "-":
        msg += "Nothing happens.\n"
        station.make_all_noise(room)
        msg += "Noise in all corridors.\n"
        if game1.get_pool().count() == 0:
            game1.get_pool().add("ADULT")
        else:
            game1.get_pool().add("-")
        return msg

    intruder = Person(name=token,
                 color="Grey",
                 character=token,
                 room_id=room,
                 knowledge=0
                 )

    # intruder enter the room

    station.enter_room(intruder, room)
    msg += "%s enter room %s.\n" % (token, room)

    # surprise attack
    #TODO

    return msg

from start_game import game1
from person import Person
from intruder import Intruder
from station import Station

import event_surprise_attack

def resolve_encounter(station: Station, room: str, person: Person):

    msg = "\n\nENCOUNTER!"
    # remove all noise
    station.remove_all_noise(room)
    msg += "\nRemove all noise."

    # draw intruder token
    token = game1.get_pool().get()

    # Blank token
    if token == "-":

        msg += "\nBlank token. Nothing happens."
        station.make_all_noise(room)
        msg += "\nNoise in all corridors."

        if game1.get_pool().count() == 0:
            game1.get_pool().add("ADULT")
        else:
            game1.get_pool().add("-")
        return msg

    # create Intruder object
    in_counter = station.state["intruders_counter"]
    name=token + "-" + str(in_counter + 1)
    intruder = Intruder(
                name=name,
                character=token,
                number=in_counter+1
                )

    # intruder enter the room
    station.enter_room(intruder, room)
    station.state["intruders_counter"] += 1
    msg += "\n%s enter room %s." % (name, room)

    # surprise attack
    msg += event_surprise_attack.surprise_attack(station, person, intruder)

    #Check alive
    if not person.check_alive():
        station.exit_room(person, room)
        # put corpse into the room
        station.rooms[room].corpse(person.get_character())
        msg += "\n\n %s IS DEAD!!!" % person.get_character()
        return msg

    return msg

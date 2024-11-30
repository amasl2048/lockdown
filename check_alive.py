from station import Station
from creature import Creature

def check_creature_alive(station: Station, creature: Creature, room: str):

    if not creature.check_alive():
        character = creature.get_character()
        station.exit_room(creature, room)
        # Put corpse into the room
        station.rooms[room].corpse(character)
        msg = "\n %s is dead!!!" % character
        return False, msg

    return True, ""

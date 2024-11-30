import config as CFG
from person import Person
from station import Station
from start_game import game1

from event_encounter import resolve_encounter
from event_surprise_attack import surprise_attack
from check_combat import in_combat
from check_alive import check_creature_alive

def apply_danger(station, room, player):

    encounter = station.make_all_noise(room)
    msg = "\nMore noise in all paths"
    if encounter:
        msg += resolve_encounter(station, room, player)

    return msg


def enter_explored_room(station, room) -> bool:

    msg = ""

    not_empty = station.rooms[room].check_players()
    _, room_name = station.rooms[room].check_room()

    if not_empty: 

        players = station.rooms[room].get_players_names()
        noise = False
        msg += "\nPlayers in the room: %s" % players

    else:  # no players in the room

        noise = True
        msg += "\nNo other players in the '%s'" % room_name

    return noise, msg


def discover_room(station: Station, current_room, room, player: Person) -> bool:

    player_char = player.get_character()

    noise = True
    effect = station.rooms[room].apply_effects()  # apply FIRE and MALFUNCTION
    msg = "\nApply effects: '%s'" % effect

    if effect == "SLIME":
        player.slime()
        msg += "\n%s get %s" % (player_char, effect)

    elif effect == "SILENCE":
        if not player.state["slime"]:
            noise = False
        else:
            msg += "\nApply 'DANGER' because of SLIME"
            msg += apply_danger(station, room, player)

    elif effect == "DOOR":
        path = str(station.rooms[room].path[current_room])
        station.path[path].close_door()
        msg += "\nDoor between %s and %s is closed." % (current_room, room)

    elif effect == "DANGER":

        #FIXME: if no intruders
        msg += apply_danger(station, room, player)


    station.rooms[room].open_room()
    _, room_name = station.rooms[room].check_room()
    msg += "\n'%s' is explored" % room_name

    return noise, msg


def noise_dice(station: Station, player: Person, room: str) -> str:

    roll = game1.get_noise_roll().roll()
    msg = "\nNoise roll: %s" % roll

    if roll in ["1", "2", "3", "4"]:

        to_room = station.rooms[room].corridors[roll]
        noise_path = station.rooms[room].get_path_from_corridor(roll)

        if station.path[noise_path].is_noise():
            msg += "\nToo noisy in path %s towards to %s room" % (noise_path, to_room)
            msg += resolve_encounter(station, room, player)

        else:
            station.path[noise_path].make_noise()
            msg += "\nWas a noise in path %s towards to %s room" % (noise_path, to_room)

    elif roll == "SILENCE":

        if player.state["slime"]:
            msg += "\nApply 'DANGER' because of SLIME"
            msg += apply_danger(station, room, player)
        else:
            return msg

    elif roll == "DANGER":
        #FIXME: if no intruders in near rooms
        msg += apply_danger(station, room, player)

    return msg


def move(station: Station, player: Person, room: str):

    msg = ""

    if room == "0":
        msg += "\nYou couldn't enter to the Technical corridor."
        return False, msg

    current_room = player.get_location()
    player_char = player.get_character()

    if room == current_room:
        msg += "\n%s are already in the room." % player_char
        return False, msg

    # if room connected
    connected = station.check_connected(current_room, room)
    msg += "\n%s try to move from %s to %s ..." % (player_char, current_room, room)

    if not connected:
        msg += "\nRoom %s is not connected to %s." % (current_room, room)
        return False, msg

    # Check the door between the rooms is open
    res, path = station.get_path(current_room, room)
    if not res:
        msg += "\nError! No path from %s to %s." % (current_room, room)
        return False, msg

    if station.path[path].is_closed():
        msg += "\nDoor from %s to %s is closed." % (current_room, room)
        return False, msg

    # Escape
    if station.rooms[current_room].check_intruders():

        for alien in station.rooms[current_room].intruders:
            msg += "\nTry to escape from %s" % alien.get_name()
            msg += surprise_attack(station, player, alien)

            #Check alive
            res, out = check_creature_alive(station, player, current_room)
            msg += out
            if not res:
                return False, msg

    # Explore
    explored, room_name = station.rooms[room].check_room()
    msg += "\n%s entering to the room %s: '%s'" % (player_char, room, room_name)

    if explored:

        noise, msg1 = enter_explored_room(station, room)

    else:  # if room is unexplored

        noise, msg1 = discover_room(station, current_room, room, player)

    msg += msg1
    
    # Move to room
    station.move(player, current_room, room)

    if noise:

        msg += noise_dice(station, player, room)

    msg += in_combat(station, room)

    if CFG.DEBUG:
        print(msg)  

    return True, msg

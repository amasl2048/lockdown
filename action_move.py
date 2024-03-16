from person import Person
from station import Station
from start_game import game1

from event_encounter import resolve_encounter
from check_combat import in_combat

def apply_danger(station, room):

    encounter = station.make_all_noise(room)
    msg = "More noise in all paths\n"
    if encounter:
        msg += "ENCOUNTER!\n"
        msg += resolve_encounter(station, room)

    return msg


def enter_explored_room(station, room) -> bool:

    msg = ""

    empty = station.rooms[room].check_players()
    _, room_name = station.rooms[room].check_room()

    if empty: # if no players in the room

        noise = True
        msg += "No other players in the '%s'\n" % room_name

    else:

        players = station.rooms[room].get_players_names()
        noise = False
        msg += "Players in the room: %s\n" % players

    return noise, msg


def discover_room(station, current_room, room, player) -> bool:

    player_name = player.get_name()

    noise = True
    effect = station.rooms[room].apply_effects()  # apply FIRE and MALFUNCTION
    msg = "Apply effects: '%s'\n" % effect

    if effect == "SLIME":
        player.slime()
        msg += "%s get %s\n" % (player_name, effect)

    elif effect == "SILENCE":
        if not player.state["slime"]:
            noise = False
        else:
            msg += "Apply 'DANGER' because of SLIME\n"
            msg += apply_danger(station, room)

    elif effect == "DOOR":
        path = str(station.rooms[room].path[current_room])
        station.path[path].close_door()
        msg += "Door between %s and %s is \n" % (current_room, room)

    elif effect == "DANGER":

        #if no intruders #FIXME!!!
        msg += apply_danger(station, room)


    station.rooms[room].open_room()
    _, room_name = station.rooms[room].check_room()
    msg += "'%s' is explored\n" % room_name

    return noise, msg


def noise_dice(station: Station, player: Person, room: str) -> str:

    roll = game1.get_noise_roll().roll()
    msg = "Noise roll: %s\n" % roll

    if roll in ["1", "2", "3", "4"]:

        to_room = station.rooms[room].corridors[roll]
        noise_path = station.rooms[room].get_path_from_corridor(roll)

        if station.path[noise_path].is_noise():
            msg += "Too noisy in path %s towards to %s room\n" % (noise_path, to_room)
            msg += "ENCOUNTER!\n"
            msg += resolve_encounter(station, room)

        else:
            station.path[noise_path].make_noise()
            msg += "Was a noise in path %s towards to %s room\n" % (noise_path, to_room)

    elif roll == "SILENCE":

        if player.state["slime"]:
            msg += "Apply 'DANGER' because of SLIME\n"
            msg += apply_danger(station, room)
        else:
            return msg

    elif roll == "DANGER":
        #FIXME
        #if not intruders in near rooms
        msg += apply_danger(station, room)

    return msg


def move(station: Station, player: Person, room: str):

    msg = ""

    if room == "0":
        msg += "You couldn't enter to the Technical corridor.\n"
        return False, msg

    current_room = player.get_location()
    player_name = player.get_name()

    if room == current_room:
        msg += "You are already in the room.\n"
        return False, msg

    # if room connected
    connected = station.check_connected(current_room, room)
    msg += "%s try to move from %s to %s ...\n" % (player_name, current_room, room)

    if not connected:
        msg += "Room %s is not connected to %s.\n" % (current_room, room)
        return False, msg

    # Check the door between the rooms is open
    res, path = station.get_path(current_room, room)
    if not res:
        msg += "Error! No path from %s to %s.\n" % (current_room, room)
        return False, msg

    if station.path[path].is_closed():
        msg += "Door from %s to %s is closed.\n" % (current_room, room)
        return False, msg

    # Move to room

    station.move(player, current_room, room)
    #player.set_location(room)  # done during move()

    explored, room_name = station.rooms[room].check_room()
    msg += "%s entering to the room %s: '%s'\n" % (player_name, room, room_name)

    if explored:

        noise, msg1 = enter_explored_room(station, room)

    else:  # if room is unexplored

        noise, msg1 = discover_room(station, current_room, room, player)

    msg += msg1

    if noise:

        msg += noise_dice(station, player, room)

    msg += in_combat(station, room)

    return True, msg

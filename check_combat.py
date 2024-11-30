from station import Station

def in_combat(station: Station, room: str):

    msg = ""
    players = station.rooms[room].check_players()
    intruders = station.rooms[room].check_intruders()

    if not intruders:
        for pl in station.rooms[room].players:
            if pl.is_combat():
                pl.clear_combat()
                msg += "\nCombat mode cleared."

    elif players and intruders:

        # In combat
        for pl in station.rooms[room].players:
            pl.combat()
        for intr in station.rooms[room].intruders:
            intr.combat()
        msg += "\nCombat mode set."

    else:
        for intr in station.rooms[room].intruders:
            intr.clear_combat()

    return msg

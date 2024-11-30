import config as CFG
from game import Game

from check_alive import check_creature_alive
from check_combat import in_combat
from check_injury import injury_effect
from event_intruder_retreat import retreat

def melee_attack(game1: Game, user: str, intruder_name: str) -> (bool, str):

    msg = "\nMelee attack.."
    station = game1.get_station()
    person = game1.get_user_player(user)
    room = person.state["room_id"]
    
    intruder = station.rooms[room].get_alien_intruder(intruder_name)
    if not intruder:
        msg += "\nError: choose proper target intruder."
        return False, msg

    if room != intruder.state["room_id"]:
        msg += "\n{char} can't attack {alien} from a different room.".format(char=character,alien=alien)
        return False, msg

    character = person.description["character"]
    alien = intruder.description["name"]
    target = intruder.description["character"]
    
    #1
    person.deck["discard"].add("CONTAMINATION")
    msg += "\n%s get contamination card." % character

    #2
    effect = ""
    combat = game1.get_combat_roll().roll()
    msg += "\nCombat result: %s" % combat
    if combat == "-":
        person.serious_wound()
        msg += "\n%s miss and get a serious wound." % character

    elif combat == "CREEPER":
        if target == "LARVA" or target == "CREEPER":
            intruder.hit(1)
            msg += "\n%s get 1 injury." % alien
            out, effect = injury_effect(intruder)
            msg += out
        else:
            person.serious_wound()
            msg += "\n{char} miss and get a serious wound from {alien}.".format(char=character,alien=alien)

    elif combat == "ADULT":
        if (target == "LARVA") or \
           (target == "CREEPER") or \
           (target == "ADULT"):
            intruder.hit(1)
            msg += "\n%s get 1 injury." % alien
            out, effect = injury_effect(intruder)
            msg += out
        else:
            person.serious_wound()
            msg += "\n{char} miss and get a serious wound from {alien}.".format(char=character,alien=alien)

    elif combat == "+" or combat == "++":
        intruder.hit(1)
        msg += "\n%s get 1 injury." % alien
        out, effect = injury_effect(intruder)
        msg += out

    res, out = check_creature_alive(station, person, room)
    msg += out

    if effect == "DIE":
        res, out = check_creature_alive(station, intruder, room)
        msg += out
    elif effect == "RETREAT":
        msg += retreat(station, intruder, room)

    msg += in_combat(station, room)
    
    if CFG.DEBUG:
        print(msg) 

    return True, msg

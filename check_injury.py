import random
from config import ENDURANCE
from intruder import Intruder


def check_retreat_blood() -> (bool, int):
    blood = random.choice(ENDURANCE)
    if blood == "-":
        return True, 0
    else:
        return False, int(blood)


def check_injury(intruder: Intruder, blood: int) -> str:

    msg = ""

    # How many hits currently
    hits = intruder.get_hits()
    name = intruder.description["name"]

    msg += "\n%s has %s endurance with %s hits" % (name, blood, hits)
    if blood <= hits:
        intruder.die()
        msg += "\n%s die." % name
        return msg, "DIE"
    return msg, "INJURY"


def injury_effect(intruder: Intruder) -> (str, str):
    
    msg = "\nCheck alien endurance.."
    alien = intruder.description["character"]
    name = intruder.description["name"]

    if alien == "LARVA" or alien == "EGG":
        intruder.die()
        msg += "\n%s die." % name
        return msg, "DIE"

    elif alien == "CREEPER" or alien == "ADULT":

        retreat, blood = check_retreat_blood()
        if retreat:
            msg += "\n%s retreat" % name
            return msg, "RETREAT"

        out, effect = check_injury(intruder, blood)
        msg += out
        return msg, effect
    
    elif alien == "BREEDER" or alien == "QUEEN":

        retreat, blood = check_retreat_blood()
        retreat2, blood2 = check_retreat_blood()
        blood_sum = 0

        # Two cards
        if retreat and retreat2:
            msg += "\n%s retreat" % name
            return msg, "RETREAT"

        if not (retreat or retreat2):
            blood_sum = blood + blood2
            out, effect = check_injury(intruder, blood_sum)
            msg += out
            return msg, effect
        
        # Third card
        retreat3, blood3 = check_retreat_blood()

        if retreat3:
            msg += "\n%s retreat" % name
            return msg, "RETREAT"
        else:
            blood_sum += blood3
            out, effect = check_injury(intruder, blood_sum)
            msg += out
            return msg, effect




    

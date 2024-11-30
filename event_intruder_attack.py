import random

import config as CFG
from person import Person

def attack_check(person: Person, attacker: str):

    msg = "\nCheck attack.."

    card = random.choice(CFG.INTRUDER_ATTACKS)
    msg += "\nOpen card: %s" % card

    intruders_list = CFG.ATTACK[card]
    msg += "\nIntruders list: %s" % ",".join(intruders_list)

    if not attacker in intruders_list:
        msg += "\nAttack misses"
        return msg
    
    else:
        msg += "\n\n%s attack!" % card
        msg += intruder_attack(person, card)

    return msg


def intruder_attack(person: Person, attack: str):

    msg = ""

    if attack == "BITE":
        msg = bite(person)
    elif attack == "SCRATCH":
        msg = scratch(person)
    elif attack == "TAIL":
        msg = tail(person)
    elif attack == "CLAW":
        msg = claw(person)
    elif attack == "SLIME":
        msg = slime(person)
    #TODO: transformation, frenzy, summoning

    return msg

def bite(person):

    if person.get_serious_wounds() == 2:
        person.die()
        msg = "\nPerson die!"
    else:
        person.serious_wound()
        msg = "\nSerious wound"

    return msg

def scratch(person):

    person.light_wound()
    # add Contamination card
    person.deck["discard"].add("CONTAMINATION")
    msg = "\nLight wound and Contamination card"
    
    return msg

def tail(person):

    if person.get_serious_wounds() >= 1:
        person.die()
        msg = "\nPerson die!"
    else:
        person.serious_wound()
        msg = "\nSerious wound"

    return msg

def claw(person):

    person.light_wound()
    person.light_wound()
    # add Contamination card
    person.deck["discard"].add("CONTAMINATION")
    msg = "\n2 Light wounds and Contamination card"
    
    return msg

def slime(person):

    person.slime()
    # add Contamination card
    person.deck["discard"].add("CONTAMINATION")
    msg = "\nSlime and Contamination card"
    
    return msg

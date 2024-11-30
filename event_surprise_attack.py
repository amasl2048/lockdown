import random

import config as CFG
from station import Station
from person import Person
from intruder import Intruder
import event_intruder_attack

def larva_infest(station: Station, person: Person, intruder: Intruder):

    msg = "\nLARVA infest"
    # remove LARVA
    station.remove_intruder(intruder)

    if person.check_infected():
        msg += "\n%s already infected." % person.get_character()
    else:
        person.infected()

    # add contamination card
    person.deck["discard"].add("CONTAMINATION")
    msg += "\n%s get a Contamination card" % person.get_character()

    return msg

def surprise_attack(station: Station, 
                    person: Person, 
                    intruder: Intruder):

    msg = ""
    token = intruder.get_character()

    cards_in_hand = person.check_hand()
    number = random.choice(CFG.INTRUDERS_TOKENS_NUMBERS)
    msg += "\nYou have %s cards vs. %s intruder number" % \
        (cards_in_hand, number)

    if cards_in_hand < number:
        msg += "\nSurprise attack"

        if token == "LARVA":
            msg += larva_infest(station, person, intruder)
            return msg

        msg += event_intruder_attack.attack_check(person, token)
    else:
        msg += "\nNo intruder's attack"

    return msg

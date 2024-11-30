#!/usr/bin/python3
import random
import pprint
pp = pprint.PrettyPrinter(indent=4)

import config as CFG
from create_player import create_player
import event_intruder_attack

name = "TEST"
color = "GREEN"
character = "PILOT"
player = create_player(name, color, character)
player.show()

for _ in range(10):
    attacker = random.choice(CFG.START_INTRUDERS_TOKENS)
    print("\n=>", attacker)
    if attacker == "LARVA" or attacker == "-":
        continue

    msg = event_intruder_attack.attack_check(player, attacker)
    print(msg)

    if not msg.strip() == "No attack": 
        player.show()

if not player.check_alive():
    print("DEAD!!!")

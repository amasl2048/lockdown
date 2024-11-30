#!/usr/bin/python3
import pprint
pp = pprint.PrettyPrinter(indent=4)

from start_game import game1
from intruder import Intruder
from create_player import create_player

from action_melee_attack import melee_attack
from check_alive import check_creature_alive

name = "PLAYER"
color = "GREEN"
character = "PILOT"
player = create_player(name, color, character)
res, msg = game1.add_player(player)
print(msg)

station1 = game1.get_station()
player1 = game1.get_player(1)
current_room = player1.get_location()
print("\nPlayer1:")
player1.show()
station1.rooms[current_room].show()

token = "BREEDER"
room = "17"

intruder = Intruder(
            name=token,
            character=token,
            number=1
            )

# intruder enter the room
station1.enter_room(intruder, room)
station1.state["intruders_counter"] += 1
print("\n%s enter room %s." % (token, room))

station1.rooms[current_room].show()

for _ in range(10):
    res, msg = melee_attack(game1, name, token)
    if "retreat" in msg:
        break

station1.rooms[current_room].show()

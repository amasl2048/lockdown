#!/usr/bin/python3
import pprint
pp = pprint.PrettyPrinter(indent=4)

from start_game import game1
import action_move

station1 = game1.get_station()
player1 = game1.get_player()
current_room = player1.get_location()

print("\nPlayer1:")
player1.show()
station1.rooms[current_room].show()


for rm in ["1", "21", "2", "1", "17"]:

    print("\n-> Move to %s" % rm)
    action_move.move(station1, player1, rm)
    print()
    station1.rooms[rm].show()

    res, pt = station1.get_path(current_room, rm)
    if res:
        station1.path[pt].show()

    current_room = rm


for rm in ["2", "21", "1", "17"]:

    action_move.move(station1, player1, rm)
    print()
    station1.rooms[rm].show()

    res, pt = station1.get_path(current_room, rm)
    if res:
        station1.path[pt].show()

    current_room = rm


assert(player1.get_location() == "17")

players_names = station1.rooms["17"].get_players_names()
print(players_names)
assert("Andrew" in players_names)

print("\nPlayer1:")
player1.show()

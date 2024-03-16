#!/usr/bin/python3
import pprint
pp = pprint.PrettyPrinter(indent=4)

from start_game import game1
player1 = game1.get_player()

station1 = game1.get_station()

if  __name__ == "__main__":

    print("\nPlayer1:")
    player1.show()

    print("\nRooms:")
    for rm in ["1", "2", "17", "21"]:

        print("## ", rm)
        station1.rooms[rm].show()

        print("Path:")
        pt = station1.rooms[rm].get_path()
        print(pt)
        for p in pt:
            station1.path[str(p)].show()

        print("\nCorridors:")
        for cor in range(1,5):
            cr = station1.rooms[rm].corridors[str(cor)]
            print("Corridor %s -> room %s" % (cor, cr))


    print("\nPaths:")
    for p in ["1", "2", "3", "4"]:

        print("##", p)
        corridors = station1.path[p].get_corridors()
        print("Corridors:", corridors)
        room1, room2 = station1.path[p].get_rooms()
        print("connected rooms %s -(%s)- %s " % (room1, corridors, room2))

        # same path in both rooms
        assert(str(station1.rooms[room1].path[room2]) == p)
        assert(str(station1.rooms[room2].path[room1]) == p)

        # same corridors to same rooms
        for cor in corridors:
            assert(str(station1.rooms[room1].corridors[cor]) == room2)
            assert(str(station1.rooms[room2].corridors[cor]) == room1)

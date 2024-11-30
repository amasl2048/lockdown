from flask import render_template

import config as CFG


def section_info(station, section: tuple) -> list:

    room_info = []

    for num in section:

        room = station.rooms[str(num)]

        explored, name = room.check_room()

        if not explored:
            color = "DarkGrey"
        else:
            color = "Black"

        effect = room.effect()
        items = room.items()

        players = room.get_players_characters()
        intruders = room.get_intruders_names()

        corridors = []
        for cor in ["1", "2", "3", "4"]:
            route = cor
            path = room.get_path_from_corridor(cor)
            state = station.path[path].show_state()

            remote = room.get_remote_room(cor)
            if remote == "0":
                remote = "Technical corridor"

            corridors.append((route, state, remote)
            )

        room_info.append((color, str(num), name, effect, items,
                          " ".join(players),
                          " ".join(intruders),
                          corridors
                         )
        )

    return room_info


def render_station(user, game, station_map):

    station1 = game.get_station()
    player1 = game.get_user_player(user)
    if not player1:
        current_room = ""
        rooms_list = []
    else:
        current_room = player1.get_location()
        rooms_list = station1.rooms[current_room].get_connected_rooms()

    room_info = []

    for section in [CFG.SECTIONS[0]]:  #FIXME: CFG.SECTIONS
        room_info.append(section_info(station1, section))

    burnout = station1.burnout()
    destruction = station1.destruction()

    connected_rooms = " ".join(rooms_list)

    return render_template("station.html",
                            user = user,
                            room=current_room,
                            connected_rooms=connected_rooms,
                            rooms_list=rooms_list,
                            room_info=room_info,
                            burnout=burnout,
                            destruction=destruction,
                            map_png=station_map
                            )
